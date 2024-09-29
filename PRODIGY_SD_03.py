"""
    Develop a program that allows users to store and manage contact information. 
    The program should provide options to add a new contact by entering their name, 
    phone number, and email address. It should also allow users to view their contact list, 
    edit existing contacts, and delete contacts if needed. The program should store the 
    contacts in memory or in a file for persistent storage.
"""

import json
import os

# Function to load contacts from a file
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

# Function to save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
   
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\n")
    else:
        print("No contacts found.")

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Editing contact {name}. Leave field blank to keep current value.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ") or contacts[name]['email']
       
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
