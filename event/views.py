from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Event, CityEvent, Seance, Salon, Actor
# Create your views here.


def deneme_event(request):
    return render(request, 'event_details.html', {})


def deneme_home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


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
