# Exo 1:
def recherche_min(tab: list) -> int:
    min = tab[0]
    indice = 0
    n = len(tab)
    for i in range(n):
        if tab[i] < min: 
            min = tab[i]
            indice = i
    return indice


assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2

# Exo 2:

def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite:
        if tab[gauche] == 0:
            gauche = gauche + 1
        else:
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab


assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]