class controllerFilm():
    def __init__(self, film):
        self.model = film

    def get_titolo(self):
        return self.model.titolo

    def get_durata(self):
        return self.model.durata

    def get_intervallo(self):
        return self.model.intervallo
