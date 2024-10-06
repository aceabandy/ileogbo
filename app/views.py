from django.shortcuts import render
from .models import Blog
from django.shortcuts import render,HttpResponse ,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
     # Retrieve the latest blog posts
    posts = Blog.objects.all()[:2]  # Assuming you want to display the latest 2 posts

    context = {
        'posts': posts  # Pass the posts queryset to the template
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})


def blog(request):
    # Retrieve all posts
    posts = Blog.objects.order_by('-published_date')

    # Set the number of posts per page
    posts_per_page = 9

    # Paginate the posts
    paginator = Paginator(posts, posts_per_page)

    # Get the current page number from the URL parameters
    page_number = request.GET.get('page')

    try:
        # Get the posts for the requested page
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': paginated_posts})