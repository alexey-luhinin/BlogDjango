from django.forms import ModelForm, TextInput, Textarea, Select, FileInput
from .models import Articles


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
