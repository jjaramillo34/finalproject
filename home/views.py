from django.shortcuts import render
from django.db.models import Q

from blog.models import Post
from course.models import Course
from user.models import Avatar


def index(request):
    header = "Clean Blog"
    subheader = "A Blog Theme by Start Bootstrap"
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx, 'header': header, 'subheader': subheader }
    #courses = Course.objects.all()
    blogs = Post.objects.all()
    context_dict.update({
        'blogs': blogs,
        
    })
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/home.html"
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        courses = Course.objects.filter(query)
        context_dict.update({
            'courses': courses,
            'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="home/home.html",
    )
