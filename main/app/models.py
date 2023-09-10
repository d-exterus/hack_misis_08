from django.db import models


class ClubChoices(models.TextChoices):
    HACK = "HACK"
    GAME = "GAME"
    DESIGN = "DESIGN"
    ROBOTS = "ROBOTS"
    AI = "AI"
    LECTURES = "LECTURES"


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.CharField(max_length=20)
    bio = models.TextField()
    is_searching = models.BooleanField(default=False)
    club = models.CharField(max_length=8, choices=ClubChoices.choices, default=ClubChoices.HACK)
    count = models.PositiveIntegerField(default=0)


class UserAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    login = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)


class Team(models.Model):
    name = models.CharField(max_length=50)
    club = models.CharField(max_length=8, choices=ClubChoices.choices, default=ClubChoices.HACK)
    users = models.ManyToManyField(User)
    count = models.PositiveIntegerField(default=0)
