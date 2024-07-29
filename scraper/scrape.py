import requests
from bs4 import BeautifulSoup
from .models import Movie

def scrape_and_save_movie(movie_url):
    try:
        # response = requests.get("https://www.rottentomatoes.com/m/alita_battle_angel")
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.text,'html.parser')
        movie_title=soup.find('h1',class_='unset').find('span')
        movie_outline=soup.find('div',class_='synopsis-wrap').find_all('rt-text')[1]
        movie_director=soup.find('section',class_='media-info').find('div',class_='content-wrap').find('dl').find_all('div',class_='category-wrap')[0].find('rt-link')
        

        movie_genre=(soup.find('section',class_='media-info').find('div',class_='content-wrap').find('dl').find_all('div',class_='category-wrap')[6]).find('dd')
        movie_language=(soup.find('section',class_='media-info').find('div',class_='content-wrap').find('dl').find_all('div',class_='category-wrap')[7]).find('dd').find('rt-text')
        movie_released=(soup.find('section',class_='media-info').find('div',class_='content-wrap').find('dl').find_all('div',class_='category-wrap')[8]).find('dd').find('rt-text')
        movie_released_date=(movie_released.text).split(',')[0]+(movie_released.text).split(',')[1]
        movie_runtime=(soup.find('section',class_='media-info').find('div',class_='content-wrap').find('dl').find_all('div',class_='category-wrap')[10]).find('dd').find('rt-text')

        genre_list=[]
        mg=movie_genre.find_all('rt-link')
        for i in mg:
            genre_list.append(i.text)

        movie = Movie.objects.create(
        title=movie_title.text,
        director=movie_director.text,
        outline=movie_outline.text,
        language=movie_language.text,
        released_on=movie_released_date,
        runtime=movie_runtime.text,
        movie_url=movie_url,
        )
        return movie

    except Exception as e:
        return e