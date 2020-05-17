from django.contrib import admin
from .models import News, Author, Category, MainNews, Files, AllFiles, AllWebs, Webs, Pictures, Gallery
# Register your models here.

admin.site.register(News)
admin.site.register(Author)
admin.site.register(MainNews)
admin.site.register(Category)
admin.site.register(Pictures)
admin.site.register(Gallery)
admin.site.register(Files)
admin.site.register(AllFiles)
admin.site.register(Webs)
admin.site.register(AllWebs)