from . import views
from django.urls import path

app_name = "contact"
urlpatterns = [
    path('', views.contact_view, name='contact'),
    
]