# Exo 1:
def renverse(chaine: str) -> str:
    r = ''
    for i in range(len(chaine)-1, -1, -1):
        r += chaine[i]
    return r
        
        
assert renverse("informatique") == "euqitamrofni"

# Exo 2:
def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits
    que n
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]