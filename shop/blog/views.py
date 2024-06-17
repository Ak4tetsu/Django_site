from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from blog.models import Post

def index(request):
    latest_posts_list = Post.objects.order_by('-poblish')[:5]
    # output = ',\n'.join([p.slug for p in latest_posts_list])
    template = loader.get_template('index.html')
    context = {
        'latest_posts_list':latest_posts_list,
    }

    return HttpResponse(template.render(context,request))

def detail(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    template = loader.get_template('ditail.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context,request))