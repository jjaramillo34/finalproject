from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.forms import CommentForm
from blog.models import Post

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