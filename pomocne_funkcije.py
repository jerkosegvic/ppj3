import GenerativnoStablo as GS
import ProgramskoStablo as PS
import zavrsni_klase as ZK
import nezavrsni_klase as NK
import deklaracije as D

def provjeri_idn(cvor):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if cvor.ime in blok_cvor.tablica_lokalnih.keys() or \
       cvor.ime in blok_cvor.nasljedena_tablica.keys():
        return True
    return False

def provjeri_valjanost_argumenata(cvor, argumenti):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if isinstance(cvor, NK.postfiks_izraz):
        idn = cvor.duhvati_idn()
        if idn != None:
            if idn.ime in blok_cvor.tablica_lokalnih.keys():
                dek = blok_cvor.tablica_lokalnih[idn.ime]
                if isinstance(dek, D.funkcija):
                    if len(dek.argumenti) == len(argumenti):
                        for i in range(len(dek.argumenti)):
                            if dek.argumenti[i].tip != argumenti[i]:
                                return False
                        return True
                    else:
                        return False

            elif idn.ime in blok_cvor.nasljedena_tablica.keys():
                dek = blok_cvor.nasljedena_tablica[idn.ime]
                if isinstance(dek, D.funkcija):
                    if len(dek.argumenti) == len(argumenti):
                        for i in range(len(dek.argumenti)):
                            if dek.argumenti[i].tip != argumenti[i]:
                                return False
                        return True
                    else:
                        return False
    return False

def provjeri_cast():
    pass

def u_petlji(cvor):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if blok_cvor.tip == "for" or blok_cvor.tip == "while":
        return True
    else:
        if blok_cvor.parent == None:
            return False
        else:
            return u_petlji(blok_cvor.parent)

def u_void_funkciji(cvor):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if blok_cvor.return_tip == "void":
        return True
    else:
        if blok_cvor.parent == None:
            return False
        else:
            return u_void_funkciji(blok_cvor.parent)

def tip_funkcije(cvor, trazeni_tip):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if blok_cvor.tip == "funkcija":
        if blok_cvor.return_tip == trazeni_tip:
            return True
        else:
            return False
    else:
        if blok_cvor.parent == None:
            return False
        else:
            return tip_funkcije(blok_cvor.parent, trazeni_tip)            