# 📐 Shape Calculator

A simple **Shape Calculator** built with Python using Object-Oriented Programming.

This project demonstrates important OOP concepts including **abstraction, inheritance, polymorphism, abstract methods, and file handling**.

## 🚀 Features

- Calculate the area of different shapes
- Calculate the perimeter of different shapes
- Support multiple shape types
- Process mixed shape objects using polymorphism
- Display results in the console
- Save calculated results to a text file

---

## 🛠️ Technologies Used

- Python 3
- Python `abc` module
- Object-Oriented Programming
- File Handling

No external packages are required.

---

## 📚 Concepts Used

### 1. Abstraction

The project contains an abstract `Shape` class:

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

Every subclass of `Shape` must implement:

- `area()`
- `perimeter()`

---

## 🔵 Circle

The `Circle` class calculates the area and perimeter of a circle.

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
```

Example:

```python
Circle(5)
```

---

## ▭ Rectangle

The `Rectangle` class calculates area and perimeter using width and height.

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

---

## 🔺 Triangle

The `Triangle` class uses base and height for area calculation and three sides for perimeter calculation.

```python
class Triangle(Shape):
    def __init__(self, side1, side2, side3, base, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
```

---

## 🔄 Polymorphism

Different shape objects are stored in the same list:

```python
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5, 4, 5)
]
```

The program processes all objects using the same methods:

```python
for shape in shapes:
    shape.area()
    shape.perimeter()
```

Even though the objects belong to different classes, Python automatically executes the correct `area()` and `perimeter()` implementation.

This demonstrates **polymorphism**.

---

## 💾 File Handling

The calculated results are stored in:

```text
shape_results.txt
```

The program creates the file using:

```python
with open("shape_results.txt", "w") as file:
    file.write(result)
```

Example output:

```text
Shape: Circle
Area: 78.5
Perimeter: 31.400000000000002
------------------

Shape: Rectangle
Area: 24
Perimeter: 20
------------------

Shape: Triangle
Area: 10.0
Perimeter: 12
------------------
```

---

## 📂 Project Structure

```text
Shape-Calculator/
│
├── app.py
├── shape_results.txt
└── README.md
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Shape-Calculator
```

Run the Python program:

```bash
python app.py
```

The results will be displayed in the terminal and saved in `shape_results.txt`.

---

## 🔄 Program Flow

```text
Create Shape Objects
        ↓
Store Objects in List
        ↓
calculate_shape(shapes)
        ↓
Loop Through Shapes
        ↓
shape.area()
shape.perimeter()
        ↓
Polymorphism
        ↓
Print Results
        ↓
Save Results to File
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Python Classes and Objects
- Object-Oriented Programming
- Abstract Base Classes
- `ABC`
- `@abstractmethod`
- Abstraction
- Inheritance
- Method Overriding
- Polymorphism
- File Handling
- Working with mixed objects in a list

---