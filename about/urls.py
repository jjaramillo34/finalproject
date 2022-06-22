from re import template
from . import views
from django.urls import path

app_name = "about"
urlpatterns = [
    path('blog/about/', views.AboutView.as_view(), name='about'),
    
]