from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, \
HiddenInput

from .models import Articles
from .models import Category
from .models import Comments


class CommentsForm(ModelForm):
    class Meta: 
        model = Comments
        fields = ['article', 'author', 'text']

        widgets = {
            'article' : HiddenInput(),
            'author' : HiddenInput(),

            'text': Textarea(attrs={
                'class': 'add-comments__text',
                'rows': 8,
            }),
        }


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['category', 'title', 'description', 'text', 'image',]

        widgets = {
            'title': TextInput(attrs={
                'class': 'add-form__title',
            }),
            'description': TextInput(attrs={
                'class': 'add-form__description',
            }),
            'text': Textarea(attrs={
                'class': 'add-form__text',
                'rows': 8,
            }),

            'category': Select(attrs={
                'class': 'add-form__category',
            }),

            'image': FileInput(attrs={
                'class': 'add-form__image',
            }),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'add-form__title',
            }),
        }
