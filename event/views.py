
from event.forms import SearchForm
from event.models import Event, Category
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Event, CityEvent, Seance, Salon, Actor

def store_database():
    event_list = open("txt_files/events.txt", "r").read().split("\n\n")
    for event in event_list:
        split_list = event.split("\n")
        for i in split_list:
            if "Event_name: " in i:
                event_name = i.split("Event_name: ")[1]
            elif "Kategori: " in i:
                event_category = i.split("Kategori: ")[1]
            elif "Yönetmen: " in i:
                director = i.split("Yönetmen: ")[1]
            elif "Yazan: " in i:
                writer = i.split("Yazan: ")[1]
            elif "Oyuncular: " in i:
                all_actors = i.split("Oyuncular: ")[1]
            elif "Vizyon Tarihi: " in i:
                first_date = i.split("Vizyon Tarihi: ")[1]
            elif "Süre: " in i:
                duration = i.split("Süre: ")[1]
            elif "Vizyon Tarihi: " in i:
                category = i.split("Tür: ")[1]
            elif "Content: " in i:
                content = i.split("Content: ")[1]
        Category.objects.update_or_create(name="tiyatro")
        Category.objects.update_or_create(name="sinema")
        this_category = Category.objects.get(name=event_category)
        Event.objects.update_or_create(name=event_name, category_name=this_category)






def call_home(request):
    # store_database()
    form = SearchForm()
    all_events = Event.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            event_name = form.cleaned_data.get('name')
            try:
                event = Event.objects.get(name=event_name)
                return redirect('event_details', pk=event.pk)
            except:
                print("yok böyle bişi")
                return redirect('home_page')

    return render(request, 'home.html', {"form": form, "all_events": all_events})



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
