class PasswordManager:
    def __init__(self, old_passwords=None):
        # Initialize old_passwords; default to an empty list if not provided
        self.old_passwords = old_passwords if old_passwords else []

    def get_password(self):
        # Return the current password (last in the list), or None if empty
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        # Add new password if it's not already in old_passwords
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)

    def is_correct(self, password):
        # Check if provided password matches the current one
        return password == self.get_password()

if __name__ == "__main__":
    # Create a PasswordManager instance
    pm = PasswordManager()

    # Set passwords
    pm.set_password("password123")
    pm.set_password("secure456")

    # Get current password
    print(pm.get_password())  # Output: secure456

    # Check if a password is correct
    print(pm.is_correct("password123"))  # Output: False
    print(pm.is_correct("secure456"))  # Output: True

    # Set a duplicate password (shouldn't be added)
    pm.set_password("secure456")
    print(pm.old_passwords)  # Output: ['password123', 'secure456']
