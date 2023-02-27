# Exo 1:
def mini(releve: list, date: list) -> tuple:
    n = len(releve)
    index = 0
    min = releve[0]
    for i in range(1, n):
        if releve[i] < min:
            min = releve[i]
            index = i
    return min, date[index]


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

assert mini(t_moy, annees) == (12.5, 2016)

# Exo 2:
def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
        result = caractere + result
    return result


def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse
 
 
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


assert inverse_chaine('bac') =='cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True
