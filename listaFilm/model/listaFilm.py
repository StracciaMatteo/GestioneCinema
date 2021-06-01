import os
import pickle

class listaFilm():
    def __init__(self):
        super(listaFilm, self).__init__()
        self.lista_film = []
        if os.path.isfile('listaFilm/data/lista_film.pickle'):
            with open('listaFilm/data/lista_film.pickle', 'rb') as f:
                self.lista_film = pickle.load(f)

    def aggiungi_film(self, film):
        self.lista_film.append(film)

    def rimuovi(self, film):
        self.lista_film.remove(film)

    def get_lista_film(self):
        return self.lista_film

    def get_film_by_name(self, name):
        for film in self.lista_film:
            if name == film.titolo:
                return film

    def save(self):
        with open('listaFilm/data/lista_film.pickle', 'wb') as handle:
            pickle.dump(self.lista_film, handle, pickle.HIGHEST_PROTOCOL)
