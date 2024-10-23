import json
import re
import os

# Define the address book file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ADDRESSBOOK_FILE = os.path.join(BASE_DIR, "contacts.json")

# Helper functions


def load_contacts():
    """Load contacts from the file."""
    try:
        with open(ADDRESSBOOK_FILE, "r") as file:
            print("Loading contacts from file...")
            contacts = json.load(file)
            print("Contacts loaded successfully.✔.")
            return contacts
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading contacts:", e)
        default_contacts = []
        save_contacts(default_contacts)
        return default_contacts


def save_contacts(contacts):
    """Save contacts to the file."""
    with open(ADDRESSBOOK_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def generate_id(contacts):
    """Generate a new ID for the contact."""
    if contacts:
        return max(contact["id"] for contact in contacts) + 1
    return 1


def validate_name(name):
    """Validate that the name contains only alphabetic characters."""
    return name.isalpha()


def validate_emails(emails):
    """Validate emails format (at least one '@')."""
    return all(re.match(r"[^@]+@[^@]+\.[^@]+", email) for email in emails)


def validate_phone_numbers(phone_numbers):
    """Validate phone numbers contain only digits."""
    return all(re.match(r"^\d+$", re.sub(r"[-\s]", "", number)) for number in phone_numbers)


def list_contacts(contacts):
    """List all contacts sorted by first name in descending order."""
    # contacts_sorted = sorted(
    #     contacts, key=lambda x: x['first_name'].lower(), reverse=True)
    contacts.sort(key=lambda x: x['first_name'])

    print("\n=====================================")
    for idx, contact in enumerate(contacts, 1):
        print(f"Position: {idx}")
        print(f"First name: {contact['first_name']}")
        print(f"Last name: {contact['last_name']}")
        print(f"Emails: {', '.join(contact['emails'])}")
        print(f"Phone numbers: {', '.join(contact['phone_numbers'])}")
    print("=====================================")


def add_contact(contacts):
    """Add a new contact."""
    first_name = input("Firstname: ").strip().lower()
    last_name = input("Lastname: ").strip().lower()

    if not (validate_name(first_name) and validate_name(last_name)):
        print("Invalid name. First and last names must contain only alphabetic characters.")
        return

    emails = [email.strip() for email in input(
        "Emails (comma separated): ").split(',')]
    if not validate_emails(emails):
        print("Invalid email format.")
        return

    phone_numbers = [number.strip() for number in input(
        "Phone numbers (comma separated): ").split(',')]
    if not validate_phone_numbers(phone_numbers):
        print("Invalid phone number format.")
        return

    new_contact = {
        "id": generate_id(contacts),
        "first_name": first_name,
        "last_name": last_name,
        "emails": list(set(emails)),
        "phone_numbers": list(set(phone_numbers))
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added to addressbook.")


def remove_contact(contacts):
    """Remove a contact by ID."""
    try:
        contact_id = int(input("Enter contact ID to remove: ").strip())
        updated_contacts = [
            contact for contact in contacts if contact['id'] != contact_id]
        if len(updated_contacts) == len(contacts):
            print(f"No contact with ID {contact_id} found.")
        else:
            save_contacts(updated_contacts)
            print(f"Contact with ID {contact_id} removed.")
    except ValueError:
        print("Invalid ID.")


def merge_contacts(contacts):
    """Merge contacts with the same first and last names."""
    contacts_dict = {}

    for contact in contacts:
        full_name = f"{contact['first_name']} {contact['last_name']}".lower()
        if full_name in contacts_dict:
            primary_contact = contacts_dict[full_name]
            primary_contact['emails'] = list(
                set(primary_contact['emails'] + contact['emails']))
            primary_contact['phone_numbers'] = list(
                set(primary_contact['phone_numbers'] + contact['phone_numbers']))
        else:
            contacts_dict[full_name] = contact

    merged_contacts = list(contacts_dict.values())
    save_contacts(merged_contacts)
    print("Contacts merged.")


def main():
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")
        choice = input("Choose an option: ").upper()

        if choice == 'L':
            list_contacts(contacts)
        elif choice == 'A':
            add_contact(contacts)
        elif choice == 'R':
            remove_contact(contacts)
        elif choice == 'M':
            merge_contacts(contacts)
        elif choice == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
