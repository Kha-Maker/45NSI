# Exo 1:
def moyenne (tab: list):
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float 
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    ''' 
    return sum(tab)/len(tab)


assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335

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