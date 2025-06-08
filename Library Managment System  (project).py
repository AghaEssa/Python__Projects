# Full updated code with Admin Panel feature
import math
import datetime
import random
import os
import pyfiglet

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = [
            Book("1984", "George Orwell"),
            Book("Python Programming", "John Zelle"),
            Book("A Brief History of Time", "Stephen Hawking")
        ]
        self.records_file = "library_records.txt"
        if not os.path.exists(self.records_file):
            open(self.records_file, 'w').close()

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} [{status}]")

    def search_books(self, keyword):
        print(f"\nSearch Results for '{keyword}':")
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"- {book.title} by {book.author} [{status}]")
                found = True
        if not found:
            print("No books found.")

    def borrow_book(self, title, username):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                date = datetime.datetime.now()
                fine = round(random.uniform(0, 10), 2)
                self.save_record(f"{username} borrowed '{book.title}' on {date.strftime('%Y-%m-%d %H:%M:%S')} | Fine Estimation: ${fine}\n")
                print(f"\nYou borrowed '{book.title}'. Estimated fine if late: ${fine}")
                return
        print("Book is not available or doesn't exist.")

    def return_book(self, title, username):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                date = datetime.datetime.now()
                late_days = random.randint(0, 10)
                fine = math.ceil(late_days * 1.5)
                self.save_record(f"{username} returned '{book.title}' on {date.strftime('%Y-%m-%d %H:%M:%S')} | Late: {late_days} days | Fine: ${fine}\n")
                print(f"\nYou returned '{book.title}'. Late by {late_days} days. Fine: ${fine}")
                return
        print("Book not found or not borrowed.")

    def save_record(self, record):
        with open(self.records_file, "a") as file:
            file.write(record)

    def admin_panel(self):
        print("\n===== Admin Panel =====")
        with open(self.records_file, 'r') as file:
            data = file.read()
            if data:
                print(data)
            else:
                print("No records found.")

class AuthSystem:
    def __init__(self):
        self.users_file = "users.txt"
        self.users = self.load_users()

    def load_users(self):
        users = {}
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    users[username] = password
        return users

    def signup(self):
        print("\n--- Sign Up ---")
        username = input("Enter username: ")
        if username in self.users:
            print("Username already exists.")
            return None
        password = input("Enter password: ")
        with open(self.users_file, 'a') as file:
            file.write(f"{username},{password}\n")
        self.users[username] = password
        print("Signup successful. Please login.")
        return None

    def login(self):
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.users.get(username) == password:
            print("Login successful.")
            return username
        else:
            print("Invalid credentials.")
            return None

def print_ascii(text):
    print(pyfiglet.figlet_format(text))

def main():
    print_ascii("Library System")
    library = Library()
    auth = AuthSystem()
    current_user = None

    while True:
        if not current_user:
            print("\n1. Login\n2. Sign Up\n3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                current_user = auth.login()
            elif choice == '2':
                auth.signup()
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
        else:
            print_ascii(f"Welcome {current_user}")
            print("1. View Books\n2. Search Book\n3. Borrow Book\n4. Return Book\n5. Admin Panel\n6. Logout")
            option = input("Choose an option: ")

            if option == '1':
                library.display_books()
            elif option == '2':
                keyword = input("Enter keyword to search: ")
                library.search_books(keyword)
            elif option == '3':
                title = input("Enter book title to borrow: ")
                library.borrow_book(title, current_user)
            elif option == '4':
                title = input("Enter book title to return: ")
                library.return_book(title, current_user)
            elif option == '5':
                if current_user.lower() == "admin":
                    library.admin_panel()
                else:
                    print("Access denied. Only admin can view records.")
            elif option == '6':
                current_user = None
            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()
