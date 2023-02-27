# Exo 1:
def recherche(a:int, tab:list) -> int:
    n = 0
    for elt in tab:
        if elt == a: n += 1
    return n


assert recherche(5, []) == 0
assert recherche(5, [-2, 3, 4, 8]) == 0
assert recherche(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5, [-2, 5, 3, 5, 4, 5]) == 3

# Exo 2:
pieces = [1, 2, 5, 10, 20, 50, 100, 200]


def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = - somme_due + somme_versee
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else:
            i = i - 1
    return rendu


assert rendu_monnaie(700, 700) == []
assert rendu_monnaie(452, 500) == [20,20,5,2,1]
assert rendu_monnaie(102, 500) == [200, 100, 50, 20, 20, 5, 2, 1]