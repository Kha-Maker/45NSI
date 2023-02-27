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
assert recherche(15, [8, 9, 10, 15]) == 3
assert recherche(50, []) == -1
assert recherche(4, [2, 4, 4, 3, 4]) == 1

# Exo 2:
def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau. """
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab)-1
    while a < l[i] and i >= 0: 
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l


assert insere(3, [1, 2, 4, 5]) == [1, 2, 3, 4, 5]
assert insere(30, [1, 2, 7, 12, 14, 25]) == [1, 2, 7, 12, 14, 25, 30]
assert insere(1, [2, 3, 4]) == [1, 2, 3, 4]
assert insere(1, []) == [1]