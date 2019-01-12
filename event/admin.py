from django.contrib import admin
from event.models import Event,Category

admin.site.register(Event)
admin.site.register(Category)

from .models import Category, EventOwner, Director, Actor, City, Building, Event, Schedule, Salon, Date, Seance, Block, Seat, CityEvent

admin.site.register(Event)
admin.site.register(EventOwner)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(City)
admin.site.register(Building)
admin.site.register(Schedule)
admin.site.register(Salon)
admin.site.register(Date)
admin.site.register(Seance)
admin.site.register(Block)
admin.site.register(Seat)
admin.site.register(CityEvent)
