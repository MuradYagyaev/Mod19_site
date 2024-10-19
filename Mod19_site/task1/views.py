from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

range_list = [str(x) for x in range(3, 11)]


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    perpage = request.GET.get('per_page')
    if perpage is None:
        perpage = 5
    page_number = request.GET.get('page')
    paginator = Paginator(posts, per_page=perpage)
    page_posts = paginator.get_page(page_number)
    info = {
        'page_posts': page_posts,
        'per_page': perpage,
        'range_list': range_list,
    }
    return render(request, 'post_list.html', info)
