
# movscrapy [Movie Sracper]

This application features automated scraping of essential movie information from Rotten Tomatoes, including titles, poster, director, plot, release dates, ratings and reviews. The collected data is securely stored in the app's database, ensuring efficient access and management. On the home page, users can browse a comprehensive list of all the movies with scraped information. Additionally, by selecting a specific movie, users can view detailed information using the movie's unique ID, providing them with all the relevant details gathered from Rotten Tomatoes.


## Features

- Scraping the movie's basic informations from [rottentomatoes](https://www.rottentomatoes.com/)
- Store the scrapped data into our app's database
- Show all scrapped movies list in home page
- See all scrapped informations about the Particular movie using by it's id


## Screenshots

![Home Page](https://raw.githubusercontent.com/iammadhanraj/mystaticfiles/main/movscrapy/home_page.png)

![Scrap Page](https://raw.githubusercontent.com/iammadhanraj/mystaticfiles/main/movscrapy/scrap_page.png)

## Setup

1.Clone this repository

2.Create virtual environment 
```python
  pyhon -m ven env_name
```
3.Install requirements
```python
  pip install -r requirements.txt
```
4.Activate the virtual environment

5.Run this project
```python
  python manage.py runserver
``` 
## References

- Sources for scrap the data from [rottentomatoes](https://www.rottentomatoes.com/)
