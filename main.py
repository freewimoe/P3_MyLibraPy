import sys
import json
import os

def display_banner():
    print("""
__  __       _ _     _                           
|  \/  |     (_) |   | |                          
| \  / | __ _ _| |__ | |__   __ _ _ __  _ __  ___ 
| |\/| |/ _` | | '_ \| '_ \ / _` | '_ \| '_ \/ __|
| |  | | (_| | | |_) | | | | (_| | |_) | |_) \__ \\
|_|  |_|\__,_|_|_.__/|_| |_|\__,_| .__/| .__/|___/
                                 | |   | |        
                                 |_|   |_|        
""")
    print("Welcome to MyLibraPy - your personal CLI book tracker!\n")

def main_menu():
    print("Please choose an option:")
    print("[1] Add a new book")
    print("[2] View all books")
    print("[3] Search books")
    print("[4] Edit a book")
    print("[5] Delete a book")
    print("[6] Export book data")
    print("[7] Show statistics")
    print("[0] Exit")

# Placeholder for book list
books = []

# Placeholder functions
def add_book():
    print("[TODO] Add book")

def view_books():
    print("[TODO] View books")

def search_books():
    print("[TODO] Search books")

def edit_book():
    print("[TODO] Edit book")

def delete_book():
    print("\n--- Delete a Book ---")
    view_books()
    if not books:
        return

    try:
        index = int(input("Enter the number of the book you want to delete: ")) - 1
        if index < 0 or index >= len(books):
            print("\n[Error] Invalid book number.\n")
            return
    except ValueError:
        print("\n[Error] Please enter a valid number.\n")
        return

    book = books[index]
    confirm = input(f"Are you sure you want to delete '{book['title']}' by {book['author']}? (y/n): ").strip().lower()
    if confirm == "y":
        deleted = books.pop(index)
        save_books()
        print(f"\n[Success] '{deleted['title']}' was deleted from your library.\n")
    else:
        print("\n[Cancelled] No book was deleted.\n")

def export_books():
    print("[TODO] Export books")

def show_statistics():
    print("[TODO] Show statistics")

def main():
    display_banner()
    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            edit_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            export_books()
        elif choice == "7":
            show_statistics()
        elif choice == "0":
            print("\nThank you for using MyLibraPy! Goodbye.\n")
            sys.exit()
        else:
            print("\nInvalid option. Please try again.\n")

if __name__ == "__main__":
    main()
