from bs4 import BeautifulSoup
import requests

MOVIE_URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url=MOVIE_URL)
soup = BeautifulSoup(response.text, 'html.parser')
h3_class = 'listicleItem_listicle-item__title__hW_Kn'
movie_titles = soup.find_all(name='h3', class_=h3_class)
movie_titles = [movie.getText() for movie in movie_titles]
movie_titles = movie_titles[::-1]
print(movie_titles)

with open('movies.txt', 'w') as file:
  for movie in movie_titles:
    file.write(f"{movie}\n")
#
