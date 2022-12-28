import GenerativnoStablo as GS
import zavrsni_klase as ZK
import pomocne_funkcije as pomocne

#IZRAZI
class primarni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None
    
    def izvedi_svojstva(self):
        if len(self.children) == 1:
            child = self.children[0]

            if isinstance(child, ZK.IDN):
                self.tip = child.tip
                self.lizraz = child.lizraz
                uvjet = pomocne.provjeri_idn(c1)

                if not uvjet:
                    pass

            elif isinstance(child, ZK.BROJ):
                self.tip = 'int'
                self.lizraz = 0

            elif isinstance(child, ZK.ZNAK):
                self.tip = 'char'
                self.lizraz = 0
            
            elif isinstance(child, ZK.NIZ_ZNAKOVA):
                self.tip = 'niz(const(char))'
                self.lizraz = 0
            
            else:
                pass        

        elif len(self.children) == 3:
            c1 = self.children[0]        
            c2 = self.children[1]        
            c3 = self.children[2]     

            if isinstance(c1, ZK.L_ZAGRADA) and isinstance(c2, izraz) and isinstance(c3, ZK.D_ZAGRADA):
                c2.izvedi_svojstva() # trebamo još vidjet što znači provjeri, pretpostavljam da to osigurava da svojstva postoje

                self.tip = c2.tip
                self.lizraz = c2.lizraz
            else:
                pass 
        
        else:
            pass

        
class postfiks_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def dohvati_idn(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, primarni_izraz):

                if isinstance(c1.children[0], ZK.IDN):
                    return c1.children[0].ime
        
        return None

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            child = self.children[0]

            if isinstance(child, primarni_izraz):
                child.izvedi_svojstva()
                self.tip = child.tip
                self.lizraz = child.lizraz
            else:
                pass

        elif len(self.children == 4): 
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]

            if isinstance(c1, postfiks_izraz) and isinstance(c2, ZK.LU_ZAGRADA) and isinstance(c3, izraz) and isinstance(c4, ZK.DU_ZAGRADA):

                #ovo je indeksiranje, oblik tipa a[2]

                c1.izvedi_svojstva()

                if c1.tip.startswith('niz'): #trebamo se jos dogovorit kako tip odredit, ugl ovo mora provjeravat je li c1 dopušteni niz
                    # niz tipa niz(niz(int)) nije dopušten!
                    tip = c1.tip[4:len(c1.tip)-1]
                    self.tip = tip
                    # osiguraj samo jedan niz
                    if tip.startswith('const'):
                        self.lizraz = 0
                    else:
                        self.lizraz = 1

                    c3.izvedi_svjostva()

                    if c3.tip != 'int':
                        pass
            
            elif isinstance(c1, postfiks_izraz) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, lista_argumenata) and isinstance(c4, ZK.D_ZAGRADA):
                #ovo je za poziv funckije s argumentima!

                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                parametri = c1.parm_tip
                argumetni = c3.tipovi

                valjano = pomocne.provjeri_valjanost_argumenata(self,argumetni)

                if not valjano:
                    pass

                self.tip = c1.pov
                self.lizraz = 0
            else:
                pass
        
        elif len(self.children) == 3:
            #poziv f-je bez argumenata
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1,postfiks_izraz) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, ZK.D_ZAGRADA):

                c1.izvedi_svojstva()
                self.tip = c1.pov

                if c1.arg_tip != 'void':
                    pass
            else:
                pass
        
        elif len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if isinstance(c1, postfiks_izraz) and (isinstance(c2,ZK.OP_INC) or isinstance(c2,ZK.OP_DEC)):
                c1.izvedi_svojstva()

                if c1.lizraz == 0 or c1.tip != 'int':
                    pass

                self.tip = c1.tip
                self.lizraz = 0
        
        else:
            pass


                    


class lista_argumenata(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tipovi = []

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, izraz_pridruzivanja):
                c1.izvedi_svojstva()
                self.tipovi.append(c1.tip)
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, lista_argumenata) and isinstance(c2, ZK.ZAREZ) and isinstance(c3, izraz_pridruzivanja):

                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                self.tipovi = c1.tipovi.append(c3.tip)

            else:
                pass
        else:
            pass


class unarni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]
            if isinstance(c1,postfiks_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass
        
        elif len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if (isinstance(c1, ZK.OP_INC) or isinstance(c1, ZK.OP_DEC)) and isinstance(c2, unarni_izraz):
                c2.izvedi_svojstva()

                if c2.lizraz == 0 or c2.tip != 'int':
                    pass #moramo se dogovorit oko errora, najbolje da tu odma izhendlamo kraj

                self.tip = 'int' #moze i c2.tip
                self.lizraz = 0

            elif isinstance(c1, unarni_operator) and isinstance(c2, cast_izraz):
                c2.izvedi_svojstva()

                if c2.tip != 'int':
                    pass

                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass


class unarni_operator(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

class cast_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, unarni_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 4:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]

            if isinstance(c1, ZK.L_ZAGRADA) and isinstance(c2, ime_tipa) and isinstance(c3, ZK.D_ZAGRADA) and isinstance(c4, cast_izraz):
                c2.izvedi_svojstva()
                c4.izvedi_svojstva()

                pomocne.provjeri_cast(c2.tip, c4.tip)

                self.tip = c2.tip
                self.lizraz = 0
            else:
                pass
        else:
            pass
            

class ime_tipa(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1,specifikator_tipa):
                c1.izvedi_svojstva()
                self.tip = c1.tip
            else:
                pass
        elif len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if isinstance(c1, ZK.KR_CONST) and isinstance(c2,specifikator_tipa):
                c2.izvedi_svojstva()

                if c2.tip == 'void':
                    pass

                self.tip = c2.tip
            else:
                pass
        else:
            pass

class specifikator_tipa(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, ZK.KR_VOID):
                self.tip = 'void'
            elif isinstance(c1, ZK.KR_CHAR):
                self.tip = 'char'
            elif isinstance(c1, ZK.KR_INT):
                self.tip = 'int'
            else:
                pass
        else:
            pass


class multiplikativni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, cast_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, multiplikativni_izraz) and (isinstance(c2,ZK.OP_PUTA) or isinstance(c2,ZK.OP_DIJELI) or isinstance(c2,ZK.OP_MOD)) and isinstance(c3, cast_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class aditivni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None
    
    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, multiplikativni_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, aditivni_izraz) and (isinstance(c2,ZK.PLUS) or isinstance(c2,ZK.MINUS)) and isinstance(c3, multiplikativni_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class odnosni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, aditivni_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, odnosni_izraz) and (isinstance(c2,ZK.OP_LT) or isinstance(c2,ZK.OP_LTE) or isinstance(c2,ZK.OP_GT) or isinstance(c2,ZK.OP_GTE)) and isinstance(c3, aditivni_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class jednakosni_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, odnosni_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, aditivni_izraz) and (isinstance(c2,ZK.OP_EQ) or isinstance(c2,ZK.NEQ)) and isinstance(c3, odnosni_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class bin_i_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, jednakosni_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, bin_i_izraz) and isinstance(c2, ZK.OP_BIN_I) and isinstance(c3, jednakosni_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class bin_xili_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, bin_i_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, bin_xili_izraz) and isinstance(c2, ZK.OP_BIN_XILI) and isinstance(c3, bin_i_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class bin_ili_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None     

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, bin_xili_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, bin_ili_izraz) and isinstance(c2, ZK.OP_BIN_ILI) and isinstance(c3, bin_xili_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass                                   

class log_i_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, bin_ili_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, log_i_izraz) and isinstance(c2, ZK.OP_I) and isinstance(c3, bin_ili_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class log_ili_izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, log_i_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, log_ili_izraz) and isinstance(c2, ZK.OP_ILI) and isinstance(c3, log_i_izraz):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != 'int' and c2.tip != 'int':
                    pass
                
                self.tip = 'int'
                self.lizraz = 0
            else:
                pass
        else:
            pass

class izraz_pridruzivanja(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, log_ili_izraz):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, postfiks_izraz) and isinstance(c2, ZK.OP_PRIDRUZI) and isinstance(c3, izraz_pridruzivanja):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c1.tip != c2.tip:
                    pass
                
                self.tip = c1.tip
                self.lizraz = 0
            else:
                pass
        else:
            pass

class izraz(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tip = None
        self.lizraz = None

    def izvedi_svojstva(self):

        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, izraz_pridruzivanja):
                c1.izvedi_svojstva()
                self.tip = c1.tip
                self.lizraz = c1.lizraz
            else:
                pass

        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, izraz) and isinstance(c2, ZK.ZAREZ) and isinstance(c3, izraz_pridruzivanja):
                c1.izvedi_svojstva()
                c3.izvedi_svojstva()
                
                self.tip = c3.tip
                self.lizraz = 0
            else:
                pass
        else:
            pass

#NAREDBE
class slozena_naredba(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        if len(self.children) == 3:

            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, ZK.L_VIT_ZAGRADA) and isinstance(c2, lista_naredbi) and isinstance(c3, ZK.D_VIT_ZAGRADA):

                c2.izvedi_svojstva()
            else:
                pass

        elif len(self.children) == 4:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]

            if isinstance(c1,ZK.L_VIT_ZAGRADA) and isinstance(c2,lista_deklaracija) \
                and isinstance(c3, lista_naredbi) and isinstance(c4,ZK.D_VIT_ZAGRADA):
                c2.izvedi_svojstva()
                c3.izvedi_svojstva()

            else:
                pass
    
        else:
            pass


class lista_naredbi(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, naredba):
                c1.izvedi_svojstva()
            else:
                pass
        elif len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if isinstance(c1, lista_naredbi) and isinstance(c2, naredba):
                c1.izvedi_svojstva()
                c2.izvedi_svojstva()

            else: pass
        else:
            pass


class naredba(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]
            if isinstance(c1, slozena_naredba):
                c1.izvedi_svojstva()

            elif isinstance(c1, izraz_naredba):
                c1.izvedi_svojstva()

            elif isinstance(c1, naredba_grananja):
                c1.izvedi_svojstva()
            
            elif isinstance(c1, naredba_petlje):
                c1.izvedi_svojstva()

            elif isinstance(c1, naredba_skoka):
                c1.izvedi_svojstva()

            else:
                pass
        else:
            pass

class izraz_naredba(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, ZK.TOCKAZAREZ):
                self.tip = 'int'
            else:
                pass
        elif len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if isinstance(c1, izraz) and isinstance(c2, ZK.TOCKAZAREZ):
                c1.izvedi_svojstva()
                self.tip = c1.tip
            else:
                pass
        else:
            pass

class naredba_grananja(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        if len(self.children) == 5:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]
            c5 = self.children[4]

            if isinstance(c1, ZK.KR_IF) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, izraz) \
                and isinstance(c4, ZK.D_ZAGRADA) and isinstance(c5, naredba):

                c3.izvedi_svojstva()

                if c3.tip != 'int':
                    pass

                c5.izvedi_svojstva()
            
            else:
                pass

        elif len(self.children) == 7:

            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]
            c5 = self.children[4]
            c6 = self.children[4]
            c7 = self.children[4]

            if isinstance(c1, ZK.KR_IF) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, izraz) \
                and isinstance(c4, ZK.D_ZAGRADA) and isinstance(c5, naredba) and isinstance(c6, ZK.KR_ELSE) and isinstance(c7, naredba):

                c3.izvedi_svojstva()

                if c3.tip != 'int':
                    pass

                c5.izvedi_svojstva()
                c7.izvedi_svojstva()

            else:
                pass

        else:
            pass
            




class naredba_petlje(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):

        if len(self.children) == 5:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]
            c5 = self.children[4]

            if isinstance(c1, ZK.KR_WHILE) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, izraz) \
                and isinstance(c4, ZK.D_ZAGRADA) and isinstance(c5, naredba):

                c3.izvedi_svojstva()

                if c3.tip != 'int':
                    pass

                c5.izvedi_svojstva()
            
            else:
                pass

        elif len(self.children) == 6:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]
            c5 = self.children[4]
            c6 = self.children[5]

            if isinstance(c1, ZK.KR_FOR) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, izraz_naredba) \
               and isinstance(c4, izraz_naredba) and isinstance(c5, ZK.D_ZAGRADA) and isinstance(c6, naredba):

               c3.izvedi_svojstva()
               c4.izvedi_svojstva()

               if c4.tip != 'int':
                    pass

               c6.izvedi_svojstva()
            else:
                pass

        elif len(self.children) == 7:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]
            c5 = self.children[4]
            c6 = self.children[5]
            c7 = self.children[6]

            if isinstance(c1, ZK.KR_FOR) and isinstance(c2, ZK.L_ZAGRADA) and isinstance(c3, izraz_naredba) \
               and isinstance(c4, izraz_naredba) and isinstance(c5, izraz) and isinstance(c6, ZK.D_ZAGRADA) and isinstance(c7, naredba):

               c3.izvedi_svojstva()
               c4.izvedi_svojstva()

               if c4.tip != 'int':
                    pass
               
               c5.izvedi_svojstva()
               c6.izvedi_svojstva()
            else:
                pass
        else:
            pass



class naredba_skoka(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        if len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if (isinstance(c1, ZK.KR_BREAK) or isinstance(c1, ZK.KR_CONTINUE)) and isinstance(c2, ZK.TOCKAZAREZ):

                uvjet = pomocne.u_petlji(self)

                if not uvjet:
                    pass

            elif isinstance(c1, ZK.KR_RETURN) and isinstance(c2, ZK.TOCKAZAREZ):

                uvjet = pomocne.u_void_funckiji(self)

                if not uvjet:
                    pass

            else:
                pass
        elif len(self.children) == 3:

            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, ZK.KR_RETURN) and isinstance(c2, izraz) and isinstance(c3, ZK.TOCKAZAREZ):
                c2.izvedi_svojstva()
                pov = pomocne.tip_funckije(self, c2.tip)

                if not pov:
                    pass

            else:
                pass
        else:
            pass

class prijevodna_jedinica(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)

    def izvedi_svojstva(self):
        
        if len(self.children) == 1:
            c1 = self.childrem[0] 

            if isinstance(c1, vanjska_deklaracija):
                vanjska_deklaracija.izvedi_svojstva()
            else:
                pass

        elif len(self.children) == 2:
            c1 = self.children[0]
            c2 = self.children[1]

            if isinstance(c1, prijevodna_jedinica) and isinstance(c2, vanjska_deklaracija):

                c1.izvedi_svojstva()
                c2.izvedi_svojstva()
            else:
                pass
        else:
            pass

class vanjska_deklaracija(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)      

    def izvedi_svojstva(self):
        if len(self.children) == 1:

            c1 = self.children[0]

            if isinstance(c1, deklaracija):
                c1.izvedi_svojstva()  
            
            elif isinstance(c1, definicija_funkcije):
                c1.izvedi_svojstva()
            else:
                pass
        else:
            pass

#DEKLARACIJE I DEFINICIJE
class definicija_funkcije(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.ime = None
        self.tip = None
        self.parametri = []
        self.broj_parametara = 0

    #ime funkcije ce mu pridodati IDN, a tip <ime tipa>
    def izvedi_svojstva(self):
        if len(self.children) == 6:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]
            c4 = self.children[3]
            c5 = self.children[4]
            c6 = self.children[5]

            if isinstance(c1, ime_tipa) and isinstance(c2, ZK.IDN) and isinstance(c3, ZK.L_ZAGRADA) \
                and isinstance(c4, ZK.KR_VOID) and isinstance(c5, ZK.D_ZAGRADA) and isinstance(c6, slozena_naredba):

                c1.izvedi_svojstva()

                if c1.tip.startswith('const'):
                    pass

                uvjet = pomocne.provjeri_egzistenciju_funckije(self, c2.ime)

                if uvjet:
                    pass

                #4. provjerit postoji li deklaracije funkcije

                #zabiljezit deklaraciju

                c6.izvedi_svojstva()

            elif isinstance(c1, ime_tipa) and isinstance(c2, ZK.IDN) and isinstance(c3, ZK.L_ZAGRADA) \
                and isinstance(c4, lista_parametara) and isinstance(c5, ZK.D_ZAGRADA) and isinstance(c6, slozena_naredba):

                c1.izvedi_svojstva()

                if c1.tip.startswith('const'):
                    pass

                uvjet = pomocne.provjeri_egzistenciju_funckije(self, c2.ime)

                if uvjet:
                    pass

                c4.izvedi_svojstva()

                # provjeri postoji li deklaracija
                # zabilježi funkciju
                # dodat varijable u funkciji
            else:
                pass
        else:
            pass




class lista_parametara(GS.Cvor):
    def __init__(self, value, dubina = 0, parent = None):
        GS.Cvor.__init__(self, value, dubina, parent)
        self.tipovi = []
        self.imena = []

    def izvedi_svojstva(self):
        if len(self.children) == 1:
            c1 = self.children[0]

            if isinstance(c1, deklaracija_parametra):

                c1.izvedi_svojstva()

                self.tipovi = [c1.tip]
                self.imena = [c1.ime]

            else:
                pass
        elif len(self.children) == 3:
            c1 = self.children[0]
            c2 = self.children[1]
            c3 = self.children[2]

            if isinstance(c1, lista_parametara) and isinstance(c2, ZK.ZAREZ) and isinstance(c3, deklaracija_parametra):

                c1.izvedi_svojstva()
                c3.izvedi_svojstva()

                if c3.ime in c1.imena:
                    pass

                self.tipovi = c1.tipovi.append(c3.tip)
                self.imena = c1.imena.append(c3.ime)
            else:
                pass
        else:
            pass

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
