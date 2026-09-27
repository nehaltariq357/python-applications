# 🐍 Python Applications

A collection of Python applications built to practice and demonstrate **Python fundamentals, Object-Oriented Programming (OOP), file handling, exception handling, abstraction, inheritance, polymorphism, and persistent data storage**.

This repository contains multiple small projects, with each project focusing on different Python concepts and practical problem-solving.

---

## 📂 Projects

### 🏦 1. Bank Account System

A console-based banking application that supports basic account operations while demonstrating **custom exceptions, file handling, and persistent data storage**.

#### Features

- Deposit money
- Withdraw money
- Check current balance
- Custom exception handling
- Prevent negative or zero transactions
- Prevent withdrawal when funds are insufficient
- Save current balance to a file
- Restore previous balance when the program starts again
- Store transaction history
- Add timestamps to transactions
- Menu-driven interface
- Invalid input handling

#### Concepts Practiced

`OOP` • `Classes` • `Custom Exceptions` • `raise` • `try/except` • `File Handling` • `datetime` • `Data Persistence`

#### Project Directory

```text
Bank_Account/
```

---

### 📐 2. Shape Calculator

An OOP-based shape calculator that calculates the **area and perimeter** of different shapes.

The project demonstrates how multiple classes can share a common interface using **abstraction, inheritance, and polymorphism**.

#### Supported Shapes

- Circle
- Rectangle
- Triangle

#### Features

- Calculate area
- Calculate perimeter
- Abstract `Shape` base class
- Abstract `area()` and `perimeter()` methods
- Process different shape objects through the same interface
- Print calculation results
- Save results to a text file

#### Concepts Practiced

`Abstraction` • `ABC` • `@abstractmethod` • `Inheritance` • `Method Overriding` • `Polymorphism` • `File Handling`

#### Project Directory

```text
shape_calculator/
```

---

### 🎓 3. Student Management System

A console-based application for managing student records.

The project uses **encapsulation and properties** to protect student marks and JSON to store student information.

#### Features

- Add students
- Search students by roll number
- Remove students
- Store student records in JSON
- Automatically load saved students on startup
- Encapsulated marks
- Validate marks
- Prevent negative marks
- Exception handling
- Menu-driven interface

#### Concepts Practiced

`OOP` • `Encapsulation` • `@property` • `Getter/Setter` • `JSON` • `File Handling` • `Exception Handling`

#### Project Directory

```text
student_management_system/
```

---

## 🧠 Python Concepts Covered

Across these projects, I practiced several important Python concepts:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Classes and objects
- Constructors
- Encapsulation
- Properties and setters
- Inheritance
- Abstraction
- Abstract classes
- Abstract methods
- Method overriding
- Polymorphism
- Custom exceptions
- `raise`
- `try / except`
- File handling
- JSON serialization and deserialization
- Persistent data storage
- Working with timestamps using `datetime`

---

## 📁 Repository Structure

```text
python-applications/
│
├── Bank_Account/
│   ├── app.py
│   ├── balance.txt
│   ├── transactions.txt
│   └── README.md
│
├── shape_calculator/
│   ├── app.py
│   ├── shape_results.txt
│   └── README.md
│
├── student_management_system/
│   ├── app.py
│   ├── students.json
│   └── README.md
│
└── README.md
```

Each project has its own README with more information about its implementation.

---

## ▶️ Running the Projects

### Clone the repository

```bash
git clone https://github.com/nehaltariq357/python-applications.git
```

Move into the repository:

```bash
cd python-applications
```

Then open the project you want to run.

For example:

```bash
cd Bank_Account
python app.py
```

Or:

```bash
cd shape_calculator
python app.py
```

Or:

```bash
cd student_management_system
python app.py
```

> Python 3 is required. These projects use Python's standard library, so no additional packages are required.

---

## 🎯 Purpose of This Repository

The purpose of this repository is to document my progress while learning Python through practical applications.

Instead of only studying individual concepts, these projects combine multiple concepts into working programs.

The repository currently focuses on strengthening:

**Python Fundamentals → OOP → Exception Handling → File Handling → Data Persistence**

More Python projects will be added as I continue learning.

---