from django.urls import path
from .views import movie_list, scrape_movie

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('scrape/', scrape_movie, name='scrape_movie'),
]
