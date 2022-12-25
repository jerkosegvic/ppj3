import GenerativnoStablo as GS

#IZRAZI
class primarni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None
        
class postfiks_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class lista_argumenata(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tipovi = []

class unarni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class unarni_operator(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class cast_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class ime_tipa(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None

class specifikator_tipa(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None

class multiplikativni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class aditivni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class odnosni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class jednakosni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class bin_i_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class bin_xili_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class bin_ili_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None                                        

class log_i_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class log_ili_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class izraz_pridruzivanja(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

class izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

#NAREDBE
class slozena_naredba(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class lista_naredbi(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class naredba(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class izraz_naredba(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class naredba_grananja(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class naredba_petlje(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class naredba_skoka(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class prijevodna_jedinica(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class vanjska_deklaracija(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)        

#DEKLARACIJE I DEFINICIJE
class definicija_funkcije(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.ime = None
        self.tip = None
        self.parametri = []
        self.broj_parametara = 0

    #ime funkcije ce mu pridodati IDN, a tip <ime tipa>

class lista_parametara(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tipovi = []
        self.imena = []

class deklaracija_parametra(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.ime = None
    
class lista_deklaracija(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
       
class deklaracija(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class lista_init_deklaratora(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class init_deklarator(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        
class izravni_deklarator(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.ime = None
        self.tip = None
        self.broj_elemenata = None

class inicijalizator(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tipovi = []
        self.broj_elemenata = None

class lista_izraza_pridruzivanja(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tipovi = []
        self.broj_elemenata = None
