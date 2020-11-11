from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, \
HiddenInput, PasswordInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Articles
from .models import Category
from .models import Comments


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]
            
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'registration__input'
        self.fields['password1'].widget.attrs['class'] = 'registration__input'
        self.fields['password2'].widget.attrs['class'] = 'registration__input'


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
