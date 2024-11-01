class MovieView:
    def __init__(self):
        self.scanner = input  # używamy input() do wczytywania danych

    def display_main_menu(self):
        print("Wybierz bazę filmową:")
        print("1. OMDb")
        print("2. TMDb")
        print("3. Zakończ działanie programu")
        return int(self.scanner())

    def display_sub_menu(self, service):
        print(f"\n{service} Menu:")
        print("1. Wyszukaj film")
        if service == "TMDb":
            print("2. Wyświetl listę obecnie granych filmów")
            print("3. Wyświetl listę najlepiej ocenianych filmów")
            print("4. Wyświetl ulubione filmy")
            print("5. Dodaj film do ulubionych")
            print("6. Powrót do głównego menu")
        else:
            print("2. Wyświetl ulubione filmy")
            print("3. Dodaj film do ulubionych")
            print("4. Powrót do głównego menu")
        return int(self.scanner())

    def get_movie_title(self):
        print("Podaj tytuł filmu:")
        return self.scanner().strip()  # Usuwamy białe znaki na początku i końcu

    def display_movie_details(self, movie):
        print(f"\nTytuł: {movie.title}\nReżyser: {movie.director}\nData produkcji: {movie.releaseDate}\nOpis: {movie.overview}\nOcena: {movie.rating}")
        print("---------------------------")

    def display_favorite_movies(self, favorite_movies):
        if not favorite_movies:
            print("Brak ulubionych filmów.")
        else:
            print("Ulubione filmy:")
            for movie in favorite_movies:
                self.display_movie_details(movie)

    def display_message(self, message):
        print(message)
