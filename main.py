data_file = "books.json"

import sys
import json
import os
from colorama import init, Fore, Style
init(autoreset=True)

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
    print(Fore.CYAN + "Please choose an option:" + Style.RESET_ALL)

    print("[1] Add a new book")
    print("[2] View all books")
    print("[3] Search books")
    print("[4] Edit a book")
    print("[5] Delete a book")
    print("[6] Export book data")
    print("[7] Show statistics")
    print("[0] Exit")

def save_books():
    try:
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(books, f, indent=4)
        print(Fore.GREEN + "\n[Info] Book data saved.\n")
    except Exception as e:
        print(Fore.RED + f"\n[Error] Failed to save data: {e}\n")


def load_books():
    if os.path.exists(data_file):
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(Fore.RED + f"\n[Error] Failed to load data: {e}\n")
    return []

# Placeholder for book list
books = load_books()


# Placeholder functions
def add_book():
    print("\n--- Add a New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    status = input("Enter status (read/unread/wishlist): ").strip().lower()

    if not title or not author:
        print("\n[Error] Title and author are required!\n")
        return

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "status": status
    }

    books.append(book)
    save_books()

    print(f"\n[Success] '{title}' by {author} was added to your library.\n")


def view_books():
    print("\n--- Your Book Collection ---")
    if not books:
        print("Your library is currently empty.\n")
        return

    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} - {book['genre']} ({book['status']})")
    print()


def search_books():
    print("\n--- Search Books ---")
    keyword = input("Enter a keyword (title, author, or genre): ").strip().lower()

    if not keyword:
        print(Fore.YELLOW + "\n[Notice] No keyword entered.\n")
        return

    results = []
    for book in books:
        if (keyword in book['title'].lower()
                or keyword in book['author'].lower()
                or keyword in book['genre'].lower()):
            results.append(book)

    if results:
        print(Fore.CYAN + f"\nFound {len(results)} matching book(s):\n")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['title']} by {book['author']} - {book['genre']} ({book['status']})")
    else:
        print(Fore.RED + "\nNo matching books found.\n")


def edit_book():
    print("[TODO] Edit book")

def delete_book():
    print(Fore.RED + "\n[Error] Invalid book number.\n")

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
        print(Fore.GREEN + f"\n[Success] '{deleted['title']}' was deleted from your library.\n")

    else:
        print(Fore.YELLOW + "\n[Cancelled] No book was deleted.\n")


import csv  # ganz oben im Importbereich ergänzen

def export_books():
    if not books:
        print(Fore.YELLOW + "\n[Notice] No books available to export.\n")
        return

    filename = "books_export.csv"
    try:
        with open(filename, "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["title", "author", "genre", "status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for book in books:
                writer.writerow(book)

        print(Fore.GREEN + f"\n[Success] Books exported to '{filename}'\n")
    except Exception as e:
        print(Fore.RED + f"\n[Error] Failed to export books: {e}\n")


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
