# Write a function is_integer that takes a string as input and returns True if the string represents an integer, and False otherwise. An integer is a string that contains only digits (0-9) and may have leading and trailing white spaces. For example, "123", " 123", "123 ", and " 123 " are all integers, but "123.0", "123 456", and "123abc" are not. You may assume that the input string is not empty.
def is_integer(unchecked: str) -> bool:
    # Remove leading and trailing white spaces
    unchecked = unchecked.strip()

    # check if the string is a valid integer
    if len(unchecked) == 0:
        return False
    # Check if the string contains only digits
    if unchecked[0] in ('+', '-') and unchecked[1:].isdigit():
        return True
    if unchecked.isdigit():
        return True
    return False


def remove_non_integer(unchecked: str) -> int:
    # Remove non-digit characters
    result = ''.join(
        [char for char in unchecked if char.isdigit() or char in ('+', '-')])
    # Ensure the result is a valid integer
    return int(result)


if __name__ == "__main__":
    # Test for is_integer function
    string = input("Enter a string: ")
    if is_integer(string):
        print("Valid integer")
    else:
        print("Invalid integer")

    # Test for remove_non_integer function
    string_with_chars = input("Enter a mixed string: ")
    print(f"Processed integer: {remove_non_integer(string_with_chars)}")
