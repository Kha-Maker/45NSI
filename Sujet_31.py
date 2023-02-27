# Exo 1:
def nb_repetitions(elt: any, tab:list) -> int:
    n = 0
    for e in tab:
        if e == elt: n += 1
    return n


assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0

# Exo 2:
def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
    
    
assert binaire(0) == '0'
assert binaire(77) =='1001101'
assert binaire(83) == '1010011'
assert binaire(127) == '1111111'