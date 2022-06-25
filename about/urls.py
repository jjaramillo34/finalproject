from re import template
from . import views
from django.urls import path

app_name = "about"
urlpatterns = [
    path('<int:pk>', views.AboutViewDetail.as_view(), name='about'),
    path('', views.about, name='about')    
]