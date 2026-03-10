# Expense Tracker

![Python](https://img.shields.io/badge/Python-3.8%2B-1f6feb?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Type-CLI-111827?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ea043?style=for-the-badge)

A beginner-friendly CLI-based personal expense tracker. Add, view, and calculate your expenses with simple text-based storage.

**Highlights**

- Add new expenses with date, category, amount, and description
- View all recorded expenses in a formatted list
- Calculate total expenses across all entries
- Data stored in a simple text file
- Clean command-line menu interface

**Tech**

- Python 3.8+

**Run**

```bash
python expense_tracker.py
```

**Menu Options**

```
====== Personal Expense Tracker ======
1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Exit
```

**Usage**

1. Select option 1 to add an expense (date: YYYY-MM-DD format)
2. Select option 2 to view all expenses
3. Select option 3 to see total spending
4. Select option 4 to exit

**Sample Session**

```
====== Personal Expense Tracker ======
1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Exit
Enter your choice: 1
Enter date (YYYY-MM-DD): 2024-01-15
Enter category: Food
Enter amount: 25.50
Enter description: Lunch at cafe
Expense added successfully!

Enter your choice: 3
Total Expenses: 25.5
```

**Data Storage**

- Expenses are stored in `expenses.txt` in CSV format
- Format: `date,category,amount,description`

**Project Structure**

- `expense_tracker.py` - Main script
- `expenses.txt` - Data file (created after adding first expense)
