from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        pass

    def area(self):
        return 3.14 * self.radius ** 2
        

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self,width,heigth):
        self.width = width
        self.heigth = heigth
    def area(self):
        return self.width * self.heigth
    def perimeter(self):
        return 2 * (self.width + self.heigth)

class Triangle(Shape):
    def __init__(self,side1,side2,side3,base,height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
        

