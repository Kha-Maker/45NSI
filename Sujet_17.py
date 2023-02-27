# Exo 1:
def moyenne(listes_notes: list) -> float:
    total_points = 0
    total_coefficients = 0
    for valeurs in listes_notes:
        note, coefficient = valeurs
        assert isinstance(note, float) or isinstance(note, int), TypeError
        assert note > 0 and note <= 20, ValueError
        assert isinstance(coefficient, int) and coefficient > 0        
        total_points = total_points + note * coefficient
        total_coefficients = total_coefficients + coefficient
    return round(total_points / total_coefficients, 1)


assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5

# Exo 2:
def pascal(n):
    triangle = [[1]]
    for k in range(1, n+1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k-1][i-1] + triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle


assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
