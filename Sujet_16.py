# Exo 1:
def recherche_indices_classement(elt: int, tab: list):
    inf, ega, sup = [], [], []
    n = len(tab)
    for index in range(n):
        if tab[index] < elt: inf.append(index)
        elif tab[index] > elt: sup.append(index)
        else: ega.append(index)
    return inf, ega, sup


assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])
  
# Exo 2:
resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]},
    'Durand': {
        'DS1': [6 , 4],
        'DM1': [14.5, 1],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [8, 4],
        'DS4':[15, 4]}}


def moyenne(nom, dico_result):
    if nom in dico_result.keys():
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1
    

assert moyenne('Durand', resultats) == round((6*4+14.5+8*4+9*3+7*2+8*4+15*4)/(4+1+4+3+2+4+4), 1)
