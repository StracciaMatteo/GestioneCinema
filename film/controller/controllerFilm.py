from film.model.film import film


class controllerFilm():
    def __init__(self, titolo, durata, intervallo):
        self.model = film(titolo, durata, intervallo)

    def get_titolo(self):
        return self.model.titolo

    def get_durata(self):
        return self.model.durata

    def get_intervallo(self):
        return self.model.intervallo
