from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Swathi P',
        'title': 'Learning html',
        'content': 'First project conteent',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Swathi P',
        'title': 'Learning html',
        'content': 'First project conteent',
        'date_posted': 'August 27, 2018'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')