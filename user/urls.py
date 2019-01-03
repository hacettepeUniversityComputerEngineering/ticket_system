from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.deneme_profile, name='profile_page'),
]
