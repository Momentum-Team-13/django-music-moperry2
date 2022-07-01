from turtle import title
from django.db import models
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    songs = models.TextField(max_length=500)

class Artist(models.Model): 
    name = models.CharField(max_length=255)
    album = models.ManyToManyField(Album)



    def __str__(self):
        return self.title
