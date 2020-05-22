from django.db import models

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

    def __str__(self):
        return self.name
    
    

    