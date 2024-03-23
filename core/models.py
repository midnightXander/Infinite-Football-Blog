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
    #it was posts_images without the /
    cover_image = models.ImageField(upload_to='posts_images/')
    bodyImage = models.ImageField(upload_to='posts_images/',blank=True) 
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:85]+"..."

class Match(models.Model):
    """structure of a match"""
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    team1Logo = models.ImageField(upload_to='team_logos/')
    team2Logo = models.ImageField(upload_to='team_logos/')
    competition = models.CharField(max_length=40)
    matchday = models.CharField(max_length=30)
    match_link = models.TextField(blank=True)
    alt_link1 = models.TextField(blank=True, default="")
    alt_link2 = models.TextField(blank=True,default="")
    class Meta:
        verbose_name_plural = 'Matches'
    def __str__(self):
        return self.team1[:5] + " vs " + self.team2[:5]


