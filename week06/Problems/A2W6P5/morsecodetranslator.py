morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", " ": "   ", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", "-": "-....-", "=": "-...-", "+": ".-.-.", "@": ".--.-.",
    ":": "---...", ";": "-.-.-.", '"': ".-..-.", "$": "...-..-", "_": "..--.-"
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


def morse_to_message(morse_input):
    """Converts Morse code to a text message."""
    reverse_morse_code = {
        v: k for k, v in morse_code.items()}  # Reverse the Morse code dictionary
    message_list = []
    words = morse_input.split('   ')  # Words are separated by 3 spaces

    for word in words:
        chars = word.split(' ')  # Characters are separated by 1 space
        message_list.append(
            ''.join(reverse_morse_code.get(char, '') for char in chars))

    return ' '.join(message_list)


def translate_text(text):
    """Translates text to or from Morse code based on its format."""
    if all(c in '.- ' for c in text):  # If text only contains Morse code characters
        return morse_to_message(text)
    else:
        return message_to_morse(text)


if __name__ == "__main__":
    morse_text = input("Enter text or morse code: ")
    result = translate_text(morse_text)
    print(result)
