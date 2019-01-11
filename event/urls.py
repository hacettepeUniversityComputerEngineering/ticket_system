from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('event_details', views.deneme_event, name='event_page'),
    path('', views.deneme_home, name='home_page'),
    url(r'^signup/$', views.signup, name='signup'),
]
