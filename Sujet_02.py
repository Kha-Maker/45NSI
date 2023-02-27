# Exo 1:
def indices_maxi(tab: list) -> tuple:
    max = tab[0]
    indices = []
    n = len(tab)
    for i in range(n):
        if tab[i] == max:
            indices.append(i)
        if tab[i] > max: 
            max = tab[i]
            indices = [i]
            
    return max, indices


assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])

# Exo 2:
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1


assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert  positif([-2]) == []