# Book Management System

#### Video Demo:  <URL HERE>
#### Description:

Welcome to the **Book Management System**! This Python-based application allows users to manage a collection of books by adding, updating, deleting, searching, and displaying books. The system also saves the data to a CSV file for persistence, ensuring that your book catalog is preserved even after the program exits.

### Features:
1. **Add a New Book**: Add a book by providing its title and author.
2. **Update a Book**: Modify the title or author of an existing book.
3. **Delete a Book**: Remove a book from the catalog.
4. **Search for a Book**: Find a book by its title and view its details.
5. **Display All Books**: View the entire catalog of books.
6. **Data Persistence**: All book data is saved to a CSV file (`books.csv`) and loaded automatically when the program starts.

### Dependencies:
- `pytest`: For running unit tests.
- `pyfiglet`: For creating ASCII art text banners.
- `tabulate`: For displaying data in a clean, tabular format.

### How It Works:
- The program uses a dictionary to store books, where the key is the book title and the value is the author.
- The `csv` module is used to read and write data to a CSV file for persistence.
- The program is menu-driven, allowing users to interact with the system through a simple text-based interface.

### Code Structure:
- **`project.py`**: Contains the main program logic, including functions for adding, updating, deleting, searching, and displaying books.
- **`test_project.py`**: Includes unit tests for the core functions using `pytest`.
- **`requirements.txt`**: Lists the dependencies required to run the project (e.g., `pytest`).

### How to Run:
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt