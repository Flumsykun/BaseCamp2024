students = [
    {"number": "1075356", "firstname": "Abdulhameed",
        "surname": "Ahmad", "day": 5, "month": 6, "year": 1996},
    {"number": "1112338", "firstname": "Budi",
        "surname": "Waskito", "day": 6, "month": 7, "year": 2005},
    {"number": "0949275", "firstname": "Kira",
        "surname": "Jesus Gomes, de", "day": 11, "month": 3, "year": 2000},
    {"number": "2401592", "firstname": "Semih",
        "surname": "Küçük", "day": 11, "month": 2, "year": 2005},
    {"number": "1100080", "firstname": "Sten",
        "surname": "Nierop", "day": 26, "month": 10, "year": 2004},
    {"number": "1111303", "firstname": "Jamil",
        "surname": "Ree, van de", "day": 29, "month": 8, "year": 2003},
    {"number": "1102004", "firstname": "Sem",
        "surname": "Roeten", "day": 15, "month": 7, "year": 2006},
    {"number": "1096116", "firstname": "Rover",
        "surname": "Rot", "day": 14, "month": 3, "year": 2005},
    {"number": "1095917", "firstname": "Youri",
        "surname": "Schmitz", "day": 17, "month": 9, "year": 2006},
    {"number": "1089791", "firstname": "Krista",
        "surname": "Tauriņa", "day": 13, "month": 12, "year": 2005},
    {"number": "1099108", "firstname": "Salih",
        "surname": "Tokur", "day": 9, "month": 10, "year": 2001},
    {"number": "1105408", "firstname": "Lean",
        "surname": "Vreeswijk, van", "day": 29, "month": 11, "year": 2006},
    {"number": "1111300", "firstname": "Sivan",
        "surname": "Zechiel", "day": 6, "month": 5, "year": 2006},
    {"number": "1102086", "firstname": "Andi",
        "surname": "Zeng", "day": 20, "month": 11, "year": 2007},
]


def print_people(people):
    """Print a list of people."""
    for person in people:
        number_and_name = (
            f"{person['number']:7s} {person['firstname']:11s} {person['surname']:16s}"
        )
        date_of_birth = f"{person['day']:02d}-{person['month']:02d}-{person['year']:4d}"
        print(number_and_name, date_of_birth)
    print("-" * 47)


# 1. Sorteer de lijst met studenten
#    Tip: gebruik de functie `sort()`

# students.sort(key=lambda student: student['number'])
# print_people(students)


# 2. Waarom lukt dat niet?


# 3. Sorteer de studenten op nummer en print de lijst
#    Tip 1: maak eerst een functie `number(student)` die het nummer van een student teruggeeft
#    Tip 2: geef die functie mee als waarde voor de parameter `key`

students.sort(key=lambda student: student['number'])
print("Nummer:")
print_people(students)


# 4. Sorteer de studenten op nummer en print de lijst
#    Tip: gebruik een anonieme functie (`lambda`)

# 5. Sorteer de studenten op voornaam
students.sort(key=lambda student: student['firstname'])
print("Voornaam:")
print_people(students)

# 6. Sorteer de studenten op voornaam vanaf de tweede letter
students.sort(key=lambda student: student['firstname'][1:])
print("Voornaam vanaf de tweede letter:")
print_people(students)

# 7. Sorteer de studenten op omgekeerde voornaam
students.sort(key=lambda student: student['firstname'][::-1])
print("Omgekeerde voornaam:")
print_people(students)

# 8. Sorteer de studenten op leeftijd
students.sort(key=lambda student: student['year'])
print("Leeftijdslijst:")
print_people(students)

# 9. Sorteer de studenten op verjaardag (een verjaardagskalender)
students.sort(key=lambda student: (student['month'], student['day']))
print("Verjaardagskalender:")
print_people(students)

# 10. Maak een lijst studenten die in de zomervakantie jarig zijn (juli en augustus)
#     Tip: gebruik de functie `filter()` met een anonieme functie

holiday_students = filter(lambda student: 7 <= student['month'] <= 8, students)
print("Zomervakantie studenten:")
print_people(holiday_students)

# 11. Schrijf een functie `my_filter(func, iterable)` die hetzelfde doet als de functie `filter()`


def my_filter(func, iterable):
    """Filter the items in the iterable for which the function func is True."""
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


holiday_students = my_filter(
    lambda student: 7 <= student['month'] <= 8, students)
print("Zomervakantie studenten:")
print_people(holiday_students)

# 12. Maak een lijst met studenten die dit jaar al jarig zijn geweest
students_already_birthday = filter(
    lambda student: (student['month'], student['day']) < (10, 17),
    students
)
print("Studenten die dit jaar al jarig zijn geweest:")
print_people(students_already_birthday)

# 13. Maak een lijst met alle voornamen
#     Tip: gebruik de functie `map()` met een anonieme functie
firstnames = list(map(lambda student: student['firstname'], students))
print("Alle voornamen:")
print(firstnames)


# 14. Schrijf een functie `my_map(func, iterable)` die hetzelfde doet als de functie `map()`
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

firstnames = my_map(lambda student: student['firstname'], students)
print("Alle voornamen:")
print(firstnames)

# 15. (Bonus) Maak een lijst met alle volledige namen
#     Tip 1: gebruik de functie `map()` met een wat complexere functie
#     Tip 2: om de achternaam goed te krijgen, kun je die splitsen op een komma,
#            het tuple omdraaien en dat omgedraaide tuple weer `join()`en met een spatie
