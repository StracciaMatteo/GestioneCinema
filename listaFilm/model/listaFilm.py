import json
import os
import pickle
import time
from operator import attrgetter

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem

from messaggeError.Error import Error


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

        # rimuove programmazione più vecchia di 7 giorni
        today = QDate.currentDate()
        toRemove = {}
        for data in self.spettacoli:
            data_spettacolo = QDate.fromString(data, 'd MMMM yyyy')
            if today.addDays(-7) > data_spettacolo:
                toRemove.update({data: self.spettacoli[data]})
        for item in toRemove:
            del self.spettacoli[item]

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

        if data not in self.spettacoli:
            self.spettacoli.update({data: [{"nome": "sala1", "15:00": {"titolo": '', "posti": 0},
                                            "18:00": {"titolo": '', "posti": 0},
                                            "21:00": {"titolo": '', "posti": 0},
                                            "00:00": {"titolo": '', "posti": 0}},
                                           {"nome": "sala2", "15:00": {"titolo": '', "posti": 0},
                                            "18:00": {"titolo": '', "posti": 0},
                                            "21:00": {"titolo": '', "posti": 0},
                                            "00:00": {"titolo": '', "posti": 0}},
                                           {"nome": "sala3", "15:00": {"titolo": '', "posti": 0},
                                            "18:00": {"titolo": '', "posti": 0},
                                            "21:00": {"titolo": '', "posti": 0},
                                            "00:00": {"titolo": '', "posti": 0}},
                                           {"nome": "sala4", "15:00": {"titolo": '', "posti": 0},
                                            "18:00": {"titolo": '', "posti": 0},
                                            "21:00": {"titolo": '', "posti": 0},
                                            "00:00": {"titolo": '', "posti": 0}},
                                           {"nome": "sala5", "15:00": {"titolo": '', "posti": 0},
                                            "18:00": {"titolo": '', "posti": 0},
                                            "21:00": {"titolo": '', "posti": 0},
                                            "00:00": {"titolo": '', "posti": 0}}]})

        index = 0
        for item in self.spettacoli[data]:
            vista.table_programmazione.setItem(index, 0, QTableWidgetItem(
                self.spettacoli[data][index]["15:00"]["titolo"]))
            vista.table_programmazione.setItem(index, 1, QTableWidgetItem(
                self.spettacoli[data][index]["18:00"]["titolo"]))
            vista.table_programmazione.setItem(index, 2, QTableWidgetItem(
                self.spettacoli[data][index]["21:00"]["titolo"]))
            vista.table_programmazione.setItem(index, 3, QTableWidgetItem(
                self.spettacoli[data][index]["00:00"]["titolo"]))
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

        self.spettacoli[data][item.row()][orario] = {"titolo": testo, "posti": 0}

    # prende in input il film da rimuovere e lo rimuove dalla lista della programmazione
    def elimina_film_da_programmazione(self, film):
        for data in self.spettacoli:
            for sala in range(5):
                for orario in {"15:00", "18:00", "21:00", "00:00"}:
                    if self.spettacoli[data][sala][orario]["titolo"] == film.titolo:
                        self.spettacoli[data][sala][orario] = {"titolo": '', "posti": 0}

    # funzioni per vendita e rimborso biglietti

    def vendi_biglietto(self, data, item, quantita):
        if item.column() == 0:
            orario = "15:00"
        elif item.column() == 1:
            orario = "18:00"
        elif item.column() == 2:
            orario = "21:00"
        else:
            orario = "00:00"

        # controlla se la quantità è diversa da 0
        if quantita == 0:
            error = Error("Errore", "Selezionare numero positivo di biglietti",
                          "riprovare...")
            error.error_messagge()
        # controlla se il titolo dello spettacolo è vuoto e in tal caso stampa errore
        elif self.spettacoli[data.toString('d MMMM yyyy')][item.row()][orario]["titolo"] != "":
            # controlla che ci siano posti liberi sufficienti
            if self.spettacoli[data.toString('d MMMM yyyy')][item.row()][orario]["posti"] <= (144 - quantita):
                self.spettacoli[data.toString('d MMMM yyyy')][item.row()][orario]["posti"] += quantita

                codice_univoco = data.toString('ddMMyyyy') + str(item.row()) + str(item.column())
                mostra_codice = Error("Operazione effettuata", "Codice biglietto/i:     ", codice_univoco)
                mostra_codice.information_message()
            else:
                error = Error("Errore", "Numero di posti disponibili non sufficiente a soddisfare la richiesta",
                              "selezionare un altro spettacolo")
                error.error_messagge()
        else:
            error = Error("Errore", "Spettacolo selezionato non valido per la vendita dei biglietti",
                          "selezionare un altro spettacolo")
            error.error_messagge()

    def rimborsa_biglietto(self, codice_univoco):
        if len(codice_univoco) != 10:
            error = Error("Errore", "Formato codice errato", "riprova")
            error.error_messagge()
        else:
            indices = [0, 8, 9]
            parts = [codice_univoco[i:j] for i, j in zip(indices, indices[1:] + [None])]
            qdate = QDate.fromString(parts[0], 'ddMMyyyy')
            data = qdate.toString('d MMMM yyyy')
            sala = int(parts[1])

            if int(parts[2]) == 0:
                orario = "15:00"
            elif int(parts[2]) == 1:
                orario = "18:00"
            elif int(parts[2]) == 2:
                orario = "21:00"
            else:
                orario = "00:00"
            try:
                # rimborsa il biglietto se lo spettacolo è presente nel sistema e il biglietto è stato venduto
                if self.spettacoli[data][sala][orario]["posti"] == 0:
                    error = Error("Errore", "Nessun biglietto venduto per questo spettacolo",
                                  "impossibile rimborsare")
                    error.error_messagge()
                else:
                    self.spettacoli[data][sala][orario]["posti"] -= 1
                    info = Error("Rimborso eseguito", f"Biglietto con codice {codice_univoco} rimborsato", "")
                    info.information_message()
            except Exception:
                error = Error("Errore", "Codice errato o spettacolo non più presente nel sistema",
                              "procedere manualmente")
                error.error_messagge()

    # funzione che restituisce array con incassi giornalieri
    def get_vendite_giornaliere(self):
        today = QDate.currentDate()

        # visualizzo le vendite del giorno precedente a tarda serata
        if int(time.strftime('%H', time.localtime())) < 4:
            today.addDays(-1)

        quantita = [0, 0, 0, 0, 0]
        index = 0
        for sala in range(5):
            for orario in {"15:00", "18:00", "21:00", "00:00"}:
                quantita[index] += self.spettacoli[today.toString('d MMMM yyyy')][sala][orario]["posti"]
            index += 1
        return quantita

    # SALVATAGGIO
    def save(self):
        # salvataggio lista film
        with open('listaFilm/data/lista_film.pickle', 'wb') as handle:
            pickle.dump(self.lista_film, handle, pickle.HIGHEST_PROTOCOL)

        # funzione che pulisce self.spettacoli dalle date senza nessun film
        toRemove = {}
        for data in self.spettacoli:
            flag = True
            for sala in range(5):
                for orario in {"15:00", "18:00", "21:00", "00:00"}:
                    if not self.spettacoli[data][sala][orario]["titolo"] == '':
                        flag = False
            if flag:
                # carica le date vuote in un dictionary
                toRemove.update({data: self.spettacoli[data]})
        # legge il dictionary ed elimina le date vuote
        for item in toRemove:
            del self.spettacoli[item]

        # salvataggio programmazione
        with open("listaFilm/data/programmazione.json", "w") as outfile:
            json.dump(self.spettacoli, outfile, indent=4)
