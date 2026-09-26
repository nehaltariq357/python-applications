import json

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
        
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,marks):
        if marks >=0:
            self.__marks = marks

        else:
            raise ValueError("Marks cannot be negative")

    def to_dict(self):
        return {
            "name":self.name,
            "roll_no":self.roll_no,
            "marks":self.__marks
        }


class StudentManager:

    def __init__(self):
        self.students = []
        self.load_student()

    def add_student(self,student):
        self.students.append(student)
        print("Student added")

    def remove_student(self,roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student removed")
                return 
        print("Student not found")

    def search_student(self,roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(student.name,student.roll_no,student.marks)
                return
        print("Student not found")

    def save_student(self):
        data = []
        for student in self.students:
            data.append(student.to_dict())

        with open("students.json","w") as file:
            json.dump(data,file)


    def load_student(self):
        try:
            with open("students.json","r") as file:
                data = json.load(file)

                for item in data:
                    student = Student(
                        item["name"],
                        item["roll_no"],
                        item["marks"],
                    )
                    self.students.append(student)
        except FileNotFoundError:
            pass

manager = StudentManager()

while True:
    print("1.Add")
    print("2.Search")
    print("3.Remove")
    print("4.Exit")

    try:
        choice = int(input("Choose: "))

        if choice == 1:
            name = input("Name: ")
            roll = int(input("Roll no: "))
            marks = int(input("Marks: "))

            student = Student(name, roll, marks)

            manager.add_student(student)

        

        elif choice == 2:

            roll = int(input("Roll no: "))
            manager.search_student(roll)


        elif choice == 3:

            roll = int(input("Roll no: "))
            manager.remove_student(roll)


        elif choice == 4:

            manager.save_student()
            print("Saved. Goodbye!")
            break


        else:
            print("Invalid choice")


    except ValueError as e:
        print(e)

    
        