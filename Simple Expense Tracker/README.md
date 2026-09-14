# Simple Expense Tracker

A beginner-friendly command-line program written in Python that lets you record, view, and summarize your daily expenses.

## Objective

This project exists to practice the fundamentals of Python:

- Variables
- Lists
- Dictionaries
- Loops
- Functions
- Conditional statements
- User input
- Basic data analysis
- Error handling

The goal is clear, readable code — not a large or clever application.

## Features

1. **Main Menu** — an interactive menu that keeps running until you choose Exit.
2. **Add Expense** — record a description, an amount, and a category.
3. **View Expenses** — list everything recorded so far, numbered.
4. **View Total** — show how many expenses there are and how much was spent in total.
5. **Category Summary** — show spending per category plus the overall total.
6. **Input Validation** — the program refuses bad input instead of crashing.

## Technologies Used

- Python 3 (any recent version)
- The standard library only — no external packages to install

## How the Program Works

All expenses live in a single Python list called `expenses`, created inside `main()`.

Each expense is one dictionary:

```python
{
    "description": "Lunch",
    "amount": 150.0,
    "category": "Food"
}
```

So the list looks like this after three entries:

```python
expenses = [
    {"description": "Lunch",         "amount": 150.0, "category": "Food"},
    {"description": "Jeepney Fare",  "amount": 30.0,  "category": "Transportation"},
    {"description": "Notebook",      "amount": 100.0, "category": "School"},
]
```

`main()` runs a `while True` loop. Each time around, it prints the menu, reads your
choice, and calls the matching function. Every feature is a separate function that
receives the `expenses` list as a parameter.

Data is stored **in memory only**. When you close the program, the expenses are gone.
Saving to a file or a database is a future improvement.

### Functions in `main.py`

| Function | Responsibility |
| --- | --- |
| `format_peso(amount)` | Turns a number into text like `₱150.00` |
| `print_header(title)` | Prints a section title |
| `ask_for_description()` | Asks for a description, rejects empty text |
| `ask_for_amount()` | Asks for an amount, rejects non-numbers and values ≤ 0 |
| `ask_for_category()` | Shows the category list, rejects invalid choices |
| `add_expense(expenses)` | Builds one expense dictionary and appends it to the list |
| `view_expenses(expenses)` | Prints every recorded expense |
| `calculate_total(expenses)` | Returns the sum of all amounts |
| `show_total(expenses)` | Prints the count and the total |
| `build_category_totals(expenses)` | Returns a dictionary of category → total |
| `category_summary(expenses)` | Prints the per-category breakdown |
| `show_menu()` | Prints the menu options |
| `main()` | Runs the menu loop |

## How to Run the Program

1. Make sure Python 3 is installed:

   ```bash
   python3 --version
   ```

2. Move into the project folder:

   ```bash
   cd "Simple Expense Tracker"
   ```

3. Run it:

   ```bash
   python3 main.py
   ```

   On Windows, use `python main.py`.

4. Choose `5` from the menu to exit.

## Example Usage

Adding an expense:

```text
Enter your choice: 1

========== ADD EXPENSE ==========

Enter expense description: Lunch
Enter amount: 150

Choose a category:
  1. Food
  2. Transportation
  3. School
  4. Bills
  5. Entertainment
  6. Shopping
  7. Other
Enter category number: 1

✓ Expense added successfully!
```

Handling invalid input:

```text
Enter amount: hello
Invalid amount.
Please enter a valid number.

Enter amount: -500
Amount must be greater than zero.

Enter amount: 150
```

## Example Output

Expense history:

```text
========== EXPENSE HISTORY ==========

1. Lunch
   Category: Food
   Amount: ₱150.00

2. Jeepney Fare
   Category: Transportation
   Amount: ₱30.00

3. Notebook
   Category: School
   Amount: ₱100.00
```

Total:

```text
========== EXPENSE SUMMARY ==========

Number of Expenses: 3
Total Spending: ₱280.00
```

Category summary:

```text
========== CATEGORY SUMMARY ==========

Food:            ₱150.00
Transportation:  ₱30.00
School:          ₱100.00

Total:           ₱280.00
```

## Python Concepts Demonstrated

- **Variables** — `total`, `amount`, `choice`, `label_width`
- **Lists** — `expenses` holds many expenses; `CATEGORIES` holds the allowed categories
- **Dictionaries** — one expense is a dictionary with labelled fields; `category_totals` maps a category name to a number
- **Loops** — `while` keeps the menu and the input prompts running; `for` walks through the expenses
- **Functions** — each feature is its own function with one job
- **Conditional statements** — `if` / `elif` / `else` route the menu choice and check for an empty list
- **User input** — `input()` reads text from the keyboard
- **Error handling** — `try` / `except ValueError` around `float()` and `int()`
- **Basic data analysis** — counting expenses, summing amounts, grouping totals by category
- **String formatting** — f-strings, `:,.2f` for two decimal places, `:<{width}` to line up columns

## Future Improvements

Ideas for after this version is understood:

- Save and load expenses from a file
- Delete or edit an expense
- Filter by category or date
- Add dates to each expense
- Move to a database, a GUI, or a web app
