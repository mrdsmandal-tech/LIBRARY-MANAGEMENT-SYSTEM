import json
def display_issued_books():
    with open("issued_books.json", "r") as f:
        issued_books = json.load(f)
    print(json.dumps(issued_books, indent=4))
display_issued_books()