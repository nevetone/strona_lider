from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField
import os
from django.utils import timezone

    
User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True)
    rank = models.ForeignKey("auth_user.Rangs", on_delete=models.SET_NULL, null=True)
    cat_color = models.TextField(default="#007bff")
    cat_text_color = models.TextField(default="#FFFFFF")
    
    def __str__(self):
        return str(self.user)
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=400)
    content = HTMLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    has_thumbnail = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField("Category")
    has_own_web = models.BooleanField(default=False)
    web_name = models.CharField(max_length=50, unique=True)
    has_gallery = models.BooleanField(default=False)
    gallery = models.ForeignKey("Gallery", on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.web_name})
    
    def get_absolute_gallery_url(self):
        return reverse("galeria_one", kwargs={"slug": self.gallery.gallery_name})
    
    def get_update_url(self):
        return reverse("post-update", kwargs={"slug": self.web_name})
    
    def get_delete_url(self):
        return reverse("post-delete", kwargs={"slug": self.web_name})
    
    def __str__(self):
        return self.title
    

    
class MainNews(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    content = HTMLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    has_thumbnail = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField("Category")
    has_own_web = models.BooleanField(default=False)
    web_name = models.CharField(max_length=50, blank=True )
    featured = models.BooleanField(default=False, null=True, blank=True)
    has_gallery = models.BooleanField(default=False)
    gallery = models.ForeignKey("Gallery", on_delete=models.SET_NULL, null=True, blank=True)

    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.web_name})
    
    def get_absolute_gallery_url(self):
        return reverse("galeria_one", kwargs={"slug": self.gallery.gallery_name})
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    gallery_name = models.CharField(max_length=50, unique=True)
    pictures = models.ManyToManyField("Pictures")
    category = models.ManyToManyField("Category", blank=True)
    overview = models.CharField(max_length=1000, default="Nie posiada opisu")
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    
    def get_absolute_url(self):
        return reverse("galeria_one", kwargs={"slug": self.gallery_name})
    
    def get_update_url(self):
        return reverse("galeria-update", kwargs={"slug": self.gallery_name})
    
    def get_delete_url(self):
        return reverse("galeria-delete", kwargs={"slug": self.gallery_name})
    
    def __str__(self):
        return self.gallery_name
    
class Pictures(models.Model):
    picture_title = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    has_gallery = models.BooleanField(default=False)
    to_gallery = models.BooleanField(default=False)
    
    def get_delete_url(self):
        return reverse("image_delete", kwargs={"slug": str(self.picture)})
    
    def __str__(self):
        return self.picture_title
    
class Webs(models.Model):
    web_name = models.CharField(max_length=50, unique=True)
    web_content = HTMLField()
    pictures = models.ManyToManyField("Pictures", blank=True)
    web_filles = models.ManyToManyField("Files", blank=True)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    
    def get_absolute_url(self):
        return reverse("webs", kwargs={"slug": self.web_name})
    
    def get_update_url(self):
        return reverse("web_edit", kwargs={"slug": self.web_name})
    
    def get_delete_url(self):
        return reverse("web_delete", kwargs={"slug": self.web_name})
    
    def __str__(self):
        return self.web_name
    
class WebCategory(models.Model):
    web_cat_name = models.CharField(max_length=25, unique=True)
    webs = models.ManyToManyField("Webs")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    
    def get_absolute_url(self):
        return reverse("webs_cat", kwargs={"slug": self.web_cat_name})
    
    def get_update_url(self):
        return reverse("webs_cat_edit", kwargs={"slug": self.web_cat_name})
    
    def get_delete_url(self):
        return reverse("webs_cat_delete", kwargs={"slug": self.web_cat_name})
    
    def __str__(self):
        return self.web_cat_name
    
class Files(models.Model):
    file_name = models.CharField(max_length=50)
    file = models.FileField()
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    
    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext
    
    
    def get_delete_url(self):
        return reverse("file_delete", kwargs={"slug": str(self.file)})

    
    def __str__(self):
        return self.file_name
    