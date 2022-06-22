from ast import arg
from black import format_cell
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse

from django.views.generic import FormView, TemplateView
#from comment.forms import CommentForm, CrispyCommentForm
from comment.forms import CommentForm
from blog.models import Post
from comment.models import Comment


# Create your views here.
    
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
        'header': 'Clean Blog', 
        'subheader': 'A Blog Theme by Start Bootstrap'}
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
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    
    def get_success_url(self) -> str:
        return reverse('blog:post_create', args=[self.object.pk])