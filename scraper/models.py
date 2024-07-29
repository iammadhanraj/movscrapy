from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    director=models.CharField(max_length=100,blank=False,null=False)
    outline = models.TextField(blank=False,null=False)
    language=models.CharField(max_length=52,null=True,blank=True)
    released_on=models.CharField(max_length=100,blank=True,null=True)
    runtime=models.CharField(max_length=24,blank=True,null=True)
    genre=models.ManyToManyField(Genre,blank=True,null=True)
    movie_url = models.URLField()
    
    def __str__(self):
        return self.title
