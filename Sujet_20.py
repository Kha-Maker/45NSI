# Exo 1:
def ajoute_dictionnaires(d1: dict, d2: dict) -> dict:
    d3 = {}
    for key in list(d1.keys()) + list(d2.keys()):
        d3[key] = d1.get(key, 0) + d2.get(key, 0)
        """
        Documentation of .get(__key, __default)
        Return the value for key if key is in the dictionary, else default.
        """
    return d3


assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}

# Exo 2:
from random import randint


def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1 
    return n


# Tester sur https://pythontutor.com/python-debugger.html