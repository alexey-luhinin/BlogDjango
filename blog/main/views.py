from django.shortcuts import render
from .models import Articles


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def articles(request):
    article = Articles.objects.all()
    articles = {'articles' : article,}
    return render(request, 'main/articles.html', articles)
