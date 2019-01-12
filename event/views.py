from event.forms import SearchForm, SelectCategory, SelectCity
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Event, CityEvent, Seance, Salon, Actor


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
                city_name = city_form.cleaned_data.get('name')
                print(city_name)
            if category_form.is_valid():
                category_name = category_form.cleaned_data.get('name')
                print(category_name)
            return redirect('home_page')

    return render(request, 'home.html',
                  {"form": form, "all_events": all_events, "city_form": city_form, "category_name": category_form})


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    cities = CityEvent.objects.filter(event__pk=pk).order_by('city')
    actors = Actor.objects.filter(event__pk=pk)
    for city in cities:
        print(city.event.name)
    seances = Seance.objects.all()
    return render(request, 'event_details.html', {'event': event,
                                                  'cities': cities,
                                                  'seances': seances,
                                                  'actors': actors})


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
