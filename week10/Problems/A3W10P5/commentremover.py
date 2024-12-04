# Read the File name (input handling)
# prompt the user to enter the name of the file to be cleaned
# handle errors if the file doesn't exist
def remove_comments_from_file():
    file = input("Enter the name of the file: ")
    try:
        with open(file, 'r') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"File: Could not open file: {file}")
        return



    # Step 3: Remove comments and store cleaned lines

    cleaned_content = []
    for line in content:
        if '#' in line:
            line = line.split('#')[0].rstrip()  # Remove comment and trailing spaces
        if line.strip():  # Skip empty lines
            cleaned_content.append(line + '\n')  # Add line break for writing

    # print a message to the user
    # to indicate that the file has been cleaned

    print("File cleaned successfully.")

    # write the cleaned content to a new file
    # prompt the user to enter the name of the new file,
    # where the cleaned content should be saved
    # open this file in write mode
    # write the cleaned content to the file

    new_file = input("Enter the name of the new file: ")
    try:
        with open(new_file, 'w') as f:
            f.writelines(cleaned_content)
            print("File saved successfully.")
    except IOError:
        print(f"Error saving file: \"{new_file}\"")

    if __name__ == "__main__":
        remove_comments_from_file()
