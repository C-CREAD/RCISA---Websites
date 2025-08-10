from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'full_name', 'email', 'phone_number', 'status', 'congregation')
    list_filter = ('status', 'congregation')
    search_fields = ('username', 'full_name', 'email', 'phone_number', 'status', 'congregation')


admin.site.register(CustomUser, CustomUserAdmin)