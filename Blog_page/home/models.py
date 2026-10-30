from django.db import models

from autoslug import AutoSlugField

# Create your models here.
class Catagory(models.Model):
    name= models.CharField(max_length=100)
    slug= AutoSlugField(populate_from= "name", unique = True, null=True, default=None)
    
    def __str__(self):
        return self.name



class Blog (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    content = models.TextField()
    
    def __str__(self):
        return self.title
    