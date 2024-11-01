import requests
from typing import List, Optional
from Movie import Movie

class OmdbService:
    API_KEY = "85fcb8bf"
    BASE_URL = f"http://www.omdbapi.com/?apikey={API_KEY}"

    def fetchMovieDetails(self, title: str) -> Optional['Movie']:
        response = requests.get(self.BASE_URL, params={"t": title})

        if response.status_code == 200:
            json_data = response.json()
            return self.parse_movie(json_data)
        else:
            print("Film nie został znaleziony")
            return None

    def fetch_now_playing_movies(self) -> List['Movie']:
        # Zwróć pustą listę, bo ta funkcjonalność nie jest obsługiwana przez OMDb
        return []

    def parse_movie(self, json_data: dict) -> 'Movie':
        title = json_data.get("Title", "N/A")
        director = json_data.get("Director", "N/A")
        year = json_data.get("Year", "N/A")
        rating = json_data.get("imdbRating", "N/A")

        return Movie(title, director, year, rating, "Opis niedostępny")

# Klasa Movie powinna być zdefiniowana gdzie indziej w kodzie
