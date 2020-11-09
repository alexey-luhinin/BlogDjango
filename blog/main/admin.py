from django.contrib import admin
from .models import Articles, Category, Comments

admin.site.register(Category)
admin.site.register(Articles)
admin.site.register(Comments)
