# Exo 1:
def recherche(tab: list, n: int) -> int:
    g = 0
    d = len(tab)-1
    while d-g >= 0:
        m = (d+g) // 2  # Calcul du milieu
        if tab[m] == n:
            return m
        elif tab[m] > n:
            d = m-1
        else:
            g = m+1    
    return -1


assert recherche([2, 3, 5, 6, 7], 5) == 2
assert recherche([2, 3, 4, 6, 7], 5) == -1
assert recherche([5, 7, 8, 9], 5) == 0
assert recherche([2, 3, 4, 5], 5) == 3

# Exo 2:
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat


assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)  == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'