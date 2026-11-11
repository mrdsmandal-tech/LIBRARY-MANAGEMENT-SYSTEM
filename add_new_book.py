import json
new_book = {}
def add_new_book():

    a=input("enter book id: ")
    b=input("enter book title: ").strip()
    c=input("enter book author: ").strip()
    d=input("enter available book copies: ").strip()
    new_book[a]={
        "title":b,
        "author":c,
        "available":d,
    }
    print(new_book)
    with open("new_book.json", "w") as f:
        json.dump(new_book, f,indent=4)

add_new_book()