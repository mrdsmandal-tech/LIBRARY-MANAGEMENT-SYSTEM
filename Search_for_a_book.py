import json
def search_for_a_book():
    new_book = json.load(open("new_book.json"))
    a=input("enter book id to search the book: ")
    if a in new_book:
        print(new_book[a])

search_for_a_book()