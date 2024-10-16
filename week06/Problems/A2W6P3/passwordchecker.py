def is_valid_password(password):
    # Define the sets for valid characters
    digits = set("0123456789")
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_symbols = set("*@!?")

    # Convert the password into a set for comparison
    password_set = set(password)

    # Check if the password length is within the required range
    if len(password) < 8 or len(password) > 20:
        return False

    # Check if the password contains at least one digit, one lowercase, one uppercase, and one special symbol
    if not (password_set & digits):
        return False
    if not (password_set & lowercase):
        return False
    if not (password_set & uppercase):
        return False
    if not (password_set & special_symbols):
        return False

    # Check for any invalid characters in the password
    valid_characters = digits | lowercase | uppercase | special_symbols
    for char in password:
        if char not in valid_characters:
            return False

    # If all conditions are met, the password is valid
    return True


def main():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Enter your password: ")
        if is_valid_password(password):
            print("Password is valid")
            break
        else:
            print("Password is invalid")
            attempts += 1

    if attempts == max_attempts:
        print("Too many attempts. Please try again later.")


if __name__ == "__main__":
    main()
