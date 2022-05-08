from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostDetailView(DetailView):
    model=Post