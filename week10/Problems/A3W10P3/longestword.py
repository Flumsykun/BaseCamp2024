import sys  # Import sys to handle command-line arguments


def main():
    # Check if the correct number of arguments is provided
    # if len(sys.argv) != 2:
    #     print("Usage: python longestword.py <filename>")
    #     sys.exit(1)
    #
    # filename = sys.argv[1]  # Get the filename from the arguments
    # print(f"Processing file: \"{filename}\"")

    # Get the filename from the command-line arguments
    filename = input("")
    try:
        # Open the file and process it
        with open(filename, 'r') as file:

            longest_length = 0  # Track the length of the longest word
            longest_words = []  # List to store words with the longest length

            # Read the file line by line
            for line in file:
                # Split the line into words based on whitespace
                for word in line.split():
                    # No regex, but punctuation and numbers are kept as part of the word
                    word = word.strip()  # Remove extra whitespace around the word
                    word_length = len(word)
                    if word_length > longest_length:
                        longest_length = word_length
                        longest_words = [word]
                    elif word_length == longest_length:
                        longest_words.append(word)

        # Print results
        print(f"Length of longest word(s) is [{longest_length}] chars")
        print("These are all the words of that length:")
        print(", ".join(longest_words))

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error reading file: \"{filename}\"")
        # sys.exit(1)


# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()