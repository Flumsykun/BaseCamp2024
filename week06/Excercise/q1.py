from salesdata import sales

# Hoeveel puzzels "Vierkant NL 1.0" heb ik verkocht?
# Gewenste uitvoerformaat:
# 50 Vierkant NL 1.0 verkocht


puzzle = "Vierkant NL 1.0"
count = 0
for sale in sales:
    if sale[1] == puzzle:
        count += sale[0]

print(f"{count} {puzzle} verkocht")
