from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('list_of_cars', views.list_of_cars, name='cars'),
    path('conditions', views.conditions, name='cond'),
    path('service', views.service, name='services'),
    path('contacts', views.contacts, name='contact')
]
