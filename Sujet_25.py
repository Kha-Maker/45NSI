# Exo 1:
def enumere(L: list) -> dict:
    dic = {}
    for ind in range(len(L)):
        val = L[ind]
        dic[val] = dic.get(val, []) + [ind]
        """
        Documentation of .get(__key, __default)
        Return the value for key if key is in the dictionary, else default.
        """
    return dic


assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}

# Exo 2:
class Arbre:
    
    
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None
        
        
def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste


def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
    un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg != None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd != None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)
            
# Racine
arbre = Arbre(5) 

# Fils Gauche
arbre.fg = Arbre(2)
arbre.fg.fd = Arbre(3)

# Fils Droit
arbre.fd = Arbre(7)

#     5
#   /   \
#  2     7
#   \
#    3

assert parcours(arbre, []) == [2, 3, 5, 7]
insere(arbre, 1)
print(parcours(arbre, []))
insere(arbre, 4)
print(parcours(arbre, []))
insere(arbre, 6)
print(parcours(arbre, []))
insere(arbre, 8)
print(parcours(arbre, []))
assert parcours(arbre, []) == [1, 2, 3, 4, 5, 6, 7, 8]