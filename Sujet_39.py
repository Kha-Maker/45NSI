# Exo 1:
def fibonacci(n: int):
    if n <= 1: return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(8) == 21

# Exo 2:
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(eleves)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]] 
    return (note_maxi, meilleurs_eleves)

    
eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert pantheon(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
assert pantheon([],[]) == (0, [])