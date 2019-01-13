from event.forms import SearchForm, SelectCategory, SelectCity, SelectPersonCount, PaymentForm, NewEventForm, \
    NewActorForm, NewSeanceForm, NewCityForm, NewBuildingForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Category, Event, CityEvent, Seance, Actor, City, Schedule, Director, EventOwner, ActorEvent, \
    BuildingEvent, SalonEvent, Building, Salon, Comment, UserInformation
from django.views.generic import CreateView
from user.models import User
from django.db.models import Avg, Count
from django.contrib.auth import get_user_model
from ticket_system.decorators import admin_required
from django.contrib.auth.forms import UserCreationForm



# **** YAPILACAKLAR ****
# her etkinliğin fiyatı olmalı
# her etkinlik için açıklama attribute'u ekle


# elmas
def call_home(request):
    form = SearchForm()
    city_form = SelectCity()
    category_form = SelectCategory
    all_events = Event.objects.all()
    all_events_number = all_events.aggregate(Count('pk'))
    all_events_number = all_events_number['pk__count']
    if request.method == 'POST':
        if "search" in request.POST:
            form = SearchForm(request.POST)
            if form.is_valid():
                event_name = form.cleaned_data.get('name')
                try:
                    event = Event.objects.get(name=event_name)
                    return redirect('event_details', pk=event.pk)
                except:
                    print("yok böyle bişi")
                    return redirect('home_page')
        elif "city_category" in request.POST:
            city_form = SelectCity(request.POST)
            category_form = SelectCategory(request.POST)
            if city_form.is_valid():
                city_name = city_form.cleaned_data.get('city_name')
            if category_form.is_valid():
                category_name = category_form.cleaned_data.get('category_name')
            all_events = get_events(city_name, category_name)
            # all_events_number = all_events.aggregate(Count('pk'))
            # all_events_number = all_events_number['pk__count']
        elif "delete_event" in request.POST:
            event_pk = request.POST['delete_event']
            Event.objects.get(pk=event_pk).delete()

    return render(request, 'home.html',
                  {"form": form, "all_events": all_events, "city_form": city_form, "category_form": category_form,
                   "all_events_number": all_events_number})


# seda


# @onlyUser_required
# @admin_required
def event_details(request, pk):
    comment_count = 0
    print(request.user.pk)
    event = Event.objects.get(pk=pk)
    city_event = CityEvent.objects.filter(event__pk=pk).order_by('city')
    building_event = BuildingEvent.objects.filter(event__pk=pk)
    salon_event = SalonEvent.objects.filter(event__pk=pk)
    seances = Seance.objects.filter(event__pk=pk)
    comments = Comment.objects.filter(event__pk=pk)

    # seances = Seance.objects.all()
    new_actor_form = NewActorForm()
    new_seance_form = NewSeanceForm()
    new_city_form = NewCityForm()
    new_building_form = NewBuildingForm()
    comment_form = CommentForm()


    if request.method == 'POST':
        if "city" in request.POST:
            new_city_form = NewCityForm(request.POST)
            if new_city_form.is_valid():
                city_name = new_city_form.cleaned_data['city_name']
                create_city(city_name, pk)
        if "building" in request.POST:
            new_building_form = NewBuildingForm(request.POST)
            if new_building_form.is_valid():
                building_name = new_building_form.cleaned_data['building_name']
                city_pk = request.POST['city_pk']
                create_new_building(building_name, pk, city_pk)


        elif "seance" in request.POST:
            new_seance_form = NewSeanceForm(request.POST)
            if new_seance_form.is_valid():
                salon_name = new_seance_form.cleaned_data['salon_name']
                date = new_seance_form.cleaned_data['date']
                time = new_seance_form.cleaned_data['time']
                city_pk = request.POST['city_pk']
                building_pk = request.POST['building_pk']
                create_new_seance(building_pk, salon_name, date, time, pk)

        elif "actor" in request.POST:
            new_actor_form = NewActorForm(request.POST)
            if new_actor_form.is_valid():
                actor_name = new_actor_form.cleaned_data['actor_name']
                create_new_actor(actor_name, pk)

        elif "delete_city" in request.POST:
            city_pk = request.POST['delete_city']
            City.objects.get(pk=city_pk).delete()

        elif "delete_building" in request.POST:
            building_pk = request.POST['delete_building']
            Building.objects.get(pk=building_pk).delete()

        elif "delete_seance" in request.POST:
            seance_pk = request.POST['delete_seance']
            salon_pk = request.POST['delete_salon']
            Seance.objects.get(pk=seance_pk).delete()
            SalonEvent.objects.get(pk=salon_pk).delete()

        elif "comment" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.cleaned_data['comment']
                create_comment(comment, pk)
    comment_count = Comment.objects.filter(event__pk=pk).aggregate(Count('pk'))['pk__count']

    actor_events = ActorEvent.objects.filter(event__pk=pk)
    actors = []

    for ae in actor_events:
        actors += Actor.objects.filter(pk=ae.actor.pk).values()

    return render(request, 'event_details.html', {
        # 'event': event,
        'city_event': city_event,
        'salon_event': salon_event,
        'building_event': building_event,
        'seances': seances,
        'actors': actors,
        'new_actor_form': new_actor_form,
        'new_seance_form': new_seance_form,
        'new_city_form': new_city_form,
        'new_building_form': new_building_form,
        'comment_form': comment_form,
        'comments': comments,
        'comment_count': comment_count,
        'event': event

    })


def create_comment(comment, event_pk):
    event = Event.objects.get(pk=event_pk)
    # userinf = UserInformation.objects.get(user__pk=request.user.pk)
    Comment.objects.update_or_create(text=comment, event=event)


def create_new_building(building_name, event_pk, city_pk):
    event = Event.objects.get(pk=event_pk)
    city = City.objects.get(pk=city_pk)
    Building.objects.update_or_create(city=city, name=building_name)
    building = Building.objects.get(city=city, name=building_name)
    BuildingEvent.objects.update_or_create(building=building, event=event)


def create_new_seance(building_pk, salon_name, date, time, event_pk):
    event = Event.objects.get(pk=event_pk)
    building = Building.objects.get(pk=building_pk)
    Salon.objects.update_or_create(name=salon_name, building=building)
    salon = Salon.objects.get(name=salon_name, building=building)
    SalonEvent.objects.update_or_create(salon=salon, event=event)
    salon = Salon.objects.get(name=salon_name, building=building)

    Seance.objects.update_or_create(date=date, time=time, salon=salon, event=event)


def create_city(city_name, pk):
    this_event = Event.objects.get(pk=pk)
    try:
        this_city = City.objects.get(name=city_name)
    except:
        City.objects.update_or_create(name=city_name)
        this_city = City.objects.get(name=city_name)
    CityEvent.objects.update_or_create(city=this_city, event=this_event)


def create_new_actor(name, event_pk):
    this_event = Event.objects.get(pk=event_pk)
    try:
        this_actor = Actor.objects.get(name=name)
    except:
        Actor.objects.update_or_create(name=name)
        this_actor = Actor.objects.get(name=name)
    ActorEvent.objects.update_or_create(event=this_event, actor=this_actor)


def get_events(city_name, category_name):
    selected_events = []
    c_e_objects = CityEvent.objects.filter(city__name=city_name)
    event_objects = Event.objects.filter(category_name__name=category_name)
    for ce in c_e_objects:
        for event in event_objects:
            if ce.event == event:
                selected_events.append(event)
    return selected_events


def buy_ticket(request):
    # event = Event.objects.all(pk=pk)
    price = 32
    person_count_form = SelectPersonCount()
    if request.method == 'POST':
        person_count_form = SelectPersonCount(request.POST)
        if person_count_form.is_valid():
            person_count = person_count_form.cleaned_data['person_count']
            price = person_count * 12
    return render(request, 'buy_ticket.html', {'person_count_form': person_count_form, 'price': price})


def payment(request):
    payment_form = PaymentForm()
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            name_surname = payment_form.cleaned_data['name_surname']
            tckn = payment_form.cleaned_data['tckn']
            e_mail = payment_form.cleaned_data['e_mail']
            credit_card_number = payment_form.cleaned_data['credit_card_numbers']
            phone_number = payment_form.cleaned_data['phone_number']
            last_usage_date = payment_form.cleaned_data['last_usage_date']
            security_number = payment_form.cleaned_data['security_number']
    return render(request, 'payment_screen.html', {'payment_form': payment_form})


def schedule(request):
    Schedule.objects.filter()


def new_event(request):
    new_event_form = NewEventForm()
    if request.method == 'POST':
        new_event_form = NewEventForm(request.POST)
        if new_event_form.is_valid():
            event_name = new_event_form.cleaned_data['event_name']
            category_name = new_event_form.cleaned_data['category_name']
            event_owner = new_event_form.cleaned_data['event_owner']
            director = new_event_form.cleaned_data['director']
            content = new_event_form.cleaned_data['content']
            create_new_event(event_name, category_name, event_owner, director, content)
            return redirect('home_page')
    return render(request, 'new_event.html', {'new_event_form': new_event_form})


def create_new_event(event_name, category_name, event_owner, director, content):
    Director.objects.update_or_create(name=director)
    this_director = Director.objects.get(name=director)

    EventOwner.objects.update_or_create(name=event_owner)
    this_owner = EventOwner.objects.get(name=event_owner)

    Category.objects.update_or_create(name=category_name)
    this_category = Category.objects.get(name=category_name)

    Event.objects.update_or_create(name=event_name, director=this_director, event_owner=this_owner,
                                   category_name=this_category, text=content)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})