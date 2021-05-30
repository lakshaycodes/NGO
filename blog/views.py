from django.shortcuts import render
from .models import post

# Create your views here.
def bloghome(request):
    posts = post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def viewblog(request, slug):
    posts = post.objects.get(slug=slug)
    return render(request, 'blog/blog.html', {'posts': posts})
