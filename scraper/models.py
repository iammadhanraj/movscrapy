from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    poster=models.URLField()
    director=models.CharField(max_length=100,blank=False,null=False)
    outline = models.TextField(blank=False,null=False)
    language=models.CharField(max_length=52,null=False,blank=False)
    released_on=models.CharField(max_length=100,blank=False,null=False)
    genre=models.ManyToManyField(Genre,blank=True,null=True)
    criticsscore=models.IntegerField(null=True,blank=True)
    criticsreviews=models.IntegerField(null=True,blank=True)
    audiencescore=models.IntegerField(null=True,blank=True)
    audiencereviews=models.IntegerField(null=True,blank=True)
    movie_url = models.URLField()
    
    def __str__(self):
        return self.title
