from MovieController import MovieController
from MovieView import MovieView
from TmdbService import TmdbService
from OmdbService import OmdbService

def main():
    omdb_service = OmdbService()
    tmdb_service = TmdbService()
    view = MovieView()

    controller = MovieController(omdb_service, tmdb_service, view)
    controller.run()
if __name__ == "__main__":
    main()
