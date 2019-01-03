from django.urls import path
from . import views

urlpatterns = [
    path('event_details', views.deneme_event, name='event_page'),
    path('', views.deneme_home, name='home_page'),

]
