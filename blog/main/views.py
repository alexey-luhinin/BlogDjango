from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import login, authenticate

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Articles, Category, Comments
from .forms import ArticlesForm, CategoryForm, CommentsForm, Registration


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm

    template_name = 'main/add_category.html'

    success_url = reverse_lazy('add_article')


class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comments.objects.filter(
            article=self.object).order_by('-date').all()
        form = CommentsForm(initial={
            'article': self.object,
            'author': self.request.user
        })

        context['form'] = form
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CommentsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path_info)


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
    comments = Comments.objects.all()
    articles = {'articles': article,
                'comments': comments,
                }
    return render(request, 'main/articles.html', articles)


@staff_member_required
def add_article(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticlesForm()

    return render(request, 'main/add_article.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = Registration()
        
    return render(request, 'main/registration.html', {'form': form})

