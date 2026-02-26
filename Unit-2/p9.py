students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    students[roll] = name
    print("Student Added Successfully!")

def search_student():
    roll = input("Enter Roll No to Search: ")
    if roll in students:
        print("Student Found:", students[roll])
    else:
        print("Student Not Found!")

def list_students():
    if not students:
        print("No Students Available!")
    else:
        for roll, name in students.items():
            print("Roll No:", roll, "Name:", name)

def update_student():
    roll = input("Enter Roll No to Update: ")
    if roll in students:
        name = input("Enter New Name: ")
        students[roll] = name
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll No to Delete: ")
    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

while True:
    print("\n----- Student Menu -----")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter Choice: ")

    if choice == 'a':
        add_student()
    elif choice == 'b':
        search_student()
    elif choice == 'c':
        list_students()
    elif choice == 'd':
        update_student()
    elif choice == 'e':
        delete_student()
    elif choice == 'f':
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
