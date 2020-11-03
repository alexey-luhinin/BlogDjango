from django.forms import ModelForm, TextInput, Textarea, Select, FileInput
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['category', 'title', 'description', 'text', 'image',]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
                'rows': 8,
            }),

            'category': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),

            'image': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            })
        }
