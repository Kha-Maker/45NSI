def moyenne(tab: list):
    '''
    moyenne(list) -> float
    Entrée : un tableau d'entiers
    Sortie : nombre de type float 
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    ''' 
    assert tab != [], 'La liste en argument est vide'
    return sum(tab)/len(tab)


assert moyenne([5, 3, 8]) == 5.333333333333333
assert moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
try: moyenne([])
except AssertionError: print("Erreur prévue.")

# Exo 2:
def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée. 
    # Au début, la zone non triée est le tableau complet.
    i = 0
    j = len(tab) - 1 
    while i != j :
        if tab[i] == 0:
            i = i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab


assert tri([0, 1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 0, 1, 1, 1, 1]
assert tri([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert tri([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]