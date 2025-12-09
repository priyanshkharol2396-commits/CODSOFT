contacts = {}  

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    print("-" * 40)
    for name, info in contacts.items():
        print(f"Name   : {name}")
        print(f"Phone  : {info['phone']}")
        print(f"Email  : {info['email']}")
        print(f"Address: {info['address']}")
        print("-" * 40)
    print()

def search_contact():
    query = input("Search by name or phone: ").strip().lower()
    found = False

    for name, info in contacts.items():
        if query in name.lower() or query in info["phone"]:
            print("\nContact found:")
            print(f"Name   : {name}")
            print(f"Phone  : {info['phone']}")
            print(f"Email  : {info['email']}")
            print(f"Address: {info['address']}\n")
            found = True

    if not found:
        print("No matching contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.\n")
        return

    print("Leave field blank if you don't want to change it.")
    phone = input("New phone number: ").strip()
    email = input("New email: ").strip()
    address = input("New address: ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    print(f"Contact '{name}' updated successfully.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print("Contact not found.\n")

def show_menu():
    print("==== Contact Book ====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:  
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
