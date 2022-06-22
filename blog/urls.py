from . import views
from django.urls import path
#from django.conf.urls import url

app_name = "blog"
urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('', views.PostList, name='home'),
    #path("search/", views.SearchResultsView.as_view(), name="search_results"),
    #path("search/", views.post_search, name="search_results"),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    #path('postautocomplete/', views.PostAutocomplete.as_view(), name='postautocomplete'), 
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    #path('blog/create/', views.PostCreateView.as_view(), name='post_create'),
    # blog 
    path('user/profile/myblogs/', views.user_posts, name='user_blogs'),
    path('user/profile/myblogs/create/', views.PostCreateView.as_view(), name="blog_create"),
    path('user/profile/myblogs/view/<int:pk>', views.PostDetailView.as_view(), name="blog_view"),
    #path('user/profile/myblogs/view/', views.user_post_remove, name="blog_view"),
    path('user/profile/myblogs/delete/<int:pk>/', views.user_post_remove, name="blog_delete"),
    #path('user/profile/management/user_list/<int:page>', views.user_management, name="users_management"),
    path('user/profile/management/user_list/', views.user_management, name="users_management"),
    #path('', views.autocomplete, name='autocomplete'),
]