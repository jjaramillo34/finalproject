from re import template
from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('', views.PostList, name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/create/', views.PostCreateView.as_view(), name='post_create'),
    
]