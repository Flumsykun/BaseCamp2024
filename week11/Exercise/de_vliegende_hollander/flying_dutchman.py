# 1. Check of dat het de eerste boot is zo niet of er een boot is aangekomen.
# 2. Ga na hoeveel zitplaatsen er beschikbaar zijn.
# 3. Als de boot nog niet leeg is wacht tot de vorige bezoekers vertrekken.
# 4. Vraag aan de nieuwe bezoekers in de rij hoe groot hun groep is in totaal.
# 5. Check of hun groep past in de boot met de helegroep met max 14 plaatsen.
# 6. Als hun aantal minder is dan 14 en de boot is vrij laat ze erin.
# 7. Als de boot vol is stuur de boot weg zo niet check of de volgende groep past in de huidige boot.
# 8. past de volgende groep niet in de huidige boot stuur ze dan naar een nieuwe boot.
# 9. herhaal de vorige stappen tot het einde van je shift.


is_first_boat = True

free_seats_in_boat = 14

group_size = int(input("Enter the group size: "))

if group_size == 0:
    print("No one is coming")
else:
    while group_size > 0:
        if is_first_boat:
            print("First boat")
            is_first_boat = False
        else:
            print("New boat")
        if free_seats_in_boat >= group_size:
            print("Group fits in the boat")
            free_seats_in_boat -= group_size
            group_size = 0
        else:
            print("Group doesn't fit in the boat")
            group_size -= free_seats_in_boat
            free_seats_in_boat = 14

