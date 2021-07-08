from unittest import TestCase
from PyQt5.QtCore import QDate

from film.model.film import film
from listaFilm.controller.controllerListaFilm import controllerListaFilm


class item():
    def column(self):
        return 1

    def row(self):
        return 1


class TestcontrollerListaFilm(TestCase):

    def setUp(self) -> None:
        self.controller = controllerListaFilm()
        self.film1_prova = film("Titolo 1","","")
        self.film2_prova = film("Titolo 2", "", "")
        self.item_prova = item()

        self.today = QDate.currentDate().toString('d MMMM yyyy')
        # vendi_biglietto e rimborsa_biglietto accettano un QDate e non una stringa
        self.qdate = QDate.currentDate()

    def test_aggiungi_film(self):
        self.controller.aggiungi_film(self.film1_prova)
        self.assertTrue(self.film1_prova in self.controller.model.lista_film)

    def test_rimuovi(self):
        self.controller.aggiungi_film(self.film1_prova)
        self.controller.rimuovi(self.film1_prova)
        self.assertTrue(self.film1_prova not in self.controller.model.lista_film)

    def test_get_lista_film(self):
        for x in range(5):
            self.controller.aggiungi_film(self.film1_prova)
        lista = self.controller.get_lista_film()
        self.assertTrue(len(lista) == 5)

    def test_get_film_by_name(self):
        self.controller.aggiungi_film(self.film1_prova)
        self.controller.aggiungi_film(self.film2_prova)
        film = self.controller.get_film_by_name("Titolo 2")
        if film is None:
            self.fail()
        else:
            self.assertTrue(film.titolo == "Titolo 2")

    def test_leggi(self):
        self.controller.leggi(self.today, None)
        self.assertFalse(self.controller.model.spettacoli == '')

    def test_aggiorna_programmazione(self):
        self.controller.leggi(self.today, None)
        self.controller.aggiorna_programmazione(self.today, "Nuovo titolo", self.item_prova)
        self.assertTrue(self.controller.model.spettacoli[self.today][self.item_prova.row()]["18:00"]["titolo"] == "Nuovo titolo")

    # crash causati da QMessageBox
    '''def test_vendi_biglietto(self):
        self.controller.leggi(self.today, None)
        self.controller.aggiorna_programmazione(self.today, "Nuovo titolo", self.item_prova)
        self.controller.vendi_biglietto(self.qdate, self.item_prova, 1)
        self.assertFalse(self.controller.model.spettacoli[self.today][self.item_prova.row()]["18:00"]["posti"] == 0)

    def test_rimborsa_biglietto(self):
        self.fail()

    def test_get_vendite_giornaliere(self):
        self.fail()'''
