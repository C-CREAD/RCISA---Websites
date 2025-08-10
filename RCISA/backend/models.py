from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    password = models.CharField()
    congregation = models.CharField(choices=[
        ("pretoria town", "Pretoria Town"),
        ("pretoria silverton", "Pretoria Silverton"),
        ("durban", "Durban"),
        ("kempton park", "Kempton Park"),
        ("mamelodi", "Mamelodi"),
        ("polokwane", "Polokwane"),
        ("n/a", "N/A")
    ], default="n/a")
    status = models.CharField(choices=[
        ("visitor", "Visitor"),
        ("member", "Member"),
        ("reverent", "Reverent")
    ], default="visitor")
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} | {self.status}"


class Congregation(models.Model):
    congregation = models.CharField(unique=True)
    location = models.CharField()
    status = models.CharField(choices=[
        ("active", "Active"),
        ("disbanded", "Disbanded")
    ], default="active")

    def __str__(self):
        return f"{self.congregation} | {self.status}"


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    congregation = models.ForeignKey(Congregation, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} | {self.congregation}"