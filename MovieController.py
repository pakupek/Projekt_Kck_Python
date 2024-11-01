class MovieController:
    def __init__(self, omdb_service, tmdb_service, view):
        self.omdb_service = omdb_service
        self.tmdb_service = tmdb_service
        self.view = view
        self.favorite_movies = []  # Lista ulubionych filmów

    def run(self):
        continue_running = True

        while continue_running:
            choice = self.view.display_main_menu()

            if choice == 1:
                self.omdb_menu()
            elif choice == 2:
                self.tmdb_menu()
            elif choice == 3:
                continue_running = False
            else:
                self.view.display_message("Nieprawidłowy wybór.")

        self.view.display_message("Dziękujemy za korzystanie z aplikacji!")

    def omdb_menu(self):
        exit_omdb = False
        while not exit_omdb:
            choice = self.view.display_sub_menu("OMDb")

            if choice == 1:
                self.search_movie(self.omdb_service)
            elif choice == 2:
                self.view.display_favorite_movies(self.favorite_movies)
            elif choice == 3:
                self.add_to_favorites(self.omdb_service)
            elif choice == 4:
                exit_omdb = True
            else:
                self.view.display_message("Nieprawidłowy wybór.")

    def tmdb_menu(self):
        exit_tmdb = False
        while not exit_tmdb:
            choice = self.view.display_sub_menu("TMDb")

            if choice == 1:
                self.search_movie(self.tmdb_service)
            elif choice == 2:
                self.display_now_playing()
            elif choice == 3:
                self.display_top_rated()
            elif choice == 4:
                self.view.display_favorite_movies(self.favorite_movies)
            elif choice == 5:
                self.add_to_favorites(self.tmdb_service)
            elif choice == 6:
                exit_tmdb = True
            else:
                self.view.display_message("Nieprawidłowy wybór.")

    def search_movie(self, service):
        title = self.view.get_movie_title()
        movie = service.fetchMovieDetails(title)
        if movie is not None:
            self.view.display_movie_details(movie)
        else:
            self.view.display_message("Film nie został znaleziony.")

    def display_now_playing(self):
        now_playing_movies = self.tmdb_service.fetchNowPlayingMovies()
        if not now_playing_movies:
            self.view.display_message("Brak informacji o obecnie granych filmach.")
        else:
            for movie in now_playing_movies:
                self.view.display_movie_details(movie)

    def display_top_rated(self):
        top_rated_movies = self.tmdb_service.fetchTopRatedMovies()
        if not top_rated_movies:
            self.view.display_message("Brak najlepiej ocenianych filmów.")
        else:
            for movie in top_rated_movies:
                self.view.display_movie_details(movie)

    def add_to_favorites(self, service):
        title = self.view.get_movie_title()
        movie = service.fetchMovieDetails(title)
        if movie is not None:
            self.favorite_movies.append(movie)
            self.view.display_message("Film dodany do ulubionych.")
        else:
            self.view.display_message("Film nie został znaleziony.")
