from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('', views.PostList, name='home'),
    #path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]