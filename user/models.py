from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class OnlyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    money = models.FloatField()
    credit_card_number = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)



class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=200)
    money = models.FloatField(null=True)
    credit_card_number = models.CharField(max_length=200, null=True)


class PastEvent(models.Model):
    name = models.CharField(max_length=200)


class UserPastEvent(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    past_event = models.ForeignKey(PastEvent,on_delete=models.CASCADE)