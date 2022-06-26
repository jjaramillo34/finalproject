from re import template
from . import views
from django.urls import path

app_name = "contact"
urlpatterns = [
    path('', views.contact, name='contact'),
    
]