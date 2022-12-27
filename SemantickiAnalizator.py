import sys
import GenerativnoStablo as GS
import nezavrsni_klase as NK
import ProgramskoStablo as PS
import zavrsni_klase as ZK

ulaz = sys.stdin.read()
lines = ulaz.split('\n')
lines.pop()
#print(lines)

trenutni_blok = PS.Cvor("Globalni blok")
PS.Cvor.korijen = trenutni_blok
trenutni = None
dubina = 0
dubina_bloka = 0

def novi_cvor(fullvalue, dubina = 0, parent = None):
    novi = None
    value_list = fullvalue.split(' ')
    value = value_list[0]
    match value:
        case "<primarni_izraz>":
            novi = NK.primarni_izraz(value, dubina, parent)
        case "<postfiks_izraz>":
            novi = NK.postfiks_izraz(value, dubina, parent)
        case "<lista_argumenata>":
            novi = NK.lista_argumenata(value, dubina, parent)
        case "<unarni_izraz>":
            novi = NK.unarni_izraz(value, dubina, parent)
        case "<unarn_ operator>":
            novi = NK.unarni_operator(value, dubina, parent)
        case "<cast_izraz>":
            novi = NK.cast_izraz(value, dubina, parent)
        case "<ime_tipa>":
            novi = NK.ime_tipa(value, dubina, parent)
        case "<specifikator_tipa>":
            novi = NK.specifikator_tipa(value, dubina, parent)
        case "<multiplikativni_izraz>":
            novi = NK.multiplikativni_izraz(value, dubina, parent)
        case "<aditivni_izraz>":
            novi = NK.aditivni_izraz(value, dubina, parent)
        case "<odnosni_izraz>":
            novi = NK.odnosni_izraz(value, dubina, parent)
        case "<jednakosni_izraz>":
            novi = NK.jednakosni_izraz(value, dubina, parent)
        case "<bin_i_izraz>":
            novi = NK.bin_i_izraz(value, dubina, parent)
        case "<bin_xili_izraz>":
            novi = NK.bin_xili_izraz(value, dubina, parent)
        case "<bin_ili_izraz>":
            novi = NK.bin_ili_izraz(value, dubina, parent)
        case "<log_i_izraz>":
            novi = NK.log_i_izraz(value, dubina, parent)
        case "<log_ili_izraz>":
            novi = NK.log_ili_izraz(value, dubina, parent)
        case "<izraz_pridruzivanja>":
            novi = NK.izraz_pridruzivanja(value, dubina, parent)
        case "<izraz>":
            novi = NK.izraz(value, dubina, parent)
        case "<slozena_naredba>":
            global trenutni_blok
            global dubina_bloka
            novi = NK.slozena_naredba(value, dubina, parent)
            pnovi = PS.Cvor(value, trenutni_blok.dubina + 1, trenutni_blok)
            trenutni_blok.add_child(pnovi)
            trenutni_blok = pnovi
            dubina_bloka = dubina
            #print(dubina_bloka)
        case "<lista_naredbi>":
            novi = NK.lista_naredbi(value, dubina, parent)
        case "<naredba>":
            novi = NK.naredba(value, dubina, parent)
        case "<izraz_naredba>":
            novi = NK.izraz_naredba(value, dubina, parent)
        case "<naredba_grananja>":
            novi = NK.naredba_grananja(value, dubina, parent)
        case "<naredba_petlje>":
            novi = NK.naredba_petlje(value, dubina, parent)
        case "<naredba_skoka>":
            novi = NK.naredba_skoka(value, dubina, parent)
        case "<prijevodna_jedinica>":
            novi = NK.prijevodna_jedinica(value, dubina, parent)
        case "<vanjska_deklaracija>":
            novi = NK.vanjska_deklaracija(value, dubina, parent)
        case "<definicija_funkcije>":
            novi = NK.definicija_funkcije(value, dubina, parent)
        case "<lista_parametara>":
            novi = NK.lista_parametara(value, dubina, parent)
        case "<deklaracija_parametra>":
            novi = NK.deklaracija_parametra(value, dubina, parent)
        case "<lista_deklaracija>":
            novi = NK.lista_deklaracija(value, dubina, parent)
        case "<deklaracija>":
            novi = NK.deklaracija(value, dubina, parent)
        case "<lista_init_deklaratora>":
            novi = NK.lista_init_deklaratora(value, dubina, parent)
        case "<init_deklarator>":
            novi = NK.init_deklarator(value, dubina, parent)
        case "<izravni_deklarator>":
            novi = NK.izravni_deklarator(value, dubina, parent)
        case "<inicijalizator>":
            novi = NK.inicijalizator(value, dubina, parent)
        case "<lista_izraza_pridruzivanja>":
            novi = NK.lista_izraza_pridruzivanja(value, dubina, parent)
        case "IDN":
            novi = ZK.IDN(value, value_list[2], dubina, parent)
        case "BROJ":
            novi = ZK.BROJ(value, value_list[2], dubina, parent)
        case "ZNAK":
            novi = ZK.ZNAK(value, value_list[2], dubina, parent)
        case "NIZ_ZNAKOVA":
            novi = ZK.NIZ_ZNAKOVA(value, value_list[2], dubina, parent)
        case _ :
            novi = GS.Cvor(value, dubina, parent)
    GS.Cvor.tablice.append(trenutni_blok.id)
    print(novi)  

    return novi

for line in lines:
    bez_spaceova = line.lstrip()
    num_leading_spaces = len(line) - len(bez_spaceova)
    if trenutni == None:
        #print("bez spaceova: " , end = " -> ")
        #print(bez_spaceova)
        trenutni = novi_cvor(bez_spaceova, dubina)
        GS.Cvor.korijen = trenutni
        dubina = num_leading_spaces
        continue

    if num_leading_spaces > dubina:
        dubina = num_leading_spaces
        novi = novi_cvor(bez_spaceova, dubina, trenutni)
        trenutni.add_child(novi)
        trenutni = novi

    elif num_leading_spaces < dubina:
        trenutni = trenutni.go_up(dubina - num_leading_spaces )
        dubina = num_leading_spaces
        if dubina < dubina_bloka:
            trenutni_blok = trenutni_blok.go_up(1)
            dubina_bloka = dubina
            #print("mijenjam neki kurac")
            #print(trenutni)
            #print(trenutni_blok)
        novi = novi_cvor(bez_spaceova, dubina, trenutni.parent)
        trenutni.parent.add_child(novi)  
        trenutni = novi
        

    else:
        novi = novi_cvor(bez_spaceova, dubina, trenutni.parent)
        trenutni.parent.add_child(novi)
        trenutni = novi

    #print(trenutni)
    
GS.Cvor.korijen.print_tree()
PS.Cvor.korijen.print_tree()
