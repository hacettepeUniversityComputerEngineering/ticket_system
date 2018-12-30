from django.db import models
from event.models import Salon, Block, Seat, Date, Event
from user.models import User
# Create your models here.

class Ticket(models.Model):
    total_ticket_price = models.FloatField()
    ticket_count = models.IntegerField()
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    block = models.ForeignKey(Block,on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Purchase(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class ConvertMoney(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
