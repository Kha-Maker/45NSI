# Exo 1:
class ABR:
    
    
    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0
        
        
    def afficher(self) -> tuple:
        g = self.gauche.afficher() if isinstance(self.gauche, ABR) else None
        r = self.cle
        d = self.droit.afficher() if isinstance(self.droit, ABR) else None
        return g, r, d


    def __str__(self) -> str:
        return str(self.afficher())
    
    
    def __repr__(self) -> str:
        return str(self.afficher())
        

n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)


def ajoute(cle: int, a: ABR) -> ABR:
    if a.cle < cle:
        return ABR(a.gauche, a.cle, ajoute(cle, a.droit) if isinstance(a.droit, ABR) else ABR(None, cle, None))
    elif a.cle > cle: # 
        return ABR(ajoute(cle, a.gauche) if isinstance(a.gauche, ABR) else ABR(None, cle, None), a.cle, a.droit)
    else:
        return ABR(a.gauche, a.cle, a.droit)
    

a = ajoute(4, abr1)
assert a.afficher() == ((None,0,None),1,(None,2,(None,3,(None,4,None))))
assert ajoute(-5, abr1).afficher() == (((None,-5,None),0,None),1,(None,2,(None,3,None)))
assert ajoute(2, abr1).afficher() == ((None,0,None),1,(None,2,(None,3,None)))

# Exo 2:
def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses :
        i = 0
        while i <= nb_boites and boites[i] + masse > c: # Mettre c en minuscule
            i = i + 1
        if i == nb_boites + 1:
            nb_boites = i
        boites[i] = boites[i] + masse # Indenter cette ligne
    return nb_boites + 1 # Car i donne l'indice de la dernière boite qui contient une masse 


assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5
assert empaqueter([3, 5, 2], 5) == 2 
