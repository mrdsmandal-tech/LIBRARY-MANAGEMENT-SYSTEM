import json
def display_all_books():
    with open("new_book.json", "r") as f:
        new_book = json.load(f)
    print(json.dumps(new_book, indent=4))

display_all_books()