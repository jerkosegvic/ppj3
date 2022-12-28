class deklaracija:
    def __init__(self, identifikator, tip):
        self.identifikator = identifikator
        self.tip = tip

class varijabla(deklaracija):
    def __init__(self, identifikator, tip, value = None):
        deklaracija.__init__(self, identifikator, tip)
        self.value = value

class niz(deklaracija):
    def __init__(self, identifikator, tip, duljina, values = []):
        deklaracija.__init__(self, identifikator, tip)
        self.duljina = duljina
        self.values = values

class funkcija(deklaracija):
    def __init__(self, identifikator, tip, parametri = None):
        deklaracija.__init__(self, identifikator, tip)
        self.parametri = parametri
        