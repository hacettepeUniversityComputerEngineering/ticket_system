from audioop import reverse

from django.shortcuts import render
from event.forms import SearchForm
from event.models import Event, Category
from django.shortcuts import redirect


def store_database():
    event_list = open("txt_files/events.txt","r").read().split("\n\n")
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
        Event.objects.update_or_create(name=event_name,category_name=this_category)





# Create your views here.
def event_details(request, pk):
    return render(request, 'event_details.html', {})


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
