from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=400)
    timestamp = models.DateField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField("Category")
    has_own_web = models.BooleanField(default=False)
    content = HTMLField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.id})
    
    
    def __str__(self):
        return self.title
    
class MainNews(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField("Category")
    has_own_web = models.BooleanField(default=False)
    featured = models.BooleanField(default=True)
    content = HTMLField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.id})
    
    def __str__(self):
        return self.title
    
    