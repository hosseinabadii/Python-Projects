class ContactBook:
    """A class used to represent a Contact Book."""

    def __init__(self) -> None:
        """Initialize contact book object with an empty dictionary."""

        self.contacts: dict[str, dict] = {}

    def is_contact(self, name: str):
        if name in self.contacts:
            return True
        return False

    def add_contact(
        self,
        name: str,
        phone: str,
        email: str | None = None,
        address: str | None = None,
    ) -> None:
        """Adds a new contact to the contact book.

        :param name: The name of the contact
        :param phone: The phone number of the contact
        :param email: The email address of the contact
        :param address: The physical address of the contact
        """
        if self.is_contact(name):
            print("Contact already exists.")
        else:
            contact = {"phone": phone, "email": email, "address": address}
            self.contacts[name] = contact
            print("Contact added successfully!")

    def get_contact(self, name: str) -> None:
        """Displays the info of the contact with the given name

        :param name: The name of the contact
        """
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name    : {name}")
            print(f"Phone   : {info['phone']}")
            print(f"Email   : {info['email']}")
            print(f"Address : {info['address']}")
            print("----------------------------")

    def get_contacts(self) -> None:
        """Displays all contacts in the contact book."""

        if not self.contacts:
            print("The contact book is empty!")

        for name in self.contacts:
            self.get_contact(name)

    def delete_contact(self, name: str):
        """Deletes a contact from the contact book.

        :param name: The name of the contact to delete
        """
        if self.is_contact(name):
            self.contacts.pop(name)
            print("Contact deleted successfully!")
        else:
            print("Contact not found")

    def delete_all(self) -> None:
        confirm = input("Delete all contacts (y/n)? ")
        if confirm.lower() == "y":
            self.contacts.clear()
            print("All contacts are deleted!")
        else:
            print("Deleting canceled!")

    def edit_contact(
        self,
        name: str,
        phone: str | None = None,
        email: str | None = None,
        address: str | None = None,
    ) -> None:
        """Edits an existing contact in the contact book.

        :param name: The name of the contact to edit
        :param phone: The new phone number of the contact
        :param email: The new email address of the contact
        :param address: The new physical address of the contact
        """
        if self.is_contact(name):
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            print("Contact updated successfully!")
        else:
            print("Contact not found")
