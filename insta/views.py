from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post


def welcome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'insta/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'insta/about.html',{'title':'About'})



