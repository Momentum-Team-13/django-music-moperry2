from turtle import title
from django.db import models
from django.utils import timezone

# Create your models here.
# class Artist(models.Model): 
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

class Album(models.Model):
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    songs = models.TextField(max_length=500)

    def __str__(self):
        return self.title


