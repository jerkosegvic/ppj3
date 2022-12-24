import sys
import GenerativnoStablo as GS

ulaz = sys.stdin.read()
lines = ulaz.split('\n')
lines.pop()
#print(lines)

trenutni = None
dubina = 0

def novi_cvor(value, dubina = 0, parent = None):
    novi = GS.Cvor(value, dubina, parent)
    return novi

for line in lines:
    bez_spaceova = line.lstrip()
    num_leading_spaces = len(line) - len(bez_spaceova)
    if trenutni == None:
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
        novi = novi_cvor(bez_spaceova, dubina, trenutni.parent)
        trenutni.parent.add_child(novi)
        trenutni = novi

    else:
        novi = novi_cvor(bez_spaceova, dubina, trenutni.parent)
        trenutni.parent.add_child(novi)
        trenutni = novi

    #print(trenutni)
    
GS.Cvor.korijen.print_tree()    