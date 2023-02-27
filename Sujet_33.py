# Exo 1:
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
    'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
    'H':['','']}


def taille(a: dict, lettre: str) -> int:
    tg = taille(a, a[lettre][0]) if a[lettre][0] != '' else 0
    td = taille(a, a[lettre][1]) if a[lettre][1] != '' else 0
    return 1 + tg + td
    
assert taille(a, 'F') == 9

# Exo 2:
def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(imin + 1, N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]


liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
assert liste == [6, 12, 18, 21, 25, 41, 55]