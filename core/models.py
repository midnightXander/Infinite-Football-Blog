from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Category(models.Model):
    """ """
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name    

class BlogPost(models.Model):
    """A typical blog post"""
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    text = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='posts_images')
    bodyImage = models.ImageField(upload_to='posts_images',blank=True) 
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]+"..."


