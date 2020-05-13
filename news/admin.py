from django.contrib import admin
from .models import News, Author, Category, MainNews
# Register your models here.

admin.site.register(News)
admin.site.register(Author)
admin.site.register(MainNews)
admin.site.register(Category)