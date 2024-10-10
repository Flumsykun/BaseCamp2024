def is_integer(unchecked: str) -> bool:
    """Checks if the string represents an integer."""
    # Remove leading and trailing whitespaces
    unchecked = unchecked.strip()

    # Check if empty string or starts with +, -, followed by digits
    if len(unchecked) == 0 or (unchecked[0] in ('+', '-') and unchecked[1:].isdigit()):
        return False

    # Check if the string contains only digits
    return unchecked.isdigit()


def remove_non_integer(unchecked: str) -> int:
    """Removes non-integer characters and returns the integer."""
    # Remove non-digit characters
    cleaned_result = ''.join(
        char for char in unchecked if char.isdigit() or char in ('+', '-'))

    # Ensure the result is a valid integer (handles leading +/-)
    if cleaned_result:
        return int(cleaned_result)
    else:
        return 0  # Return 0 for empty string or invalid input


if __name__ == "__main__":
    # Test for is_integer function
    integer = input("Enter a integer: ")
    if is_integer(integer):
        print("valid")
    else:
        print("invalid")

    # Test for remove_non_integer function
    # string_with_chars = input("Enter a mixed string: ")
    # print(f"Processed integer: {remove_non_integer(string_with_chars)}")
