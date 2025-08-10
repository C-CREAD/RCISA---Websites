from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError
import re
from phonenumbers import parse, is_valid_number

User = get_user_model()


def validate_phone_number(value):

    try:
        # Remove whitespace characters from phone number fields
        value = value.replace(" ", "")
        phone = parse(value, None)
        if not is_valid_number(phone):
            raise ValidationError("Enter a valid phone number")
        print(phone)
        return phone
    except:
        # Fallback regex validation if phonenumbers lib fails
        if not re.match(r'^\+?[0-9]{10,15}$', value):
            raise ValidationError("Phone number must be 10-15 digits, optionally starting with +")


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=CustomUser.objects.all())
    ])

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("full_name", "username", "phone_number", "email", "password", "congregation", "status")

    def validate(self, data):
        """
        Validate all data fields
        """
        if not data.get('username'):
            raise serializers.ValidationError({"username": "Please enter a valid username"})

        if not data.get('full_name') or len(data.get('full_name').split()) < 2:
            raise serializers.ValidationError({"full_name": "Please enter your first and last names"})

        if not data.get('email'):
            raise serializers.ValidationError({"email": "Please enter your email"})

        if not data.get('password'):
            raise serializers.ValidationError({"password": "Please enter a valid password"})

        if data.get('phone_number'):
            self.phone_number = validate_phone_number(data.get('phone_number'))

        return data

    def create(self, data):
        return CustomUser.objects.create_user(
            username=data["username"],
            full_name=data["full_name"],
            phone_number=data["phone_number"],
            email=data["email"],
            password=data["password"],
            congregation=data["congregation"],
            status=data["status"]
        )


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Custom claims
        token['username'] = user.username
        token['status'] = user.status
        return token