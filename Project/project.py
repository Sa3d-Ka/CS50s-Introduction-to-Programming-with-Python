import csv
import pyfiglet
from tabulate import tabulate

books = {}

def main():
    hello_text = pyfiglet.figlet_format("HELLO", font="big")
    print(hello_text)
    LoadData()
    menu()

def menu():
    while True:
        print("\n=========== Menu ===========")
        print("1. Add a new book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search for a book by title")
        print("5. Display all books")
        print("6. Exit")
        print("============================")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ").lower().strip()
            author = input("Enter the book author: ").lower().strip()
            result = AddBook(title, author)
            print(result)
        elif choice == "2":
            title = input("Enter the title of the book to update: ").lower().strip()
            if title not in books:
                print("This book does not exist.")
                continue
            print("\n1. Update the title")
            print("2. Update the author\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_title = input("Enter the new title: ").lower().strip()
                result = UpdateBook(title, new_title=new_title)
            elif choice == "2":
                new_author = input("Enter the new author: ").lower().strip()
                result = UpdateBook(title, new_author=new_author)
            else:
                print("Invalid choice.")
                continue
            print(result)
        elif choice == "3":
            title = input("Enter the title of the book to delete: ").lower().strip()
            result = DeleteBook(title)
            print(result)
        elif choice == "4":
            title = input("Enter the book title: ").lower().strip()
            result = SearchBookByTitle(title)
            if result:
                print("====== Book Information ======")
                print(f"  Title: {result['title'].title()}")
                print(f"  Author: {result['author'].title()}")
                print("===============================")
            else:
                print("This book does not exist.")
        elif choice == "5":
            DisplayBooks()
        elif choice == "6":
            bye = pyfiglet.figlet_format("GOODBYE", font="big")
            print(bye)
            break
        else:
            print("Invalid choice.")

def AddBook(title, author):
    if title in books:
        return "This book already exists."
    books[title] = author
    ExportToCSV()
    return f"The book '{title.title()}' was added successfully."

def UpdateBook(title, new_title=None, new_author=None):
    if new_title:
        author = books[title]
        del books[title]
        books[new_title] = author
        ExportToCSV()
        return f"The book '{title.title()}' was updated to '{new_title.title()}' successfully."
    elif new_author:
        books[title] = new_author
        ExportToCSV()
        return f"The author of '{title.title()}' was updated to '{new_author.title()}' successfully."

def DeleteBook(title):
    if title not in books:
        return "This book does not exist."
    del books[title]
    ExportToCSV()
    return f"The book '{title.title()}' was deleted successfully."

def SearchBookByTitle(title):
    if title not in books:
        return None
    return {"title": title, "author": books[title]}

def DisplayBooks():
    try:
        with open('Project/books.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            table = list(reader)

            headers = table[0]
            data = table[1:]

            print(tabulate(data, headers, tablefmt="grid"))
        print("Books loaded successfully.")
    except FileNotFoundError:
        print("No data file found. Starting with an empty catalog.")

def ExportToCSV():
    with open('Project/books.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author"])
        for title, author in books.items():
            writer.writerow([title, author])

def LoadData():
    try:
        with open('Project/books.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title, author = row
                books[title] = author
        print("Books loaded successfully.")
    except FileNotFoundError:
        print("No data file found. Starting with an empty catalog.")

if __name__ == "__main__":
    main()