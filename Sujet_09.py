# Exo 1:
def multiplication(n1: int, n2: int) -> int:
    r = 0
    if n2 == 0:
        return r
    if n2 > 0:
        for _ in range(n2):
            r += n1
    if n2 < 0:
        for _ in range(-n2):
            r -= n1
    return r


assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0
assert multiplication(0, -2) == 0

# Exo 2:
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None 
    elif i > j: 
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m
 

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2
