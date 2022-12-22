
class Cvor:
    korijen = None
    def __init__(self, value, dubina = 0, parent = None):
        self.value = value
        self.children = []
        self.parent = parent
        self.dubina = dubina
        self.nasljedna = []
        self.izvedena = []
    def go_up(self, n):
        if self.parent == None:
            return self
        if n == 0:
            return self
        else:
            return self.parent.go_up(n-1)
    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self):
        return self.dubina*" " + self.value

    def print_tree(self):
        print(self)
        for child in self.children:
            child.print_tree()
    
    