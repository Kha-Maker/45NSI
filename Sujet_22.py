# Exo 1:
def liste_puissances(a: int, n: int) -> list:
    assert n > 0, liste_puissances.__annotations__
    l = []
    r = 1
    for i in range(n):
        r *= a
        l.append(r)
    return l


def liste_puissances_borne(a: int, borne: int) -> list:
    if borne <= a: return []
    n = 1
    l = liste_puissances(a, n) # renvoie toujours [a] car n=1
    while l[-1]*a < borne:
        n += 1
        l = liste_puissances(a, n)
    return l


assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]
assert liste_puissances_borne(2, 16) == [2, 4, 8]
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []    

# Exo 2:
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
 "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
 "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
 "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
 "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot) :
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0 :
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

    
    
assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)