from MovieView import MovieView
from MovieController import MovieController
from TmdbService import TmdbService  # Zakładam, że masz tę klasę zdefiniowaną
from OmdbService import OmdbService

def main():
    omdb_service = OmdbService()
    tmdb_service = TmdbService()
    view = MovieView()

    controller = MovieController(omdb_service, tmdb_service, view)
    controller.run()


if __name__ == "__main__":
    main()
