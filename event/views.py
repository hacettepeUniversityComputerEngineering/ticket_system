from event.forms import SearchForm, SelectCategory, SelectCity, SelectPersonCount, PaymentForm, NewEventForm, \
    NewActorForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Event, CityEvent, Seance, Salon, Actor, City, Schedule, Director, EventOwner,ActorEvent


# her etkinliğin fiyatı olmalı
# her etkinlik için açıklama attribute'u ekle

# elmas
def call_home(request):
    form = SearchForm()
    city_form = SelectCity()
    category_form = SelectCategory
    all_events = Event.objects.all()
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
    return render(request, 'home.html',
                  {"form": form, "all_events": all_events, "city_form": city_form, "category_form": category_form})


# seda
def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    cities = CityEvent.objects.filter(event__pk=pk).order_by('city')
    actor_events = ActorEvent.objects.filter(event__pk=pk)
    actors = []
    for ae in actor_events:
        actors.append(Actor.objects.filter(pk=ae.actor.pk))

    for city in cities:
        print(city.event.name)
    seances = Seance.objects.all()
    new_actor_form = NewActorForm()
    if request.method == 'POST':
        new_actor_form = NewActorForm(request.POST)
        if new_actor_form.is_valid():
            actor_name = new_actor_form.cleaned_data['actor_name']
            create_new_actor(actor_name, pk)
    return render(request, 'event_details.html', {'event': event,
                                                  'cities': cities,
                                                  'seances': seances,
                                                  'actors': actors,
                                                  'new_actor_form': new_actor_form,
                                                  })


def create_new_actor(name, event_pk):
    this_event = Event.objects.get(pk=event_pk)
    try:
        this_actor = Actor.objects.get(name=name)
    except:
        Actor.objects.update_or_create(name=name, event=this_event)
        this_actor = Actor.objects.get(name=name, event=this_event)
    ActorEvent.objects.update_or_create(event=this_event,actor=this_actor)


# seda
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
    person_count_form = SelectPersonCount()
    if request.method == 'POST':
        person_count_form = SelectPersonCount(request.POST)
        if person_count_form.is_valid():
            person_count = person_count_form.cleaned_data['person_count']
            print(person_count)
    return render(request, 'buy_ticket.html', {'person_count_form': person_count_form})


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
            create_new_event(event_name, category_name, event_owner, director)
    return render(request, 'new_event.html', {'new_event_form': new_event_form})


def create_new_event(event_name, category_name, event_owner, director):
    Director.objects.update_or_create(name=director)
    this_director = Director.objects.get(name=director)

    EventOwner.objects.update_or_create(name=event_owner)
    this_owner = EventOwner.objects.get(name=event_owner)

    Category.objects.update_or_create(name=category_name)
    this_category = Category.objects.get(name=category_name)

    print(this_category)
    Event.objects.update_or_create(name=event_name, director=this_director, event_owner=this_owner,
                                   category_name=this_category)
