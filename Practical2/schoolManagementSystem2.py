# Student, Teacher, Course classes

class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_details(self):
        print("Course:", self.course_name)
        print("Teacher:", self.teacher.name)
        print("Students:")
        for s in self.students:
            print("-", s.name)

# Example
t1 = Teacher("Mr. Sharma")
c1 = Course("Math", t1)

s1 = Student("Aman")
s2 = Student("Riya")

c1.add_student(s1)
c1.add_student(s2)

c1.show_details()
