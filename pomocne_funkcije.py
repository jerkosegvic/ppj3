import GenerativnoStablo as GS
import ProgramskoStablo as PS
import zavrsni_klase as ZK
import nezavrsni_klase as NK
import deklaracije as D

def provjeri_idn(cvor):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if cvor.ime in blok_cvor.tablica_lokalnih_varijabli.keys() or \
       cvor.ime in blok_cvor.nasljedena_tablica_varijabli.keys() or \
       cvor.ime in blok_cvor.tablica_lokalnih_funkcija.keys() or \
       cvor.ime in blok_cvor.nasljedena_tablica_funkcija.keys():
        return True
    return False

def provjeri_valjanost_argumenata(cvor, argumenti):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if isinstance(cvor, NK.definicija_funkcije):
        idn = cvor.ime
        if idn != None:
            if idn in blok_cvor.tablica_lokalnih_funkcija.keys():
                dek = blok_cvor.tablica_lokalnih_funkcija[idn]
                if isinstance(dek, D.funkcija):
                    if len(dek.parametri) == len(argumenti):
                        for i in range(len(dek.argumenti)):
                            if dek.parametri[i].tip != argumenti[i]:
                                return False
                        return True
                    else:
                        return False

            elif idn in blok_cvor.nasljedena_tablica_funkcija.keys():
                dek = blok_cvor.nasljedena_tablica_funkcija[idn]
                if isinstance(dek, D.funkcija):
                    if len(dek.parametri) == len(argumenti):
                        for i in range(len(dek.parametri)):
                            if dek.parametri[i].tip != argumenti[i]:
                                return False
                        return True
                    else:
                        return False
    return False

def provjeri_valjanost_argumenata_postfiks(cvor, argumenti):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if isinstance(cvor, NK.postfiks_izraz):
        idn = cvor.dohvati_idn()
        if idn != None:
            if idn.ime in blok_cvor.tablica_lokalnih_funkcija.keys():
                dek = blok_cvor.tablica_lokalnih_funkcija[idn.ime]
                if isinstance(dek, D.funkcija):
                    if dek.parametri == None and argumenti == None:
                        return True
                    if len(dek.parametri) == len(argumenti):
                        for i in range(len(dek.argumenti)):
                            if dek.parametri[i].tip != argumenti[i]:
                                return False
                        return True
                    else:
                        return False

            elif idn.ime in blok_cvor.nasljedena_tablica_funkcija.keys():
                dek = blok_cvor.nasljedena_tablica_funkcija[idn.ime]
                if isinstance(dek, D.funkcija):
                    if dek.parametri == None and argumenti == None:
                        return True
                    if len(dek.parametri) == len(argumenti):
                        for i in range(len(dek.parametri)):
                            if dek.parametri[i].tip != argumenti[i]:
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

def porvjeri_egzistenciju(cvor, ime):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if ime in blok_cvor.tablica_lokalnih_funkcija.keys() or \
       ime in blok_cvor.nasljedena_tablica_funkcija.keys():
        return True
    else:
        if blok_cvor.parent == None:
            return False
        else:
            return porvjeri_egzistenciju(blok_cvor.parent, ime)


def dodaj_lokalnu_funkciju_void(cvor, ime, tip, definirana):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    blok_cvor.dodaj_lokalnu_funkciju_void(ime, tip, definirana)

def dodaj_lokalnu_funkciju(cvor, ime, tip, definirana, parametri):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    blok_cvor.dodaj_lokalnu_funkciju(ime, tip, definirana, parametri)

def dodaj_argumente(cvor, argumenti):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    for arg in argumenti:
        blok_cvor.dodaj_lokalnu_varijablu(arg[1], arg[0])

def provjeri_identifikator_lokalno(cvor, ime):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if ime in blok_cvor.tablica_lokalnih_varijabli.keys():
        return True
    else:
        return False

def provjeri_deklaraciju_i_tipove(cvor, ime, tip, parametri = None):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if ime not in blok_cvor.tablica_lokalnih_funkcija.keys():
        return None
    
    dek = blok_cvor.tablica_lokalnih_funkcija[ime]
    if isinstance(dek, D.funkcija):
        if dek.tip == tip:
            if parametri == None and dek.parametri == None:
                return True
            if len(dek.parametri) == len(parametri):
                for i in range(len(dek.parametri)):
                    if dek.parametri[i].tip != parametri[i]:
                        return False
                return True
            else:
                return False
        else:
            return False
    return False
    
def izlaz(cvor):
    out = ""
    out += cvor.value + " ::= " 
    for dijete in cvor.djeca:
        out += str(dijete) + " "
    print(out)
    exit(0) 

def tip_idn(cvor, ime):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    if ime in blok_cvor.tablica_lokalnih_varijabli.keys():
        return blok_cvor.tablica_lokalnih_varijabli[ime].tip
    
    elif ime in blok_cvor.tablica_lokalnih_funkcija.keys():
        return blok_cvor.tablica_lokalnih_funkcija[ime].tip

    elif ime in blok_cvor.nasljedena_tablica_varijabli.keys():
        return blok_cvor.nasljedena_tablica_varijabli[ime].tip

    elif ime in blok_cvor.nasljedena_tablica_funkcija.keys():
        return blok_cvor.nasljedena_tablica_funkcija[ime].tip

    else:
        if blok_cvor.parent == None:
            return None
        else:
            return tip_idn(blok_cvor.parent, ime)

def updateaj_blok(cvor):
    id_bloka = GS.Cvor.tablice[cvor.id]
    blok_cvor = PS.Cvor.cvorovi[id_bloka]
    blok_cvor.update_tablice()