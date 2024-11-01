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

class TextualView(App):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Przechowuj instancję MovieController

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

    # Dekoratory dla zdarzeń naciśnięcia przycisków
    @on(Button.Pressed, "#omdb_button")
    async def handle_omdb_click(self, event: Event):
        await self.controller.omdb_menu()  # Wywołaj metodę omdb_menu z kontrolera

    @on(Button.Pressed, "#tmdb_button")
    async def handle_tmdb_click(self, event: Event):
        await self.controller.tmdb_menu()  # Wywołaj metodę tmdb_menu z kontrolera

    @on(Button.Pressed, "#exit_button")
    async def handle_exit_click(self, event: Event):
        await self.shutdown()  # Zakończ działanie aplikacji


# Przykład użycia
if __name__ == "__main__":
    # Załóżmy, że masz instancje usług OMDb i TMDb oraz stworzoną instancję MovieController
    omdb_service = OmdbService
    tmdb_service = TmdbService
    controller = MovieController(view=None, omdb_service=omdb_service, tmdb_service=tmdb_service)

    # Tworzymy instancję MovieView z kontrolerem
    app = TextualView(controller=controller)
    