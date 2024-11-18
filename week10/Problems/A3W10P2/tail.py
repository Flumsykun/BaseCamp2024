import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tail.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines[-10:]:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error reading file: \"{filename}\"")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


# This ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
