from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    director=models.CharField(max_length=100,blank=False,null=False)
    outline = models.TextField(blank=False,null=False)
    movie_url = models.URLField()
    
    def __str__(self):
        return self.title
