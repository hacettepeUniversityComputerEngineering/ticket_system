from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    # path('event_details', views.event_details, name='event_page'),
    url(r'event_details/(?P<pk>\d+)/$', views.event_details, name='event_details'),
    path('', views.call_home, name='home_page'),

    url(r'^signup/$', views.signup, name='signup'),
]
