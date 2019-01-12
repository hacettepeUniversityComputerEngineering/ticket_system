from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    money = models.FloatField()
    credit_card_numer = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)


class PastEvent(models.Model):
    name = models.CharField(max_length=200)


class UserPastEvent(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    past_event = models.ForeignKey(PastEvent, on_delete=models.CASCADE)
