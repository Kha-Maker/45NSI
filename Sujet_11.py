# Exo 1:
def convertir(tab):
    """
    tab est un tableau d'entiers, dont les éléments sont 0 ou 1,
    et représentant un entier écrit en binaire. 
    Renvoie l'écriture décimale de l'entier positif dont la 
    représentation binaire est donnée par le tableau tab
    """
    n = len(tab)-1 # pour aller de n-1 à 0
    r = 0 
    for bin in tab:
        if bin == 1: r += 2**n
        n -= 1
    return r


assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130

# Exo 2:
def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j est utilisée pour déterminer où placer la valeur à insérer
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1 
        tab[j] = valeur_insertion
    return tab # à ajouter bien sur

        
        
liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
assert tri_insertion(liste) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]