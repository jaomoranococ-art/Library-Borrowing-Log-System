# ========== LOGIN FUNCTION ==========
def login():
    correct_username = "admin"
    correct_password = "1234"

    while True:
        print("===== LOGIN =====")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful! Proceeding to menu...\n")
            break
        else:
            print("Incorrect username or password. Try again.\n")


# ========== MAIN MENU FUNCTION ==========
def main_menu():
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Log")
    print("6. Logout")
    print("7. Exit")


# ========== START OF PROGRAM ==========
while True:
    
    # ---- LOGIN SECTION ----
    login()

    # ---- LIBRARY DATA ----
    books = []           
    borrowed_books = {}  
    log = []             

    # ---- MENU LOOP ----
    while True:
        main_menu()
        choice = input("Enter choice: ")

        # 1. Add Book
        if choice == "1":
            title = input("Enter book title to add: ")

            if title in books:
                print("Book already exists!")
            else:
                books.append(title)
                log.append(f"Added book: {title}")
                print("Book added successfully!")

        # 2. View Books
        elif choice == "2":
            if len(books) == 0:
                print("No books available.")
            else:
                print("\nAvailable Books:")
                for b in books:
                    print("- " + b)

        # 3. Borrow Book
        elif choice == "3":
            if len(books) == 0:
                print("No books available to borrow.")
            else:
                name = input("Enter your name: ")

                print("\nAvailable Books:")
                for b in books:
                    print("- " + b)

                book_choice = input("Enter the book you want to borrow: ")

                if book_choice in books:
                    borrowed_books[name] = book_choice
                    books.remove(book_choice)
                    log.append(f"{name} borrowed {book_choice}")
                    print("You borrowed:", book_choice)
                else:
                    print("Book not found in library.")

        # 4. Return Book
        elif choice == "4":
            name = input("Enter your name: ")

            if name in borrowed_books:
                returned_book = borrowed_books.pop(name)
                books.append(returned_book)
                log.append(f"{name} returned {returned_book}")
                print("Book returned:", returned_book)
            else:
                print("You have no borrowed books.")

        # 5. View Log
        elif choice == "5":
            print("\n===== BORROW LOG =====")
            if len(log) == 0:
                print("No activity yet.")
            else:
                for entry in log:
                    print(entry)

        # 6. Logout
        elif choice == "6":
            print("Logging out... Returning to login screen.\n")
            break   # breaks menu → returns to LOGIN

        # 7. Exit
        elif choice == "7":
            print("Exiting system... Goodbye!")
            exit()  # fully ends the program

        # Invalid Input
        else:
            print("Invalid choice. Try again.")
