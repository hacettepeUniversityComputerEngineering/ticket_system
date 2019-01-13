from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'profile', views.deneme_profile, name='profile_page'),
    url(r'update', views.edit_profile, name='user_update'),
]
