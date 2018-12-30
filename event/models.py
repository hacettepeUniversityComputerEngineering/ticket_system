from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)


class Event(models.Model):
    name = models.CharField(max_length=200)
    poster = models.ImageField
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)


class EventOwner(models.Model):
    web_site = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Director(models.Model):
    name = models.CharField(max_length=200)


class Actor(models.Model):
    name = models.CharField(max_length=200)


class EventCreation(models.Model):
    event_owner = models.ForeignKey(EventOwner, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()


class EventSchedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    publishing_date_of_schedule = models.TimeField()


class City(models.Model):
    name = models.CharField(max_length=200)


class CityEvent(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Building(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class BuildingEvent(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Salon(models.Model):
    name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


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
