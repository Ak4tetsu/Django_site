from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.http import HttpResponse
# from django.template import loader
# Create your views here.
from blog.models import Post
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe

@require_http_methods(['GET','POST'])
def index(request):
    latest_posts_list = Post.objects.order_by('-poblish')[:5]
    # output = ',\n'.join([p.slug for p in latest_posts_list])
    # template = loader.get_template('index.html')
    context = {
        'latest_posts_list':latest_posts_list,
    }

    # return HttpResponse(template.render(context,request))
    return render(request, 'index.html', context)

@require_GET
def detail(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    # template = loader.get_template('ditail.html')
    context = {
        'post': post,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'ditail.html', context)

@require_safe
def archive_year(request, year):

    # year_filter_posts = Post.objects.filter(poblish__year = year)
    year_filter_posts = get_list_or_404(Post, poblish__year = year)

    context = {
        'year_filter_posts' : year_filter_posts,
    }

    return render(request, 'archive.html', context)