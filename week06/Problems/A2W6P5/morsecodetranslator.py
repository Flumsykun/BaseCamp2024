morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", " ": "   "  # 3 spaces for word separation
}


def message_to_morse(message):
    """Converts a text message to Morse code."""
    morse_code_list = []
    for char in message.upper():
        if char in morse_code:
            morse_code_list.append(morse_code[char])
        else:
            return f"Can't convert char [{char}] if there is no mapping for specific characters."
    return ' '.join(morse_code_list)


def morse_to_message(morse_code):
    """Converts Morse code to a text message."""
    morse_code_dict = {value: key for key, value in morse_code.items()}
    message_list = []
    words = morse_code.split('   ')
    for word in words:
        chars = word.split(' ')
        message_list.append(''.join(morse_code_dict.get(char, '')
                            for char in chars))
    return ' '.join(message_list)


def translate_text(text):
    """Translates text to or from Morse code based on its format."""
    if text.isalpha():
        return message_to_morse(text)
    elif all(char in morse_code.values() or char == ' ' for char in text):
        return morse_to_message(text)
    else:
        return "Invalid input. Please enter a text message or Morse code."


if __name__ == "__main__":
    text = input()
    result = translate_text(text)
    print(result)
