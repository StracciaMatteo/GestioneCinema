import json
import os
import pickle
from operator import attrgetter

from PyQt5.QtWidgets import QTableWidgetItem


class listaFilm():
    def __init__(self):
        super(listaFilm, self).__init__()
        self.lista_film = []
        self.spettacoli = ''

        # carica lista dei film
        if os.path.isfile('listaFilm/data/lista_film.pickle'):
            with open('listaFilm/data/lista_film.pickle', 'rb') as f:
                self.lista_film = pickle.load(f)

        # carica programmazione
        if os.path.isfile('listaFilm/data/programmazione.json'):
            with open('listaFilm/data/programmazione.json', 'r') as p:
                self.spettacoli = json.load(p)

        # rimuove programmazione più vecchia di 3 giorni
        '''for data in self.spettacoli:
            oggi = '''

    # funzioni riguardanti i film
    def aggiungi_film(self, film):
        self.lista_film.append(film)
        # ordina film alfabeticamente
        self.lista_film.sort(key=attrgetter('titolo'), reverse=False)

    def rimuovi(self, film):
        self.lista_film.remove(film)
        self.elimina_film_da_programmazione(film)

    def get_lista_film(self):
        return self.lista_film

    def get_film_by_name(self, name):
        for film in self.lista_film:
            if name == film.titolo:
                return film

    # funzioni riguardanti gli spettacoli
    def leggi(self, data, vista):

        if not data in self.spettacoli:
            self.spettacoli.update({data: [{"nome": "sala1", "15:00": '', "18:00": '', "21:00": '', "00:00": ''},
                                           {"nome": "sala2", "15:00": '', "18:00": '', "21:00": '', "00:00": ''},
                                           {"nome": "sala3", "15:00": '', "18:00": '', "21:00": '', "00:00": ''},
                                           {"nome": "sala4", "15:00": '', "18:00": '', "21:00": '', "00:00": ''},
                                           {"nome": "sala5", "15:00": '', "18:00": '', "21:00": '', "00:00": ''}]})

        index = 0
        for item in self.spettacoli[data]:
            vista.table_programmazione.setItem(index, 0, QTableWidgetItem(
                self.spettacoli[data][index]["15:00"]))
            vista.table_programmazione.setItem(index, 1, QTableWidgetItem(
                self.spettacoli[data][index]["18:00"]))
            vista.table_programmazione.setItem(index, 2, QTableWidgetItem(
                self.spettacoli[data][index]["21:00"]))
            vista.table_programmazione.setItem(index, 3, QTableWidgetItem(
                self.spettacoli[data][index]["00:00"]))
            index += 1

    def aggiorna_programmazione(self, data, testo, item):
        if item.column() == 0:
            orario = "15:00"
        elif item.column() == 1:
            orario = "18:00"
        elif item.column() == 2:
            orario = "21:00"
        else:
            orario = "00:00"

        self.spettacoli[data][item.row()][orario] = testo

    # prende in input il film da rimuovere e lo rimuove dalla lista della programmazione
    def elimina_film_da_programmazione(self, film):
        for data in self.spettacoli:
            for sala in range(5):
                for orario in {"15:00", "18:00", "21:00", "00:00"}:
                    if self.spettacoli[data][sala][orario] == film.titolo:
                        self.spettacoli[data][sala][orario] = ''
        # Ricaricare la view programmazione per visualizzare le modifiche in seguito all'eliminazione


    # salvataggio
    def save(self):
        # salvataggio lista film
        with open('listaFilm/data/lista_film.pickle', 'wb') as handle:
            pickle.dump(self.lista_film, handle, pickle.HIGHEST_PROTOCOL)
        # salvataggio programmazione
        with open("listaFilm/data/programmazione.json", "w") as outfile:
            json.dump(self.spettacoli, outfile, indent=4)
