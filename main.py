import json

# File to store the library data

LIBRARY_FILE = "library.txt"

# Load the library from file if it exists

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save the library in file

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book with users input

def add_book(library):
    title = input("\n Enter the book title: ")
    author = input("\n Enter the author: ")
    year = input("\n Enter the publication year: ")
    # Select the genre
    genres = ["Fiction", "Non-Fiction", "Mystery", "Fantasy", "Science Fiction", "Biography", "History", "Romance", "Horror"]
    print("\nSelect a genre:\n")
    for idx, genre in enumerate(genres, start=1):
        print(f"{idx}. {genre}")
    
    while True:
        try:
            genre_choice = int(input("\nEnter the number corresponding to the genre: "))
            if 1 <= genre_choice <= len(genres):
                genre = genres[genre_choice - 1]
                break
            else:
                print("\nInvalid choice. Please select a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
    read = input("\n Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    # Add the book in library list as dictionary
    
    library.append({
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read
    })
    print("\nBook added successfully! 🎉")

# Remove the book by title or author

def remove_book(library):
    title = input("\nEnter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("\nBook removed successfully! ❌")
            return
    print("\nBook not found. 🤷‍♂️")

# Search the book by book title

def search_book(library):
    choice = input("\nSearch by:\n1. Title\n2. Author\nEnter your choice: ")
    keyword = input("\nEnter the search term: ").lower()
    
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    
    if results:
        print("\nMatching Books:")
        for idx, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"\n{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("\nNo matching books found. 🤷‍♂️")

# Displays all the book in library

def display_books(library):
    if not library:
        print("\nYour library is empty. 📪")
        return
    
    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"\n{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics of library, e.g, Total-books, Readed_books, Read-percentage

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("\nNo books in the library.")
        return
    
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    
    print(f"\nTotal books: {total_books}")
    print(f"Readed books: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")


# Main function to run the menu

def main():
    library = load_library()

    print("""
    ╔════════════════════════════════════════╗
    ║    🚀 WELCOME TO  \033[1mBIBLIO SHELL 🚀      ║
    ╠════════════════════════════════════════╣
    ║   📚 YOUR PROFFESSIONAL & PERSONAL     ║
    ║          LIBRARY MANAGER 📊            ║
    ╚════════════════════════════════════════╝
    """)
    
    while True:
        print("""
        Main Menu:\n
        1. 📖 Add a book
        2. ❌ Remove a book
        3. 🔎 Search for a book
        4. 📚 Display all books
        5. 📊 Display statistics
        6. 🚪 Exit
        """)
        choice = input("Choose what do you like to do: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\nThanks for using ")
            print("\nLibrary saved to file. Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
