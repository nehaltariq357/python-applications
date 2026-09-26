# Student Management System

A simple **console-based Student Management System** built with Python.
This project demonstrates **Object-Oriented Programming (OOP)** concepts like classes, encapsulation, properties, file handling, and exception handling.

## 🚀 Features

* Add new students
* Search students by roll number
* Remove students
* Store student data permanently using JSON file
* Load saved students automatically when the program starts
* Validate marks using encapsulation
* Handle invalid inputs with exception handling

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)
* Object-Oriented Programming (OOP)

---

## 📚 Concepts Implemented

### 1. Classes and Objects

The project uses two main classes:

### Student Class

Represents a student with:

* Name
* Roll number
* Marks

Example:

```python
student = Student("Ali", 101, 90)
```

---

### StudentManager Class

Handles student operations:

* Adding students
* Removing students
* Searching students
* Saving and loading data

---

## 🔒 Encapsulation

Marks are stored as a private attribute:

```python
self.__marks
```

Direct access is restricted.

A `@property` getter and setter are used:

### Getter

```python
@property
def marks(self):
    return self.__marks
```

Used to access marks safely.

### Setter

```python
@marks.setter
def marks(self, marks):
    if marks >= 0:
        self.__marks = marks
    else:
        raise ValueError("Marks cannot be negative")
```

Used to validate and update marks.

---

## 💾 Data Storage

Student data is saved in:

```
students.json
```

The program converts student objects into dictionaries before saving.

Example JSON format:

```json
[
    {
        "name": "Ali",
        "roll_no": 101,
        "marks": 90
    }
]
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to project folder

```bash
cd student-management-system
```

### 3. Run the program

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Add
2. Search
3. Remove
4. Exit
```

### Add Student

Enter:

```
Name: Ali
Roll no: 101
Marks: 90
```

Student will be added.

---

### Search Student

Enter roll number:

```
Roll no: 101
```

Output:

```
Ali 101 90
```

---

### Remove Student

Enter roll number:

```
Roll no: 101
```

Student will be removed.

---

### Exit

Before closing, all students are automatically saved:

```
Saved. Goodbye!
```

---

## 🧠 Error Handling

The program handles:

* Negative marks

Example:

```
Marks cannot be negative
```

* Invalid user input

Example:

```
ValueError
```

* Missing JSON file

The program creates/loads data safely without crashing.

---

## 📂 Project Structure

```
Student-Management-System/
│
├── main.py
├── students.json
└── README.md
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python OOP
* Encapsulation
* Getter and Setter using `@property`
* File handling
* JSON serialization/deserialization
* Exception handling
* Working with classes and objects

---


