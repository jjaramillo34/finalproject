from re import template
from . import views
from django.urls import path

app_name = "contact"
urlpatterns = [
    path('blog/contact/', views.ContactView.as_view(), name='contact'),
    
]