# Exo 1:
def recherche(elt: int, tab: list) -> int:
    """
    Fonction qui renvoie l'indice de la première occurence du nombre entier elt dans la liste tab. 
    Si elt n'existe pas dans tab, alors -1 est renvoyé 
    """
    n = len(tab)
    for i in range(n):
        if elt == tab[i]:
            return i
    return -1
    

assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 1
assert recherche(50, []) == -1
assert recherche(4, [2, 4, 4, 3, 4]) == 1

# Exo 2:
class AdresseIP:
    
    
    def __init__(self, adresse):
        self.adresse = adresse


    def liste_octet(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 


    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        return self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255'


    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
        IP qui suit l’adresse self
        si elle existe et False sinon"""
        if self.liste_octet()[-1] < 254:
            octet_nouveau = self.liste_octet()[-1]+1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False
        

adresse1, adresse2, adresse3 = AdresseIP('192.168.0.1'), AdresseIP('192.168.0.2'), AdresseIP('192.168.0.0')

assert adresse1.est_reservee() == False
assert adresse3.est_reservee() == True
assert adresse2.adresse_suivante().adresse == '192.168.0.3'