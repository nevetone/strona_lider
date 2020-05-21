from django.db import models

# Create your models here.
class Rangs(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField("Permissions")
    
    def __str__(self):
        return self.name
    
    
class Permissions(models.Model):
    create_user = models.BooleanField(default=False)
    cat = models.ManyToManyField("news.Category")
    create_new = models.BooleanField(default=False)
    edit_main = models.BooleanField(default=False)
    adding_images = models.BooleanField(default=False)
    create_gallery = models.BooleanField(default=False)
    create_files = models.BooleanField(default=False)
    create_webs = models.BooleanField(default=False)
    