# Exo 1:
def ecriture_binaire_entier_positif(n: int) -> list:
    binaire = [n % 2]
    n = n // 2
    while n > 0:
        binaire.insert(0, n % 2)
        n = n // 2
    return binaire


assert ecriture_binaire_entier_positif(0) == [0]
assert ecriture_binaire_entier_positif(2) == [1, 0]
assert ecriture_binaire_entier_positif(105) == [1, 1, 0, 1, 0, 0, 1]

# Exo 2:
def tri_bulles(T):
    '''
    Renvoie le tableau T trié par ordre croissant
    '''
    n = len(T)
    for i in range(n-1, -1,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

    
assert tri_bulles([]) == []
assert tri_bulles([7]) == [7]
assert tri_bulles([9, 3, 7, 2, 3, 1, 6]) == [1, 2, 3, 3, 6, 7, 9]
assert tri_bulles([9, 7, 4, 3]) == [3, 4, 7, 9]