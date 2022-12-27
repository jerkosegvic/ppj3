class Cvor:
    korijen = None
    cid = 0
    cvorovi = []
    def __init__(self, value, nas = {}, tip = None, rt = None, dubina = 0, parent = None):
        self.value = value
        self.dubina = dubina
        self.parent = parent
        self.children = []
        self.tablica_lokalnih = {}
        self.nasljedena_tablica = nas
        self.tip = tip
        self.return_tip = rt
        self.id = Cvor.cid
        Cvor.cid += 1
        Cvor.cvorovi.append(self)

    def add_child(self, child):
        self.children.append(child)
    
    def go_up(self, n):
        if self.parent == None:
            return self
        if n == 0:
            return self
        else:
            return self.parent.go_up(n-1)
    
    def __str__(self):
        return self.dubina*" " + self.value + ", tip je " + str(self.tip) + ", vraca " + str(self.return_tip) +  ", ID " + str(self.id)
    
    def print_tree(self):
        print(self)
        for child in self.children:
            child.print_tree()
