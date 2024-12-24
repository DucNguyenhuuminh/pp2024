class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def __str__(self):
        return f"Student Name: {self.name}, DoB: {self.dob}"
    
class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(name,dob)
        self.id = student_id
        
    def __str__(self):
        return f"Student ID: {self.id}, {super().__str__()}"
    
    @classmethod
    def input(cls):
        id = input("Input Student ID: ")
        name = input("Input Student Name: ")
        Dob = input("Input DoB (dd/mm/yyyy): ")
        return cls(id,name,Dob)
    
class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.id}, Course Name: {self.name}"
    
    @classmethod
    def input(cls):
        id = input("Input Course ID: ")
        name = input("Input Coure Name: ")
        return cls(id,name)
    
class Mark:
    def __init__(self):
        self.marks_infor = {}
        
    def input(self, student, course):
        mark = float(input(f"Enter mark for student {student.id} in course {course.id}: "))
        if course.id not in self.marks_infor:
            self.marks_infor[course.id] = {}
        self.marks_infor[course.id][student.id] = mark
        
    def show(self, student, course):
        if course.id in self.marks_infor and student.id in self.marks_infor[course.id]:
            print(f"Student ID: {student.id}, Mark: {self.marks_infor[course.id],[student.id]}")
        else:
            print(f"Student ID: {student.id}, Mark: Not entered")

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def input_student(self):
        number_student = int(input("Enter number of students in class: "))
        for _ in range(number_student):
            student = Student.input()
            self.students.append(student)
            
    def input_course(self):
        number_course = int(input("Enter number of courses: "))
        for _ in range(number_course):
            course = Course.input()
            self.courses.append(course)

    def list_of_students(self):
        if not self.students:
            print("The list of students is empty. Please, enter the information of students in class. \n")
        else:
            print("List of Students in class: \n")
            for student in self.students:
                print(student)

    def list_of_courses(self):
        if not self.courses:
            print("The list of courses is empty. Please, enter the information of courses in class. \n")
        else:
            print("List of courses in class: \n")
            for course in self.courses:
                print(course)

    def input_marks(self):
        self.list_of_courses()
        course_id = input("Select the course ID: ")
        selected_course = next((course for course in self.courses if course.id == course_id), None)
        
        if not selected_course:
            print("Course ID not found!\n")
            return
        
        self.list_of_students()
        student_id = input("Select the student ID to input marks: ")
        selected_student = next((student for student in self.students if student.id == student_id), None)
        
        if not selected_student:
            print("Student ID not found!")
            return
        
        self.marks.input_marks(selected_course,selected_student)
        
    def print_marks(self):
        course_id = input("What course do you want to find: ")

        if course_id not in self.marks or not self.marks[course_id]:
            print("Not found")
        else:
            for student in self.students:
                mark = self.marks[course_id].get(student.id, "Not entered")
                print(f"Student ID: {student.id}, Mark: {mark}")


def main():
    school = School()

    while True:
        print("\n----------------------")
        print(" Enter your choice ")
        print("----------------------")
        print("|0. Exit the program |")
        print("|1. Input students   |")
        print("|2. Input courses    |")
        print("|3. List of students |")
        print("|4. List of courses  |")
        print("|5. Input marks      |")
        print("|6. Show mark        |")
        print("----------------------\n")
        

        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            school.input_student()
        elif choice == 2:
            school.input_course()
        elif choice == 4:
            school.list_of_courses()
        elif choice == 3:
            school.list_of_students()
        elif choice == 5:
            school.input_marks()
        elif choice == 6:
            school.print_marks()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
