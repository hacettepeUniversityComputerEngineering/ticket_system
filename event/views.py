from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Category, Event, CityEvent, Seance, Salon, Actor
from ticket_system.forms import SignUpForm
from user.models import User
# Create your views here.


def deneme_event(request):
    return render(request, 'event_details.html', {})


def deneme_home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    cities = CityEvent.objects.filter(event__pk=pk).order_by('city')
    actors = Actor.objects.filter(event=event.pk)
    for actor in actors:
        print(actor)

    return render(request, 'event_details.html', {'event': event,
                                                  'cities': cities,
                                                  'actors': actors,
                                                  })


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'onlyUser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_page')
