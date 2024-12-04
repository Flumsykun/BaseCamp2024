def remove_comments_from_file():
    file = input("Enter the name of the file: ")
    try:
        with open(file, 'r') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"Could not open file: {file}")  # Updated error message
        return

    cleaned_content = []
    for line in content:
        if '#' in line:
            line = line.split('#')[0].rstrip()
        if line.strip():
            cleaned_content.append(line + '\n')

    print("File cleaned successfully.")

    new_file = input("Enter the name of the new file: ")
    try:
        with open(new_file, 'w') as f:
            f.writelines(cleaned_content)
            print("File saved successfully.")
    except IOError:
        print(f"Error saving file: {new_file}")


if __name__ == "__main__":
    remove_comments_from_file()