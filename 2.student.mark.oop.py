class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"Student ID: {self.id}, Student Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.id}, Course Name: {self.name}"


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number(self, messange):
        return int(input(messange))

    def input_information_student(self):
        number_students = self.input_number("Enter number of students: ")
        print("Enter the information of students: \n")
        for _ in range(number_students):
            student_id = input("Input id: ")
            name = input("Input name: ")
            dob = input("Input DoB (dd/mm/yyyy): ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_information_course(self):
        number_courses = self.input_number("Enter number of courses: ")
        print("Enter the information of courses: \n")
        for _ in range(number_courses):
            course_id = input("Input id: ")
            name = input("Input name of course: ")
            course = Course(course_id, name)
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
        course_id = input("Select the course id: ")
        if course_id not in self.marks:
            self.marks[course_id] = {}

        self.list_of_students()
        student_id = input("Select the student ID to input mark: ")

        self.marks[course_id][student_id] = float(input("Enter mark of student: "))

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
        print("\n---Enter your choice---")
        print("--0. Exit the program--")
        print("--1. Input students----")
        print("--2. Input courses-----")
        print("--3. Show list of courses------")
        print("--4. Show list of students-----")
        print("--5. Input marks--------")
        print("--6. Show mark---------\n")

        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            school.input_information_student()
        elif choice == 2:
            school.input_information_course()
        elif choice == 3:
            school.list_of_courses()
        elif choice == 4:
            school.list_of_students()
        elif choice == 5:
            school.input_marks()
        elif choice == 6:
            school.print_marks()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
