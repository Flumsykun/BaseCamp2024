def message_to_morse(message):
    morse_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        "0": "-----", " ": "   "  # 3 spaces for separating words
    }

    morse_code = ""
    unsupported_chars = []

    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + " "
        else:
            unsupported_chars.append(char)

    if unsupported_chars:
        return f"Can't convert char(s) {', '.join(unsupported_chars)} if there is no mapping for specific characters."

    return morse_code.strip()


if __name__ == "__main__":
    message = input("Enter a message: ")
    print(message_to_morse(message))
