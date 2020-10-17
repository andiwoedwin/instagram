from django.shortcuts import render
from .models import Post


def welcome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/home.html', context)

def about(request):
    return render(request, 'insta/about.html',{'title':'About'})



