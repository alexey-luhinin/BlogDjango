from django.contrib import admin
from .models import Articles, Category

admin.site.register(Category)
admin.site.register(Articles)
