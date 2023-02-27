# Exo 1:
def min_et_max(tab: list) -> dict:
    dic = {'min': tab[0], 'max': tab[0]}
    for elt in tab:
        if elt < dic['min']: dic['min'] = elt 
        if elt > dic['max']: dic['max'] = elt
    return dic


assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}
assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}

# Exo 2:
class Carte:
    
    
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et 
        valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v
        
        
    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10,
        Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]
    
    
    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, 
        carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]


class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 
        objets Carte possibles rangés par valeurs croissantes en 
        commençant par pique, puis coeur, carreau et trèfle. """
        self.contenu = []
        for couleur in range(1, 1+len(['pique', 'coeur', 'carreau', 'trèfle'])):
            for valeur in range(1, 1+len(['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi'])):
                self.contenu.append(Carte(couleur, valeur))


    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        assert pos >= 0 and pos <= 51, 'paramètre pos invalide'
        return self.contenu[pos]
            
        
        
jeu = Paquet_de_cartes()
carte1 = jeu.get_carte(20)
print(carte1.get_valeur() + " de " + carte1.get_couleur())
# '8 de coeur'
carte2 = jeu.get_carte(0)
print(carte2.get_valeur() + " de " + carte2.get_couleur())
# 'As de pique'
try:
    carte3 = jeu.get_carte(52)
except AssertionError: print('Erreur prévue.')
