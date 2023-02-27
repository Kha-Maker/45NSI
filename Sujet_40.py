# Exo 1:
def nombre_de_mots(phrase: str) -> int:
    n = -1 if phrase[-1] == '!' or phrase[-1] == '?' else 0
    phrase = phrase.split(' ')
    n += len(phrase)
    return n 


assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est separe !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10
assert nombre_de_mots('Fin.') == 1

# Exo 2:
class Noeud:
    
    
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    
    
    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée'''
        return self.valeur


    def droitExiste(self):
        '''Méthode renvoyant True si le sous-arbre droit est non 
        vide
        Aucun paramètre en entrée'''
        return (self.droit is not None)


    def gaucheExiste(self):
        '''Méthode renvoyant True si le sous-arbre gauche est non 
        vide
        Aucun paramètre en entrée'''
        return (self.gauche is not None)
    
    
    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de 
        recherche
        Paramètre d'entrée : cle (int)'''
        if cle < self.valeur :
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on recommence le test initial
                self.gauche.inserer(cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur :
            # on insère à droite
            if self.droitExiste() :
                # on descend à droite et on recommence le test initial
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
assert arbre.gauche.getValeur() == 3
assert arbre.droit.getValeur() == 9
assert arbre.gauche.gauche.getValeur() == 1
assert arbre.gauche.droit.getValeur() == 6