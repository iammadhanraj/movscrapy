from django.shortcuts import render, redirect
from .scrape import scrape_and_save_movie
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'scraper/movie_list.html', {'movies': movies})

def scrape_movie(request):
    if request.method == 'POST':
        movie_url = request.POST.get('movie_url')
        scrape_and_save_movie(movie_url)
        return redirect('movie_list')
    return render(request, 'scraper/scrape_movie.html')
