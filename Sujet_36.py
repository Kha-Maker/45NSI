# Exo 1:
def couples_consecutifs(tab: list) -> list:
    couples = []
    for i in range(len(tab)-1):
        if tab[i]+1 == tab[i+1]:
            couples.append((tab[i], tab[i+1]))
    return couples


assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs ([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

# Exo 2:
def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val
        
    # l'élément en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)
        
    # l'élément en bas fait partie de la composante
    if i+1 < len(M) and M[i+1][j] == 1:
        propager(M, i+1, j, val)
        
    # l'élément à gauche fait partie de la composante
    if j-1 >= 0 and M[i][j-1] == 1:
        propager(M, i, j-1, val)
        
    # l'élément à droite fait partie de la composante
    if j+1 < len(M) and M[i][j+1] == 1:
        propager(M, i, j+1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]