import requests
import json
from Movie import Movie

class TmdbService:
    def __init__(self):
        pass

    def parse_movie(self, json_data):
        # Sprawdzanie, czy są wyniki
        if 'results' in json_data:
            movie_data = json_data['results'][0]  # Weź pierwszy wynik
            title = movie_data.get("title")
            director = movie_data.get("director", "N/A")  # Jeśli brak, użyj "N/A"
            release_date = movie_data.get("release_date", "N/A")
            rating = movie_data.get("vote_average", "N/A")
            overview = movie_data.get("overview", "N/A")

            # Tworzenie obiektu Movie
            return Movie(title, director, release_date, rating, overview)
        else:
            print("Brak wyników dla podanego tytułu.")
            return None

    def fetchMovieDetails(self, title):
        base_url = "https://api.themoviedb.org/3/search/movie"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzEwMzY4MmY0ZWQ0NTI3Y2QzYjYzZDM1NTcyZmU3MiIsIm5iZiI6MTczMDIwMzg1Ni41NzMwMDMsInN1YiI6IjYyOWY4ODY3ZDIxNDdjMTE3ZTYzZTNlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2uMrsVqkiYb7BFd_yCBX4TQ2xdEG8IiTrkkOw-2U5QM"
        }
        # Dodanie tytułu jako parametru zapytania
        params = {
            "query": title
        }
        r = requests.get(base_url, headers=headers, params=params)
        if r.status_code == 200:
            json_data = r.json()
            return self.parse_movie(json_data)
        else:
            print("Film nie został znaleziony\n")
            return None
        
    def fetchNowPlayingMovies(self):
        base_url = "https://api.themoviedb.org/3/movie/now_playing"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzEwMzY4MmY0ZWQ0NTI3Y2QzYjYzZDM1NTcyZmU3MiIsIm5iZiI6MTczMDIwMzg1Ni41NzMwMDMsInN1YiI6IjYyOWY4ODY3ZDIxNDdjMTE3ZTYzZTNlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2uMrsVqkiYb7BFd_yCBX4TQ2xdEG8IiTrkkOw-2U5QM"
        }
        r = requests.get(base_url, headers=headers)
        movies = []
        if(r.status_code == 200):
            search_data = r.json()
            results = search_data.get('results', [])
            for result in results:
                title = result.get("title")
                director = result.get("director")
                releaseDate = result.get("release_date")
                rating = result.get("vote_average")
                overview = result.get("overview")

                movie = Movie(title,director,releaseDate,rating,overview)
                movies.append(movie)
        else:
            print("Błąd pobierania danych: " + r.getStatus())
        return movies
    
    def fetchTopRatedMovies(self):
        base_url ="https://api.themoviedb.org/3/movie/top_rated"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzEwMzY4MmY0ZWQ0NTI3Y2QzYjYzZDM1NTcyZmU3MiIsIm5iZiI6MTczMDIwMzg1Ni41NzMwMDMsInN1YiI6IjYyOWY4ODY3ZDIxNDdjMTE3ZTYzZTNlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2uMrsVqkiYb7BFd_yCBX4TQ2xdEG8IiTrkkOw-2U5QM"
        }
        r = requests.get(base_url, headers=headers)

        movies = []
        if(r.status_code == 200):
            search_data = r.json()
            results = search_data.get('results', [])
            for result in results:
                title = result.get("title")
                director = result.get("director")
                releaseDate = result.get("release_date")
                rating = result.get("vote_average")
                overview = result.get("overview")

                movie = Movie(title,director,releaseDate,rating,overview)
                movies.append(movie)
        else:
            print("Błąd pobierania danych: " + r.getStatus())
        return movies
