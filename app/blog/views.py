from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from django.views.generic import FormView, TemplateView
from requests import request
from comment.forms import CommentForm
from blog.models import Post
from comment.models import Comment
from user.models import Profile

# Create your views here.
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context['post_list'] = Post.objects.filter(Q(title__icontains=query))
        context['post_count'] = Post.objects.filter(Q(title__icontains=query)).count()
        print(type(context['post_count']))
        print(context)
        return context
    
def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    
    print(object_list)
    
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    context_dict = {
        'page': page, 
        'post_list': post_list, 
        'header': 'J&J Blog Site', 
        'subheader': 'Coder House Rocks.'}
    return render(request=request,
                template_name='home/home.html',
                context=context_dict
                )
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    print(model)
        
def post_detail(request, slug):
    template_name = 'blog/post.html'
    form_class = CommentForm
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm()
    
    
    context_dict = {'post': post,
                    'comments': comments,
                    'new_comment': new_comment,
                    'comment_form': comment_form}

    print(context_dict)

    return render(request=request, 
                  template_name=template_name, 
                  context=context_dict,
                  )
    
#class PostCreateView(CreateView):
#    model = Post
#    fields = ['title', 'author', 'body']
#    
#    def get_success_url(self) -> str:
#        return reverse('blog:post_create', args=[self.object.pk])

#def autocomplete(request):
#    if 'term' in request.GET:
#        qs = Post.objects.filter(title__icontains=request.GET.get('term'))
#        titles = list()
#        for product in qs:
#            titles.append(product.title)
#        # titles = [product.title for product in qs]
#        return JsonResponse(titles, safe=False)
#    return render(request, 'home/home.html')


@login_required
def user_posts(request):
    if request.user.is_authenticated and request.user.is_superuser:
        context = {}
        user = get_object_or_404(User, username=request.user.username)
        current_user = request.user.id
        print(user)
        print('Current User:', current_user)
        profile = get_object_or_404(Profile, user=1)
        #user_posts = get_object_or_404(Post, id=1)
        user_posts = Post.objects.all()
        print(user_posts)
        context = {'post_list': user_posts, 'user': user, 'header': 'CRUD Blogs', 'subheader': 'Create, Read, Update and Delete'}
        return render(request=request, 
                    template_name='blog/user_blogs.html', 
                    context=context)
        
    elif request.user.is_authenticated:
        context = {}
        user = get_object_or_404(User, username=request.user.username)
        current_user = request.user.id
        print(user)
        print('Current User:', current_user)
        profile = get_object_or_404(Profile, user=1)
        #user_posts = get_object_or_404(Post, id=1)
        user_posts = Post.objects.filter(author=request.user)
        print(user_posts)
        context = {'post_list': user_posts, 'user': user}
        return render(request=request, 
                    template_name='blog/user_blogs.html', 
                    context=context)
    
@login_required        
def user_post_remove(request, pk):
    if request.user.is_authenticated:
        try:
            obj_to_be_deleted = Post.objects.get(pk=pk)
            obj_to_be_deleted.delete()
            return redirect('blog:user_blogs')
        except:
            errors = "An error has occured while deleting a Post"
            return render(request, 'home/errors/errors.html', {'errors': errors})
        
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'cover', 'status','body']
    success_url = reverse_lazy('blog:user_blogs')
    template_name = 'blog/post_form.html'
    success_message = "Post was create successfully"
    prepopulated_fields = {'slug':('title')}
    
    def get_context_data(self, **kwargs):
        kwargs['latest_posts_list'] = Post.objects.order_by('-id')
        return super(PostCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        #self.object = form.save(commit=False)
        ##self.object.slug = self.object.title
        #self.object.slug = self.request.user.username
        #self.object.save()
        return super().form_valid(form)
    
    #def get_initial(self):
    #    return self.request.GET
    
class PostEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'cover', 'status','body']
    success_url = reverse_lazy('blog:user_blogs')
    template_name = 'blog/post_form.html'
    success_message = "Post was edit successfully"
    prepopulated_fields = {'slug':('title')}
    
    def get_context_data(self, **kwargs):
        kwargs['latest_posts_list'] = Post.objects.order_by('-id')
        return super(PostEditView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required    
def user_management(request):
    if not request.user.is_superuser:
        return render(request, 'home/errors/403.html', {})
        #raise PermissionDenied
    else:
        page = None
        context = {}
        users = User.objects.values()
        template_name = 'blog/user_management.html'
        paginator = Paginator(users, per_page=2)
        page_object = paginator.get_page(page)
        print(page_object)
        context = {
            'header': 'User Management', 
            'subheader': 'Some other title', 
            'users': users,
            'page_obj': page_object,
            }
        return render(request=request, 
                        template_name=template_name, 
                        context=context)

def custom_error_403(request, exception):
    return render(request, 'home/errors/404.html', {})
