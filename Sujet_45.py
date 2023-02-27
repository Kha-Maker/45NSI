# Exo 1:
def rangement_valeurs(notes_eval: list) -> list:
    r = [0]*11 # liste de longueur 11
    for i in range(len(notes_eval)):
        r[notes_eval[i]] += 1 # L'indice correspond à la note dans r
    return r


def notes_triees(effectifs_notes: list) -> list:
    r = []
    for note in range(11):
        for _ in range(effectifs_notes[note]):
            r.append(note)
    return r
    
    
notes_eval =[2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
effectifs_notes = rangement_valeurs(notes_eval)
assert effectifs_notes == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
assert notes_triees(effectifs_notes) == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]

# Exo 2:
def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit


assert dec_to_bin(25) == '11001'
assert bin_to_dec('11001') == 25

assert bin_to_dec('101010') == 42
assert dec_to_bin(42) == '101010'