import os
from utils import load_data, save_data


def main():
    os.system("clear")
    print("\n--- Contact Book Application ---")
    book = load_data()

    while True:
        print("\n1. View contacts")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Save changes")
        print("9. Delete all contacts")
        print("0. Save and Quit")
        user_choice = input("\nPlease choose an option: ")
        os.system("clear")

        if user_choice == "1":
            print("\n# List of contacts\n")
            book.get_contacts()

        elif user_choice == "2":
            print("\n# Add New Contact\n")
            name = input("Enter Contact name: ")
            if book.is_contact(name):
                print(f"The contact with {name=} already exists!")
                book.get_contact(name)
                continue
            phone = input("Enter Contact phone: ")
            email = input("Enter Contact email: ")
            address = input("Enter Contact address: ")
            book.add_contact(name, phone, email, address)

        elif user_choice == "3":
            print("\n# Edit Contact\n")
            name = input("Enter name of the contact to edit: ")
            if not book.is_contact(name):
                print(f"The contact with {name=} does not exist!")
                continue
            book.get_contact(name)
            phone = input("Enter new phone number (press Enter to keep unchanged): ")
            email = input("Enter new email (press Enter to keep unchanged): ")
            address = input("Enter new address (press Enter to keep unchanged): ")
            book.edit_contact(name, phone or None, email or None, address or None)

        elif user_choice == "4":
            print("\n# Delete Contant\n")
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)

        elif user_choice == "5":
            print("\n# Save Changes\n")
            save_data(book)

        elif user_choice == "9":
            print("\n# Delete All Contants\n")
            book.delete_all()

        elif user_choice == "0":
            save_data(book)
            print("\nThank You for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
