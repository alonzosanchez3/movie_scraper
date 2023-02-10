from bs4 import BeautifulSoup
import requests

MOVIE_URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url=MOVIE_URL)
soup = BeautifulSoup(response.text, 'html.parser')
