# Sheet 3: Building a Library System

In this sheet and the following ones, we will **accumulatively** build a project as we expand our knowledge of Python.

---

## Project Overview

We want to build a library management system based on the following requirements:

1. **Data Storage:** The system should store book information, including ISBN, Title, Author, Year, and Number of Copies.
2. **User Functionality:** The system should allow users to:
* Add a new book.
* Search for a book by title or author.
* List all books and authors.
* Borrow and return books.



---

## Implementation

### Part 1: Data Structures

1. **Input Data:** Ask the user to input the ISBN, Title, Author, Year of Publish, and Number of Copies.
* Use `str` for ISBN, Title, Author, and Year (as these are descriptive).
* Use `int` for the Number of Copies.


2. **Main Storage:** Use a **Dictionary** to store all information.
* **Key:** ISBN (string).
* **Value:** A **Tuple** containing the Title, Author, Year, and Copies (remember that order matters in a tuple).


3. **Search Helpers:**
* Use a **List** to store all book titles.
* Use a **Set** to store unique authors.


4. **Initial Data:** Manually add three books to your dictionary first, then prompt the user to add one more.

**Sample Data Format:**
| ISBN | Title | Author | Year | Copies |
| :--- | :--- | :--- | :--- | :--- |
| 978-01 | Python Basics | John Doe | 2021 | 5 |

5. **Basic Search:** Ask the user to search for a book by its **ISBN** and print the associated details.

---

### Part 2: Flow Control

> This part tests your understanding of **conditions** and **loops**.

To make the system more convenient, we will implement a menu so the user can choose specific tasks. Use a `while True` loop to keep the program running until the user chooses to exit.

1. **The Main Menu:** Print a welcome message and implement a loop that asks the user for a choice.
```python
print("Welcome to the Library System")
while True:
    print("\nWhat do you want to do? (Enter a number)")
    print("1. Add new book")
    print("2. List all books")
    print("3. Search for a book by title")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Search for all books by author")
    print("7. Exit")

    choice = input("> ")

```


2. **Add New Book:** When the user selects `1`, prompt for the ISBN, Title, Author, Year, and Copies, then update your dictionary and helper structures.
3. **List All Books:** When the user selects `2`, iterate through your dictionary and print the books in a clean, readable format.
4. **Search by Title:** When the user selects `3`, search through your collection using the book title.
5. **Borrow Book:** When the user selects `4`, find the book by its ISBN and **subtract 1** from the number of available copies.
6. **Return Book:** When the user selects `5`, find the book by its ISBN and **add 1** to the number of available copies.
7. **Search by Author:** When the user selects `6`, find all books associated with a specific author. (Hint: One author may have multiple books in the system).
8. **Exit:** If the user selects `7`, break the loop to close the program.
