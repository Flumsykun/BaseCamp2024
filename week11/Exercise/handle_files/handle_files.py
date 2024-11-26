# Read the file file.txt using the open function
# and return the contents of that file as a string
def read_file_using_open() -> str:
    txtfile = open("file.txt")
    contents = txtfile.read()
    txtfile.close()
    return contents


# Read the file file.txt using the with statement
# and return the contents of that file as a string
def read_file_using_with() -> str:
  with open ("file.txt") as txtfile:
    contents = txtfile.read()
    return contents

# Read the file file.txt using the with statement
# and return the second line of that file
def read_second_line() -> str:
    with open ("file.txt") as txtfile:
        txtfile.readline()
        return txtfile.readline()


# Read the file file.txt using the with statement
# and return the second line of that file without the new line character
def read_second_line_without_new_line() -> str:
    with open("file.txt") as txtfile:
        txtfile.readline()
        return txtfile.readline().strip()


# Read the file file.txt using the with statement
# and read all the lines with a for loop
# and return the lines in a list
def read_lines_using_for_loop() -> list:
    lines = []
    with open("file.txt") as txtfile:
        for line in txtfile:
            lines.append(line)
        return lines



# Read the file file.txt using the with statement
# and the readlines function
# and return the lines in a list
def read_lines_using_readlines() -> list:
    lines = []
    with open("file.txt") as txtfile:
        lines = txtfile.readlines()
        return lines


# Create the file newfile.txt using the with statement
# and write the string line to that file
def write_line_to_a_file(line: str) -> None:
    with open ("newfile.txt", "w") as outputfile:
        outputfile.write(line)
        outputfile.close()


# Create the file newfile.txt using the with statement
# and write the strings in the list lines to that file
# Don't forget to seperate the lines with a new line character
def write_lines_to_a_file(lines: list) -> None:
    with open ("newfile.txt", "w") as outputfile:
        outputfile.write("\n".join(lines))
        outputfile.close()

# Append the string line to the file newfile.txt
# using the with statement
def add_line_to_a_file(line: str) -> None:
    with open ("newfile.txt", "a") as outputfile:
        outputfile.write(line)
