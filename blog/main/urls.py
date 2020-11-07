from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('articles', views.articles, name='articles'),
    path('add_article', views.add_article, name='add_article'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/update/<int:pk>', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('add_category', views.CategoryCreateView.as_view(), name='add_category'),
]
