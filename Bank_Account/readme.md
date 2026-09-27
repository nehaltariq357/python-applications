# 🏦 Bank Account Management System

A simple **console-based Bank Account Management System** built with Python.

This project demonstrates core Python concepts including **Object-Oriented Programming (OOP), custom exceptions, exception handling, file handling, persistent data storage, and transaction logging with timestamps**.

## 🚀 Features

- Deposit money into the account
- Withdraw money from the account
- Check current balance
- Prevent negative or zero deposits/withdrawals
- Prevent withdrawals greater than the available balance
- Custom exception handling
- Save current balance to a file
- Restore previous balance when the program starts again
- Save transaction history
- Add timestamps to every transaction
- Handle invalid user input without crashing
- Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Python `datetime` module
- File Handling
- Object-Oriented Programming

No external packages are required.

---

## 📚 Python Concepts Used

### Object-Oriented Programming

The project uses a `BankAccount` class to manage account operations.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.load_balance()
```

The class contains methods for:

- Depositing money
- Withdrawing money
- Checking balance
- Saving transactions
- Saving balance
- Loading previous balance

---

## ⚠️ Custom Exceptions

The project defines custom exceptions for handling banking errors.

### InvalidAmountError

Raised when the user enters zero or a negative amount.

```python
class InvalidAmountError(Exception):
    pass
```

Example:

```text
Enter a deposit amount: -500
Amount must be greater than 0
```

### InsufficeintFundsError

Raised when the withdrawal amount is greater than the available balance.

```python
class InsufficeintFundsError(Exception):
    pass
```

Example:

```text
Current Balance: 1000
Withdraw: 2000

Insufficient fund
```

---

## 💰 Deposit Money

The `deposite()` method validates the amount before adding it to the balance.

```python
def deposite(self, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0")

    self.balance += amount
    self.save_balance()

    self.save_transaction(
        f"Deposite: {amount}, Balance: {self.balance}"
    )
```

After a successful deposit, the updated balance is saved automatically.

---

## 💸 Withdraw Money

The `withdraw()` method checks both the amount and available balance.

```python
def withdraw(self, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0")

    if amount > self.balance:
        raise InsufficeintFundsError("Insufficient fund")

    self.balance -= amount
    self.save_balance()

    self.save_transaction(
        f"Withdraw: {amount}, Balance: {self.balance}"
    )
```

---

## 💾 Balance Persistence

The current balance is stored in:

```text
balance.txt
```

For example:

```text
1500
```

Whenever a deposit or withdrawal is successful, the balance is saved using:

```python
def save_balance(self):
    with open("balance.txt", "w") as file:
        file.write(str(self.balance))
```

When the application starts again, the previous balance is restored:

```python
def load_balance(self):
    try:
        with open("balance.txt", "r") as file:
            self.balance = int(file.read())

    except FileNotFoundError:
        pass

    except ValueError:
        print("Invalid balance file. Using default balance.")
```

This means the balance is not reset every time the program is restarted.

---

## 📝 Transaction History

Every successful deposit and withdrawal is stored in:

```text
transactions.txt
```

Transactions are saved using append mode (`"a"`), so previous transactions are not overwritten.

Example:

```text
Deposite: 500, Balance: 1500 - 2026-09-27 18:30:20
Withdraw: 200, Balance: 1300 - 2026-09-27 18:31:42
Deposite: 1000, Balance: 2300 - 2026-09-27 18:35:10
```

---

## ⏰ Transaction Timestamps

Python's `datetime` module is used to generate timestamps:

```python
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

Format:

```text
YYYY-MM-DD HH:MM:SS
```

This allows each transaction to record when it occurred.

---

## 🖥️ Menu

When the application starts:

```text
1.Deposite
2.Withdraw
3.Check Balance
4.Exit
```

The menu continues running until the user selects option `4`.

---

## 🛡️ Exception Handling

The application handles multiple types of errors:

```python
except ValueError:
    print("Please enter a valid number.")

except InvalidAmountError as e:
    print(e)

except InsufficeintFundsError as e:
    print(e)
```

This prevents invalid user input from crashing the application.

---

## 📂 Project Structure

```text
Bank_Account/
│
├── app.py
├── balance.txt
├── transactions.txt
└── README.md
```

`balance.txt` stores the latest balance.

`transactions.txt` stores the complete transaction history.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project directory

```bash
cd Bank_Account
```

### 3. Run the application

```bash
python app.py
```

---

## 🔄 Application Flow

```text
Start Program
      ↓
Create BankAccount
      ↓
Load Previous Balance
      ↓
Display Menu
      ↓
 ┌───────────────┐
 │ Deposit       │
 │ Withdraw      │
 │ Check Balance │
 │ Exit          │
 └───────────────┘
      ↓
Validate Input
      ↓
Perform Operation
      ↓
Save Balance
      ↓
Log Transaction + Timestamp
      ↓
Return to Menu
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Python classes and objects
- Object-Oriented Programming
- Methods and constructors
- Custom exceptions
- `raise`
- `try` / `except`
- File handling
- Read, write, and append modes
- Persistent data storage
- Transaction logging
- Working with `datetime`
- Menu-driven programs
- Input validation

---
