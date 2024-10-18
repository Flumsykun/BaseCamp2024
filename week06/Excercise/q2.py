from salesdata import sales

# Hoeveel puzzels heb ik verkocht van verschillende types?
# Gewenste uitvoerformaat:
# 17 Vierkant NL 0.9 verkocht
# 50 Vierkant NL 1.0 verkocht
# 40 Vierkant NL 1.1 verkocht

puzzles = {}
for count, name, _ in sales:
    if name not in puzzles:
        puzzles[name] = 0
    puzzles[name] += count

count = 0

for puzzle in puzzles:
    print(f"{puzzles[puzzle]} {puzzle} verkocht")
