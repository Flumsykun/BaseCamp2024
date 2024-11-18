import sys  # Import the sys module to access command-line arguments


def main():
    """
    The main function that handles reading the file and printing the first 10 lines.
    """
    # Step 1: Check if the correct number of arguments is provided
    if len(sys.argv) != 2:  # Expect exactly one argument after the script name
        # If not, print the usage message and exit
        print("Usage: python3 head.py <filename>")
        sys.exit(1)  # Exit with a status of 1 to indicate an error

    # Step 2: Get the filename from the command-line arguments
    filename = sys.argv[1]  # The filename is the second argument (index 1)

    # Step 3: Open the file and handle potential errors
    try:
        # Use a context manager to open the file in read mode
        with open(filename, 'r') as file:
            # Step 4: Read and print the first 10 lines
            # Enumerate provides the line number (i) and the line content (line)
            for i, line in enumerate(file):
                if i >= 10:  # Stop reading after 10 lines
                    break
                # Print the line, stripping any extra whitespace (like newlines)
                print(line.strip())

    # Step 5: Handle errors gracefully
    except FileNotFoundError:  # If the file doesn't exist
        # Print an error message and exit
        print(f"Error reading file: \"{filename}\"")
        sys.exit(1)  # Exit with a status of 1 to indicate an error
    except Exception as e:  # Catch any other unexpected errors
        # Print the error message and exit
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with a status of 1 to indicate an error


# This ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
