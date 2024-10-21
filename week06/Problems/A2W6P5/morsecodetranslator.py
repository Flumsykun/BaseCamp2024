# Dictionary to map letters and numbers to Morse code
morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", " ": "  ", "a": ".-", "b": "-...", "c": "-.-.",
    "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "@": ".--.-.",
    "#": ".-.-. # .-.-.",  # Use "#" for "#"
    "$": "...-..-",
    "%": ".-..-.",
    "&": ".-... .",
    "(": "-.--.",
    ")": "-.--.-",
    "_": "..--.-",
    "+": ".-.-.",
    "-": "-....-",
    "=": "-...-",
    "<": ".-..-.",
    ">": "--.-.",
    "/": "-.-.-.",
    "`": ".-.--",
    "'": ".--.",
}

# Reverse dictionary for converting from Morse to text
reverse_morse_code = {v: k for k, v in morse_code.items()}


def message_to_morse(message):
    morse_code_list = []
    for char in message.lower():
        if char in morse_code:
            # print(f"Adding Morse code for {char}: {morse_code[char]}")
            morse_code_list.append(morse_code[char])
        else:
            return f"Can't convert char [{char}]"
    return ' '.join(morse_code_list)


def morse_to_message(morse_input):
    words = morse_input.split("    ")  # 4 spaces between Morse code words
    decoded_message = []
    for word in words:
        letters = word.split()  # Split by single space between Morse letters
        decoded_word = []
        for letter in letters:
            if letter in reverse_morse_code:
                decoded_word.append(reverse_morse_code[letter])
            else:
                return f"Can't convert Morse sequence [{letter}]"
        decoded_message.append("".join(decoded_word))
    return " ".join(decoded_message)  # Ensure proper spacing between words


def translate_text(input_text):
    """Automatically detects if the input is text or Morse code and translates accordingly."""
    input_text = input_text.strip()
    # If the input contains dots or dashes only, treat as Morse
    if all(char in ".- " for char in input_text):
        return morse_to_message(input_text)
    else:
        return message_to_morse(input_text)


if __name__ == "__main__":
    # Interactive user input
    user_input = input("")
    user_result = translate_text(user_input)
    print(user_result)  # Print the result directly without additional prompts
