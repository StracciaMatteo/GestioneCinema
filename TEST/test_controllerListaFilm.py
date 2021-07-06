from unittest import TestCase
from film.model import film
from listaFilm.model.listaFilm import listaFilm


class TestcontrollerListaFilm(TestCase):
    def test_aggiungi_film(self):
        self.test_film = film("Titolo", None, None)
        listaFilm.aggiungi_film(self, self.test_film)
        self.assertTrue()

    def test_rimuovi(self):
        self.fail()

    def test_get_lista_film(self):
        self.fail()

    def test_get_film_by_name(self):
        self.fail()

    def test_leggi(self):
        self.fail()

    def test_aggiorna_programmazione(self):
        self.fail()

    def test_vendi_biglietto(self):
        self.fail()

    def test_rimborsa_biglietto(self):
        self.fail()

    def test_get_vendite_giornaliere(self):
        self.fail()

    def test_save(self):
        self.fail()
