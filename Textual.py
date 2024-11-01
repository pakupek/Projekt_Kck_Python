from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Static
from textual.events import Click, Event
from textual.reactive import reactive
from textual.message import Message
from OmdbService import OmdbService
from TmdbService import TmdbService
from MovieController import MovieController
from textual import on
from MovieView import MovieView

class TextualView(App):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.selected_choice = None  # Przechowuj instancję MovieController

    async def on_mount(self):
        await self.display_main_menu()  # Wyświetl główne menu po zamontowaniu

    async def display_main_menu(self):
        # Utwórz kontener menu
        menu_container = Vertical(id="menu_container")

        # Zamontuj kontener w aplikacji
        await self.mount(menu_container)

        # Dodaj nagłówek do kontenera
        header = Static("Wybierz bazę filmową:")
        await menu_container.mount(header)  # Najpierw zamontuj nagłówek

        # Stwórz przyciski
        omdb_button = Button("1. OMDb", id="omdb_button")
        tmdb_button = Button("2. TMDb", id="tmdb_button")
        exit_button = Button("3. Zakończ działanie programu", id="exit_button")

        # Zamontuj przyciski w kontenerze
        await menu_container.mount(omdb_button)
        await menu_container.mount(tmdb_button)
        await menu_container.mount(exit_button)

    async def display_sub_menu(self, title):
        sub_menu_container = Vertical(id="sub_menu_container")
        await self.mount(sub_menu_container)

        # Dodaj nagłówek
        header = Static(title)
        await sub_menu_container.mount(header)

        # Przyciski opcji menu
        option1 = Button("1. Search Movie", id="option_1")
        option2 = Button("2. Display Favorites", id="option_2")
        option3 = Button("3. Add to Favorites", id="option_3")
        exit_button = Button("4. Exit", id="exit_button")

        # Zamontuj przyciski
        await sub_menu_container.mount(option1, option2, option3, exit_button)


    # Dekoratory dla zdarzeń naciśnięcia przycisków
    @on(Button.Pressed, "#omdb_button")
    async def handle_omdb_click(self):
        await self.controller.omdb_menu()  # Wywołaj metodę omdb_menu z kontrolera
        

    @on(Button.Pressed, "#tmdb_button")
    async def handle_tmdb_click(self):
        await self.controller.tmdb_menu()  # Wywołaj metodę tmdb_menu z kontrolera
        

    @on(Button.Pressed, "#exit_button")
    async def handle_exit_click(self):
        await self.shutdown()  # Zakończ działanie aplikacji

    


# Przykład użycia
if __name__ == "__main__":
    omdb_service = OmdbService()
    tmdb_service = TmdbService()
    controller = MovieController(view=None, omdb_service=omdb_service, tmdb_service=tmdb_service)  # Twórz kontroler bez widoku

    app = TextualView(controller=controller)  # Przekazuj kontroler do widoku
    controller.view = app  # Przypisz widok do kontrolera


    # Krok 5: Uruchom aplikację
    app.run()
    
    
