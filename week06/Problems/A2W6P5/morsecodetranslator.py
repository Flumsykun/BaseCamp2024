def message_to_morse(message):
    """Converts a text message to Morse code."""
    morse_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        "0": "-----", " ": "   ",  # 3 spaces for word separation
        "?": "..--..", ",": "--..--", ".": ".-.-.-", "!": "-.-.--",  # Punctuation
        "'": ".----.", "-": "-....-", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
        "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
        "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-."
    }

    morse_code = []

    for char in message.upper():
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            return f"Can't convert char [{char}] if there is no mapping for specific characters."

    return ' '.join(morse_code)


def morse_to_message(morse_code):
    """Converts Morse code to a text message."""
    morse_dict = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
        "-----": "0", "..--..": "?", "--..--": ",", ".-.-.-": ".", "-.-.--": "!",
        "   ": " "  # 3 spaces for word separation
    }

    message = []
    words = morse_code.split('   ')  # Split by 3 spaces (word separator)

    for word in words:
        chars = word.split(' ')  # Split by single spaces (character separator)
        message.append(''.join(morse_dict.get(char, '') for char in chars))

    return ' '.join(message)


def translate_text(text, direction="to_morse"):
    """Translates text to or from Morse code."""
    if direction == "to_morse":
        return message_to_morse(text)
    elif direction == "from_morse":
        return morse_to_message(text)
    else:
        raise ValueError(
            "Invalid direction. Choose 'to_morse' or 'from_morse'.")


if __name__ == "__main__":
    # For testing purposes, we remove interactive input and provide example cases
    test_cases = [
        ("Hello World", "to_morse"),
        (".... . .-.. .-.. ---    .-- --- .-. .-.. -..", "from_morse"),
        ("SOS? Yes, or no.", "to_morse"),
        ("... --- ... ..--..    -.-- . ... --..--    --- .-.    -. --- .-.-.-", "from_morse"),
    ]

    for text, direction in test_cases:
        result = translate_text(text, direction)
        print(f"Input: {text} | Direction: {direction} | Output: {result}")
