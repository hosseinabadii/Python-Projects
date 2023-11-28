<img src="./images/banner.png" width="800">

# Contact Book

A simple command-line interface (CLI) application to manage a contact book. This application allows users to create, view, edit, and delete contacts. All contact information is persisted using Python's `pickle` module.

## Features

- Add new contacts with details such as name, phone, email, and address
- View all contacts in the contact book
- Get details of a specific contact
- Edit existing contact details
- Delete specific contacts
- Delete all contacts in the contact book
- Persist contact data across application sessions


## Requirements
- Python 3.10+


## Installation

Follow these steps to set up the project:

1. Clone the repository to your local machine

2. Navigate to the project directory

3. Run the main project file:

```bash
python src/main.py
```

## Usage

After starting the application, you will be presented with a menu of options:

1. View contacts
2. Add contact
3. Edit contact
4. Delete contact
5. Save changes
9. Delete all contacts
0. Save and Quit

Select an option by typing the corresponding number and following the prompted instructions.

## Data Storage

Contact information is stored using Python's `pickle` module in a file named `contacts.pkl` located in the `data` directory. Make sure not to delete this file to retain the contacts' data.
