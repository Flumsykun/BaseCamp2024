import sys  # Importing sys to handle command-line arguments


# Define the main function to encapsulate the program logic
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:  # Expect the script name and one filename
        print("Usage: python longestword.py <filename>")
        sys.exit(1)  # Exit with an error status
    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            longest_word = ''  # Initialize a variable to store the longest word
            # Read the file line by line
            for line in file:
                # Split the line into words and iterate over each word
                for word in line.split():
                    # If the current word is longer than the longest_word, update longest_word
                    if len(word) > len(longest_word):
                        longest_word = word
            # Print the longest word found
            print(longest_word)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error reading file: \"{filename}\"")
        sys.exit(1)  # Exit with a status code of 1 to indicate an error
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")
        sys.exit(1)  # Exit with a status code of 1 to indicate an error

print(f"Arguments passed: {sys.argv}")

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
