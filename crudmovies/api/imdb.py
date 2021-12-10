import json
import requests

class IMDB():
    def __init__(self, raw):
        self.title = raw['title']
        self.imdbID = raw['id']
        self.year = raw['year']
        self.main_photo = raw['poster']
        self.runtime = raw['length']
        self.description = raw['plot']
        self.imdb_rating = raw['rating']
        

def searchMovie(key):
    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{key}"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bfca3f66f0mshd875810935566e0p1b73f8jsncdf6f12b92a2"
        }

    response = requests.request("GET", url, headers=headers)
    json_response = json.loads(response.text)
    return IMDB(json_response)