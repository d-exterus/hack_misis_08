from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.CharField(max_length=20)


class UserAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    login = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)