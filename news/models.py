from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True)
    
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
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    has_thumbnail = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField("Category")
    has_own_web = models.BooleanField(default=False)
    web_name = models.CharField(max_length=50, unique=True)
    has_gallery = models.BooleanField(default=False)
    gallery = models.ManyToManyField("Gallery", blank=True)
    
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.web_name})
    
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
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    has_thumbnail = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField("Category")
    has_own_web = models.BooleanField(default=False)
    web_name = models.CharField(max_length=50, blank=True )
    featured = models.BooleanField(default=True)
    has_gallery = models.BooleanField(default=False)
    gallery = models.ManyToManyField("Gallery", blank=True)
    
    
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.web_name})
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    gallery_name = models.CharField(max_length=50)
    pictures = models.ManyToManyField("Pictures", blank=True)
    
    def __str__(self):
        return self.gallery_name
    
class Pictures(models.Model):
    picture_title = models.CharField(max_length=50)
    picture = models.ImageField()
    
    def __str__(self):
        return self.picture_title
    
class Webs(models.Model):
    web_name = models.CharField(max_length=50)
    web_content = HTMLField(null=True, blank=True)
    pictures = models.ManyToManyField("Pictures", blank=True)
    web_filles = models.ManyToManyField("Files", blank=True)
    
    def __str__(self):
        return self.web_name
    
class AllWebs(models.Model):
    picture_title = models.CharField(max_length=50)
    pictures = models.ManyToManyField("Pictures", blank=True)
    
    def __str__(self):
        return self.picture_title
    
class AllFiles(models.Model):
    all_files_name = models.CharField(max_length=50)
    files = models.ManyToManyField("Files", blank=True)
    
    def __str__(self):
        return self.all_files_name
    
class Files(models.Model):
    file_name = models.CharField(max_length=50)
    file = models.FileField()
    
    def __str__(self):
        return self.file_name