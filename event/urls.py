from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

    # path('event_details', views.event_details, name='event_page'),
    url(r'event_details/(?P<pk>\d+)/$', views.event_details, name='event_details'),
    path('', views.call_home, name='home_page'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    path('buy_ticket', views.buy_ticket, name='buy_ticket'),
    path('payment_screen', views.payment, name='payment_screen'),
    path('new_event', views.new_event, name='new_event')

]
