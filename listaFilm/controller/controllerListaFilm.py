from listaFilm.model.listaFilm import listaFilm


class controllerListaFilm():
    def __init__(self):
        super(controllerListaFilm, self).__init__()
        self.model = listaFilm()

    # funzioni riguardanti i film
    def aggiungi_film(self, film):
        self.model.aggiungi_film(film)

    def rimuovi(self, film):
        return self.model.rimuovi(film)

    def get_lista_film(self):
        return self.model.get_lista_film()

    def get_film_by_name(self, name):
        return self.model.get_film_by_name(name)

    # funzioni riguardanti gli spettacoli
    def leggi(self, data, vista):
        self.model.leggi(data, vista)

    def aggiorna_programmazione(self, data, testo, item):
        self.model.aggiorna_programmazione(data, testo, item)

    # funzioni per vendita e rimborso biglietti

    def vendi_biglietto(self, data, item, quantità):
        return self.model.vendi_biglietto(data, item, quantità)

    def rimborsa_biglietto(self, codice_univoco):
        self.model.rimborsa_biglietto(codice_univoco)

    # salvataggio
    def save(self):
        self.model.save()
