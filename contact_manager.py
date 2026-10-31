import json
import os


CONTACTS_FILE = "contacts.json"


def load_contacts():

    if not os.path.exists(CONTACTS_FILE):
        return []

    with open(CONTACTS_FILE, "r") as file:
        data = json.load(file)

    return data.get("contacts", [])


def find_contact(name):

    contacts = load_contacts()

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact

    return None


if __name__ == "__main__":

    name = input("Enter recipient name: ")

    contact = find_contact(name)

    if contact:
        print("\nContact found!")
        print("Name:", contact["name"])
        print("Email:", contact["email"])

    else:
        print("\nContact not found!")
        print("Please provide a verified email address.")

