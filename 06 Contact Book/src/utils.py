import pickle
from contact import ContactBook


def save_data(data: ContactBook):
    with open("data/contacts.pkl", "wb") as f:
        pickle.dump(data, f)
    print("All changes saved!")


def load_data() -> ContactBook:
    print("loading data...")
    try:
        with open("data/contacts.pkl", "rb") as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        book = ContactBook()
        save_data(book)
        return book
