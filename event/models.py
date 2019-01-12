from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EventOwner(models.Model):
    web_site = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Salon(models.Model):
    name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    poster = models.ImageField
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    event_owner = models.ForeignKey(EventOwner, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return self.name


class ActorEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)


class CityEvent(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    publishing_date_of_schedule = models.TimeField()


class Date(models.Model):
    date = models.DateField()
    time = models.TimeField()


class Seance(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    time = models.ForeignKey(Date, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Block(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)


class Seat(models.Model):
    row = models.CharField(max_length=200)
    number = models.IntegerField()
    seat = models.FloatField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
