class deklaracija:
    def __init__(self, identifikator, tip):
        self.identifikator = identifikator
        self.tip = tip

class varijabla(deklaracija):
    def __init__(self, identifikator, tip):
        deklaracija.__init__(self, identifikator, tip)
        self.value = None

class niz(deklaracija):
    def __init__(self, identifikator, tip, duljina):
        deklaracija.__init__(self, identifikator, tip)
        self.duljina = duljina
        self.values = []

class funkcija(deklaracija):
    def __init__(self, identifikator, tip, parametri):
        deklaracija.__init__(self, identifikator, tip)
        self.parametri = parametri
        