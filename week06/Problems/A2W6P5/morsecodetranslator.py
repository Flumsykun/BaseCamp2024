# Dictionary to map letters and numbers to Morse code
morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    " ": "   ", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "@": ".--.-.",
    "'": ".----.", "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-"
}

# Reverse dictionary for converting from Morse to text
reverse_morse_code = {v: k for k, v in morse_code.items()}


def message_to_morse(message):
    """Converts a text message to Morse code."""
    morse_code_list = []
    for char in message.upper():
        if char in morse_code:
            morse_code_list.append(morse_code[char])
        else:
            return f"Can't convert char [{char}]"

    # Join Morse code characters for each word with single space, words with triple space
    return ' '.join(morse_code_list)


def morse_to_message(morse_input):
    """Converts Morse code to a text message."""
    words = morse_input.split("   ")  # Split by 3 spaces (words)
    decoded_message = []

    for word in words:
        letters = word.split()  # Split by single space (letters in a word)
        decoded_word = []

        for letter in letters:
            if letter in reverse_morse_code:
                decoded_word.append(reverse_morse_code[letter])
            else:
                return f"Can't convert Morse sequence [{letter}]"

        decoded_message.append("".join(decoded_word))

    # Join decoded words with a single space
    return " ".join(decoded_message)


def translate_text(text):
    """Automatically detects if the input is text or Morse code and translates accordingly."""
    text = text.strip()
    # If the input contains dots or dashes only, treat as Morse
    if all(char in ".- " for char in text):
        return morse_to_message(text)
    else:
        return message_to_morse(text)


if __name__ == "__main__":
    # Interactive user input
    morse_input = input("Enter text or morse code: ")
    morse_result = translate_text(morse_input)
    print(morse_result)
