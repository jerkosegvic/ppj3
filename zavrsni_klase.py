import GenerativnoStablo as GS

class IDN(GS.Cvor):
    def __init__(self, value, vr, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
    def __str__(self):
        return self.dubina*" " + self.value + " -> " + self.ime
class BROJ(GS.Cvor):
    def __init__(self, value, vr, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.vrijednost = vr


    def __str__(self):
        return self.dubina*" " + self.value + " -> " + str(self.vrijednost)

class ZNAK(GS.Cvor):
    def __init__(self, value, vr, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.vrijednost = vr

    def __str__(self):
        return self.dubina*" " + self.value + " -> " + self.vrijednost

class NIZ_ZNAKOVA(GS.Cvor):
    def __init__(self, value, vr, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.vrijednost = vr


    def __str__(self):
        return self.dubina*" " + self.value + " -> " + self.vrijednost
        