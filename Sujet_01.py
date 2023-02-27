# Exo 1:
def verifie(tab: list) -> bool:
    """ 
    Compare la liste tab à une liste triée contenant les mêmes éléments.
    """
    n = len(tab)
    if n <= 1: return True
    # Tri à bulles 
    listT = [e for e in tab]
    for i in range(n):
        for j in range(i+1, n):
            if listT[i] > listT[j]:
                # Pour inverser les valeurs numériques sans variable intermédiaire
                listT[i] += listT[j] 
                listT[j] = listT[i] - listT[j]
                listT[i] -= listT[j]
                
    return tab == listT
    

def verifie(tab: list) -> bool:
    """
    Version récursive proposée par:
    Karim Hellali Terminale 1
    """
    if len(tab) <= 1: return True
    if tab[0] <= tab[1]: return verifie(tab[1:])
    else: return False


assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True

# Exo 2:
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']


def depouille(urne):
    resultat = {
      'A': 0,
      'B': 0,
      'C': 0
      }
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat


def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
    
    
election = depouille(urne)
print(election)
# {'B': 4, 'A': 3, 'C': 3}
print(vainqueur(election))
# ['B']