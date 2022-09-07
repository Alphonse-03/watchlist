from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    viewed=models.BooleanField(default=True)
    rating=models.IntegerField(null=True, blank=True)
    urls=models.URLField(null=True, blank=True)
    director=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name


class StreamPlatform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.CharField(max_length=100)

    def __str__(self):
        return self.name