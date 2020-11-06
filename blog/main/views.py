from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Articles
from .forms import ArticlesForm


class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'article'

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

def add_article(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticlesForm()

    return render(request, 'main/add_article.html', {'form':form})
    
