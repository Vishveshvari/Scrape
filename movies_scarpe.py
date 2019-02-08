

from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#We are going to scrape Movies title, cast and ratings according to their ranking which is available on the website

movies = soup.select('td.titleColumn')
cast = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]

for i in range(0, len(movies)):
    movie_string = movies[i].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(i)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    rank = movie[:len(str(i)) - (len(movie))]
    print("Rank: "+rank +" Movie Name-> "+ movie_title +" Year: "+year+" Cast: "+cast[i]+" Rating: " +ratings[i])




#output
#>python movies_scrape.py
#Rank: 1 Movie Name-> The Shawshank Redemption Year: 1994 Cast: Frank Darabont (dir.), Tim Robbins, Morgan Freeman Rating: 9.216905286794802
#Rank: 2 Movie Name-> The Godfather Year: 1972 Cast: Francis Ford Coppola (dir.), Marlon Brando, Al Pacino Rating: 9.155777408268719
#Rank: 3 Movie Name-> The Godfather: Part II Year: 1974 Cast: Francis Ford Coppola (dir.), Al Pacino, Robert De Niro Rating: 8.990428065971162
