# Python Control Flow Assignment

## Student Name

**Muskan Dewangan**

## Overview

This assignment focuses on practicing fundamental Python control-flow concepts through order-processing and sales-processing programs.

The programs demonstrate the use of:

* `if`
* `elif`
* `else`
* `for` loops
* `while` loops
* `break`
* `continue`
* Lists
* `input()`
* Integer type conversion
* Basic arithmetic
* Basic error handling using `try` and `except`

---

## Folder Structure

```text
Python -Control Flow(Conditionals & Loops)/
│
├── discount_rules.py
├── process_multiple_orders.py
├── user_menu.py
├── loop_control.py
└── README.md
```

---

# Discount Rules

### File

`discount_rules.py`

### Description

The program accepts an order amount from the user and applies a discount according to the following rules:

| Order Amount | Discount |
| ------------ | -------: |
| 2000 or more |      15% |
| 1500 to 1999 |      10% |
| 1000 to 1499 |       7% |
| Below 1000   |       0% |

The program also:

* Converts the input into an integer.
* Handles non-numeric input.
* Displays an error message for invalid input.
* Calculates the discount amount.
* Calculates the final amount.

### Run

```text
python discount_rules.py
```

---

# Process Multiple Orders

### File

`process_multiple_orders.py`

### Description

The program processes the following orders:

```text
[1200, 2500, 800, 1750, 3000]
```

A `for` loop is used to:

* Process every order.
* Apply the correct discount.
* Calculate the final amount.
* Display a summary table.
* Calculate total revenue after discounts.

### Run

```text
python process_multiple_orders.py
```

### Expected Total Revenue

```text
8166.0
```

---

# User Menu

### File

`user_menu.py`

### Menu

```text
1 - Add order amount
2 - Show all orders and totals after applying discounts
q - Quit
```

### Description

The program uses a `while` loop to repeatedly display the menu.

* Option `1` adds an order to the list.
* Option `2` displays all orders, discounts, final amounts, and total revenue.
* `q` exits the program using `break`.
* Invalid input uses `continue` to return to the menu.
* Invalid numeric order input is handled using `try` and `except`.

### Run

```text
python user_menu.py
```

---

# Loop Control with Conditions

### File

`loop_control.py`

### Daily Sales Data

```text
[200, 150, 0, 400, 50, -1, 300]
```

### Rules

* `-1` represents corrupted data.
* When `-1` is found, `break` stops the loop.
* `0` represents a day with no sales.
* `continue` skips the zero-sales day.
* Positive sales are added to the running total.

### Run

```text
python loop_control.py
```

### Expected Final Total

```text
Final Total Sales: 800
```

The value `300` is not processed because the loop stops when `-1` is encountered.

---

# Requirements and Restrictions

## Concepts Used

* Conditional statements
* `for` loop
* `while` loop
* `break`
* `continue`
* Lists
* `input()`
* Integer conversion
* `try` / `except`
* Basic arithmetic

## Restrictions Followed

The assignment programs do not use:

* User-defined functions
* Classes
* External libraries
* File operations

---

# How to Run the Assignment

### Step 1

Install Python 3 on your computer.

### Step 2

Open Command Prompt or Terminal.

### Step 3

Navigate to the assignment folder.

```text
cd Python-Control-Flow-Assignment

```

### Step 4

Run each task separately.

#### Task 1

```text
python discount_rules.py
```

#### Task 2

```text
python process_multiple_orders.py
```

#### Task 3

```text
python user_menu.py
```

#### Task 4

```text
python loop_control.py
```

---

# Submission Instructions

All Python files and `README.md` must be placed inside the main assignment folder:

```text
Python-Control-Flow-Assignment/
```

The complete folder should be compressed into **ZIP format**.

The ZIP file can then be uploaded to the assignment submission portal.

---

## Final Verification

Before submission, verify that:

* Task 1 handles invalid/non-numeric input.
* Task 1 calculates discounts correctly.
* Task 2 applies discounts inside the loop.
* Task 2 calculates total revenue correctly.
* Task 3 uses `continue` for invalid input.
* Task 3 uses `break` when `q` is entered.
* Task 4 uses `sale == -1` for corrupted data.
* `README.md` explains how to run every task.

