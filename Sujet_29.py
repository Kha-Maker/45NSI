# Exo 1:
class Arbre:
    
    
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None
    

a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)
    

def taille(a: Arbre) -> int:
    tg = taille(a.fg) if a.fg is not None else 0
    td = taille(a.fd) if a.fd is not None else 0
    return 1 + tg + td


def hauteur(a: Arbre) -> int:
    tg = hauteur(a.fg) if a.fg is not None else 0
    td = hauteur(a.fd) if a.fd is not None else 0
    return 1 + max(tg, td)

assert taille(a) == 4
assert hauteur(a) == 3

A = Arbre(0)

A.fg = Arbre(1)
A.fg.fg = Arbre(3)

A.fd = Arbre(2)
A.fd.fg = Arbre(4)
A.fd.fd = Arbre(5)
A.fd.fg.fd = Arbre(6)

assert taille(A) == 7
assert hauteur(A) == 4

# Exo 2:
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[i+1] = element
    return L


assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(4, 4, [7, 8, 9]) == [7, 8, 9, 4]