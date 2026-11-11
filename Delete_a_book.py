import json
def delete_a_book():
     with open("new_book.json") as f:
            book = json.load(f)
     with open("new_book.json", "r") as f:
        new_book = json.load(f)
        print(json.dumps(new_book, indent=4))

     book_need_to_delete =input("Enter a book id you would like to delete: ")
removed_book = new_book.pop(book_need_to_delete,"key not found")
if removed_book == "key not found":
     print(f"{book_need_to_delete} doesn't exist")
else:
     print(f"{book_need_to_delete} deleted")

with open("new_book.json", "w") as f:
        json.dump(new_book, f,indent=4)
        print("changes are saved successfully")

delete_a_book()