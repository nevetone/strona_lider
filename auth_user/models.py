from django.db import models
from django.utils import timezone

# Create your models here.
class Rangs(models.Model):
    name = models.CharField(max_length=50)
    create_user = models.BooleanField(default=False)
    create_new = models.BooleanField(default=False)
    edit_main = models.BooleanField(default=False)
    adding_images = models.BooleanField(default=False)
    create_gallery = models.BooleanField(default=False)
    create_files = models.BooleanField(default=False)
    create_webs = models.BooleanField(default=False)
    write_messages = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
class Messages(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    sender_nickname = models.CharField(max_length=150)
    sender_email = models.EmailField(max_length=254)
    send_back = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    