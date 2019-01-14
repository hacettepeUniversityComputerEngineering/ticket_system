from django.db import models
from event.models import Salon, Block, Seat, Event
from user.models import User
# from django.contrib.auth.models import User


class Ticket(models.Model):
    total_ticket_price = models.FloatField()
    ticket_count = models.IntegerField()
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, blank=True, null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Purchase(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ConvertMoney(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
