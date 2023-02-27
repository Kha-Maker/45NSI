# Exo 1:
def tri_selection(tab: list):
    for i in range(len(tab)-1):
        imin = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[imin]:
                imin = j
        tab[i], tab[imin] = tab[imin], tab[i]
    return tab
            

l = [1, 52, 6, -9, 12]
assert tri_selection(l) == [-9, 1, 6, 12, 52]

# Exo 2:
from random import randint
def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0
    
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur+1)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)
        

plus_ou_moins()