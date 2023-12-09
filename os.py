import os

# Dictionary to store contact information
contacts = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contacts[name] = (phone_number, email)
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for name, (phone_number, email) in contacts.items():
            print(f"Name: {name}, Phone: {phone_number}, Email: {email}")

def edit_contact():
    name_to_edit = input("Enter the name of the contact to edit: ")
    
    if name_to_edit in contacts:
        phone_number = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")

        contacts[name_to_edit] = (phone_number, email)
        print(f"Contact {name_to_edit} updated successfully!")
    else:
        print(f"Contact {name_to_edit} not found.")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"Contact {name_to_delete} deleted successfully!")
    else:
        print(f"Contact {name_to_delete} not found.")

def contact_manager():
    while True:
        clear_screen()
        print("Contact Manager")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        input("Press Enter to continue...")

if _name_ == "_main_":
    contact_manager()