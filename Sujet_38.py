# Exo 1:
def correspond(mot: str, mot_a_trous: str) -> bool:
    n1 = len(mot)
    n2 = len(mot_a_trous)
    if n1 != n2: return False
    for i in range(n1):
        if mot_a_trous[i] == '*':
            continue
        elif mot_a_trous[i] != mot[i]:
            return False
    return True


assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False
assert correspond('AUTO', '*UT*') == True

# Exo 2:
def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant à un 
    plan d'envoi de messages (ici entre les personnes A, B, C, D, 
    E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1
    return nb_destinaires == len(plan)


assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}) == False
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F','D':'A'}) == True
assert est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}) == True
assert est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}) == False
