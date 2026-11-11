import add_new_book
import Display_all_books
import Search_for_a_book
import Register_a_student
import Issue_a_book
import Return_a_book
import Display_issued_books
import Delete_a_book
def main_menu():
    while True:
        print("===============================")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("Welcome to the main menu")
        print("1. Add new book")
        print("2. Display all books")
        print("3. search for books")
        print("4. Register a student")
        print("5. Issue a book")
        print("6. Return a book")
        print("7. Display issued books")
        print("8. Delete a book")
        print("9. Exit")
        print("==============================")

        choice = input("Enter your choice(1-9): ")
        if choice == "1":
            add_new_book.add_new_book()

        elif choice == "2":
            Display_all_books.display_all_books()

        elif choice == "3":
            Search_for_a_book.search_for_a_book()

        elif choice == "4":
            Register_a_student.register_a_student()

        elif choice == "5":
            Issue_a_book.issue_a_book()

        elif choice == "6":
            Return_a_book.return_a_book()

        elif choice == "7":
            Display_issued_books.display_issued_books()

        elif choice == "8":
            Delete_a_book.delete_a_book()

        elif choice == "9":
            print("Thank you for using this program")
            break
        else:
            print("Please enter a valid choice")

main_menu()