from . import views
from django.urls import path

app_name = "contact"
urlpatterns = [
    #path('', views.contact_view, name='contact'),
    path('', views.ContactFormView.as_view(), name='contact'),
    
]