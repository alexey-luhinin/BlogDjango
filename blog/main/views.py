from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Articles, Category
from .forms import ArticlesForm, CategoryForm


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm

    template_name = 'main/add_category.html'

    success_url = reverse_lazy('add_article')


class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    model = Articles
    form_class = ArticlesForm

    template_name = 'main/article_update.html'

    success_url = reverse_lazy('articles')


class ArticleDeleteView(DeleteView):
    model = Articles

    template_name = 'main/article_delete.html'

    success_url = reverse_lazy('articles')


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
            return redirect('articles')
    else:
        form = ArticlesForm()

    return render(request, 'main/add_article.html', {'form':form})
    
