from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserType(AbstractUser):
    is_onlyUser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class User(models.Model):
    user = models.OneToOneField(UserType, on_delete=models.CASCADE, null=True, related_name='onlyUser')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=200)
    money = models.FloatField(null=True)
    credit_card_number = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class PastEvent(models.Model):
    name = models.CharField(max_length=200)


class UserPastEvent(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    past_event = models.ForeignKey(PastEvent, on_delete=models.CASCADE)
