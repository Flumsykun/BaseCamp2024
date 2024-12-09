def check_comments_from_files():
    files = input("Enter the names of the files (comma-separated): ").split(',')
    for file in files:
        file = file.strip()  # Remove any extra whitespace
        try:
            with open(file, 'r') as f:
                content = f.readlines()
        except FileNotFoundError:
            print(f"Could not open file: {file}")
            continue

        # Check for functions without preceding comments
        for comment, line in enumerate(content):
            if line.strip().startswith("def "):  # Check for function definition
                if comment == 0 or not content[comment - 1].strip().startswith("#"):  # Check preceding line
                    function_name = line.split("(")[0].strip()[4:]  # Extract function name
                    print(
                        f"File: {file} contains a function [{function_name}()] on line [{comment + 1}] without a preceding comment.")


if __name__ == "__main__":
    check_comments_from_files()
