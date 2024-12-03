def input_number():
    return int(input("Enter number: "))

def input_information_student():
    students = []
    number_students = input_number()
    print("Enter the information of students: \n")
    for i in range (number_students):
        id = input("Input id: ")
        name = input("Input name ")
        date = input("Input DoB(dd/mm/yyyy): ")
        inforStudent = {'id':id,'name':name,'DoB':date}
        students.append(inforStudent)
    return students
    
def input_information_course():
    number_courses = input_number()
    courses = []
    print("Enter the information of courses: \n")
    for i in range (number_courses):
        id = input("Input id: ")
        name = input("Input name of course: ")
        inforCourses = {'id':id,'name':name}
        courses.append(inforCourses)
    return courses

def list_of_students(students):
    print("List of Students in class: \n")
    for student in students:
        print(f"Stundent ID: {student['id']}, Student Name: {student['name']}, DoB: {student['DoB']}")
            
def list_of_courses(courses):
    print("List of courses in class: \n")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def input_marks(students, courses, marks):
    list_of_courses(courses)
    print("Select the course id: ")
    course = input()
    if course not in marks:
        marks[course] = {}
    
    print(f"Enter marks for students in the course {course}: ")
    for student in students:
        print(f"Enter marks for {student}: ")
        student_marks = input()
        try:
            student_marks = float(student_marks)
        except ValueError:
            print("Invalid input. Please enter numeric marks.")
            continue

        marks[course][student] = student_marks
    print(f"Make have been recorded for the course {course}")

def print_marks(students, marks):
    course = input("What course do you want to find: ")

    if course not in marks or marks[course] == {}:
        print("Not found")
    else:
        for student in students:
            if(student['id'] in marks[course]):
                print("Student ID: {}, Mark: {}".format(student["id"], marks[course][student["id"]]))
            else:
                print("Student id : {}, Mark : Not entered".format(student["id"]))

marks = {}


while (True):
    print("---Enter your choice---")
    print("--0. Exit the program--")
    print("--1. Input students----")
    print("--2. Input courses-----")
    print("--3. Show list of courses------")
    print("--4. Show list of students-----")
    print("--5. Input marks--------")
    print("--6. Show mark---------\n")

    choice = int(input())
    if (choice == 0):
        break
    elif (choice == 1):
        students = input_number()
    elif (choice == 2):
        courses = input_number()
    elif (choice == 3):
        list_of_courses(courses)
    elif (choice == 4):
        list_of_students(students)
    elif (choice == 5):
        marks = input_marks(students,courses, marks)
    elif (choice == 6):
        print_marks(students, marks)
    else:
        print("Invalid choice")
