# Define your lists for gifts and ordinal numbers
gifts = [
    "A partridge in a pear tree",
    "Two turtledoves",
    "Three French hens",
    "Four calling birds",
    "Five gold rings (five golden rings)",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming"
]

ordinals = [
    "1st", "2nd", "3rd", "4th", "5th",
    "6th", "7th", "8th", "9th", "10th",
    "11th", "12th"
]


def next_verse(day):
    if day < 1 or day > 12:
        return "Invalid day"

    verse = f"On the {ordinals[day - 1]} day of Christmas, my true love sent to me "

    # Add gifts in reverse order for the given day, starting from the current day
    if day == 1:
        verse += "A partridge in a pear tree"
    else:
        verse += ", ".join(gifts[day-1:0:-1]) + " And " + gifts[0]

    return verse


def all_verses():
    return "\n\n".join(next_verse(i) for i in range(1, 13))


# Example usage
if __name__ == "__main__":
    print(next_verse(3))  # Check the output for the 2nd day
    print(all_verses())    # Check the output for all verses
