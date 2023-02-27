# Exo 1:
def max_et_indice(tab: list) -> tuple:
    """
    Fonction qui renvoie un couple contenant la valeur maximale de la liste tab et l'indice de sa première occurrence dans tab. 
    """
    max = tab[0]
    indice = 0
    n = len(tab)
    for i in range(n):
        if tab[i] > max: 
            max = tab[i]
            indice = i
    return max, indice


assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)

# Exo 2:
def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les 
    entiers de 1 à n, False sinon
    '''
    for i in range(1, len(tab)):
        if i not in tab:
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n-1:
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb


assert est_un_ordre([1, 6, 2, 8, 3, 7]) == False
assert est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]) == True
assert nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]) == 4
assert nombre_points_rupture([1, 2, 3, 4, 5]) == 0
assert nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]) == 7
assert nombre_points_rupture([2, 1, 3, 4]) == 2