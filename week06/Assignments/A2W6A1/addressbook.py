import json
import os
import re


class Contact:
    """Klasse voor contactpersoon die e-mails en telefoonnummers uniek opslaat."""

    def __init__(self, contact_id, first_name, last_name, emails, phone_numbers):
        self.id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.emails = list(set(emails))  # Zorg dat e-mails uniek zijn
        # Zorg dat telefoonnummers uniek zijn
        self.phone_numbers = list(set(phone_numbers))

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"First name: {self.first_name}\n"
            f"Last name: {self.last_name}\n"
            f"Emails: {', '.join(self.emails)}\n"
            f"Phone numbers: {', '.join(self.phone_numbers)}"
        )


class AddressBook:
    """Klasse voor het adresboek dat contacten beheert en opslaat in een JSON-bestand."""

    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        """Laad contacten uit het JSON-bestand."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
                for entry in contacts_data:
                    contact = Contact(
                        entry['id'],
                        entry['first_name'],
                        entry['last_name'],
                        entry['emails'],
                        entry['phone_numbers']
                    )
                    self.contacts.append(contact)
        else:
            self.contacts = []

    def save_contacts(self):
        """Sla de huidige lijst met contacten op in het JSON-bestand."""
        with open(self.filename, 'w') as file:
            json.dump(
                [
                    {
                        'id': contact.id,
                        'first_name': contact.first_name,
                        'last_name': contact.last_name,
                        'emails': contact.emails,
                        'phone_numbers': contact.phone_numbers
                    }
                    for contact in self.contacts
                ],
                file,
                indent=4
            )

    def get_next_id(self):
        """Bepaal het volgende ID voor een nieuw contact."""
        return max((contact.id for contact in self.contacts), default=0) + 1

    def add_contact(self, first_name, last_name, emails, phone_numbers):
        """Voeg een nieuw contact toe aan het adresboek."""
        new_id = self.get_next_id()
        new_contact = Contact(new_id, first_name,
                              last_name, emails, phone_numbers)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"Contact {first_name} {last_name} added to addressbook")

    def remove_contact(self, contact_id):
        """Verwijder een contact uit het adresboek op basis van het ID."""
        initial_count = len(self.contacts)
        self.contacts = [
            contact for contact in self.contacts if contact.id != contact_id]
        if len(self.contacts) < initial_count:
            self.save_contacts()
            print(f"Contact with ID {contact_id} removed")
        else:
            print(f"No contact found with ID {contact_id}")

    def list_contacts(self):
        """Geef alle contacten weer, gesorteerd op voornaam in aflopende volgorde."""
        self.contacts.sort(key=lambda x: x.first_name, reverse=True)
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print("======================================")
            print(contact)
        print("======================================")

    def merge_contacts(self):
        """Voeg contacten samen die dezelfde voor- en achternaam hebben."""
        contact_map = {}
        for contact in self.contacts:
            full_name = (contact.first_name, contact.last_name)
            if full_name not in contact_map:
                contact_map[full_name] = contact
            else:
                # Voeg unieke e-mails en telefoonnummers toe
                primary_contact = contact_map[full_name]
                primary_contact.emails.extend(
                    email for email in contact.emails if email not in primary_contact.emails
                )
                primary_contact.phone_numbers.extend(
                    phone for phone in contact.phone_numbers if phone not in primary_contact.phone_numbers
                )

        self.contacts = list(contact_map.values())
        self.save_contacts()
        print("Duplicate contacts merged.")


def validate_name(name):
    """Valideer of een naam alleen alfabetische tekens bevat."""
    return name.isalpha()


def validate_emails(emails):
    """Valideer of e-mails een correct formaat hebben."""
    return all(re.match(r"[^@]+@[^@]+\.[^@]+", email) for email in emails)


def validate_phone_numbers(phone_numbers):
    """Valideer of telefoonnummers alleen cijfers bevatten."""
    return all(re.match(r"^\d+$", re.sub(r"[-\s]", "", number)) for number in phone_numbers)


def main():
    address_book = AddressBook('contacts.json')

    while True:
        choice = input(
            "[L] List contacts\n"
            "[A] Add contact\n"
            "[R] Remove contact\n"
            "[M] Merge contacts\n"
            "[Q] Quit program\n"
            "Choose an option: "
        ).upper()

        if choice == 'L':
            address_book.list_contacts()
        elif choice == 'A':
            first_name = input("First name: ").strip().lower()
            last_name = input("Last name: ").strip().lower()

            if not (validate_name(first_name) and validate_name(last_name)):
                print(
                    "Invalid name. First and last names must contain only alphabetic characters.")
                continue

            emails = input("Emails (comma-separated): ").split(',')
            emails = [email.strip()
                      for email in emails if validate_emails([email])]
            if not emails:
                print("Invalid email format.")
                continue

            phone_numbers = input(
                "Phone numbers (comma-separated): ").split(',')
            phone_numbers = [
                number.strip() for number in phone_numbers if validate_phone_numbers([number])]
            if not phone_numbers:
                print("Invalid phone number format.")
                continue

            address_book.add_contact(
                first_name, last_name, emails, phone_numbers)
        elif choice == 'R':
            try:
                contact_id = int(input("Enter contact ID to remove: "))
                address_book.remove_contact(contact_id)
            except ValueError:
                print("Invalid ID. Please enter a valid numeric ID.")
        elif choice == 'M':
            address_book.merge_contacts()
        elif choice == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
