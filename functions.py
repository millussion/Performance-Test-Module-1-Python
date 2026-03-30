#VALIDATION ID
def validation_id(students): #validates that the same ID is not registered again
    running = True
    while running:
        try:
            id_student = int(input("Enter the ID of the student 'Example: 12345': "))

            exist = False
            
            for student in students:
                if student['id'] == id_student:
                    exist = True
                
            if exist:
                print("This Student ID already exist.")
            else:
                return id_student
        except ValueError:
            print("Invalid ID")

#ADD NEW STUDENT
def add_student(students):
    id_student = validation_id(students)

    name = input("Enter the name of the student: ").upper() #upper makes everything capitalized
    age = int(input("Enter the age of the student: "))
    program = input("Enter the program or course of the student: ").upper()
    status = input("Are they Active or Inactive?: ").upper()

    while "ACTIVE" not in status:
        print("Invalid. ACTIVE or INACTIVE")
        status = input("Are they Active or Inactive?: ").upper()


    student = {
        "id": id_student,
        "name": name,
        "age": age,
        "program": program,
        "status": status
    }
    
    students.append(student)
    print(f"The Student {name} registered sucessfully")

#SHOW ALL OF THE STUDENTS
def show_students(students):
    if not students:
        print("The are not students to show.")
    else:
        print("\n" + "─" * 70)
        print(f"  {'ID':<22} {'NAME':>10} {'AGE':>10} {'PROGRAM':>10} {'STATUS':>10}")
        print("─" * 70)

        for student in students:
            print(f"  {student['id']:<22} {student['name']:>15} {student['age']:>4} {student['program']:>10} {student['status']:>10}")

        print("─" * 70)
        print(f"  Total of students: {len(students)}\n")

#SEARCH FOR AN ESPECIFIC STUDENT
def search_student(students):
    running = True
    while running:
        id_search = int(input("Enter the ID of the student: "))
        for student in students:
            if student['id'] == id_search:
                print("\n" + "─" * 70)
                print(f"  {'ID':<22} {'NAME':>10} {'AGE':>10} {'PROGRAM':>10} {'STATUS':>10}")
                print("─" * 70)

                
                print(f"  {student['id']:<22} {student['name']:>15} {student['age']:>4} {student['program']:>10} {student['status']:>11}")

                print("─" * 70)
                return student
        else:
            print("Student not found. Register and try again.")

#UPDATE A STUDENT
def update_stud(students):

    student = search_student(students) #the information searched here is stored in a variable and that's the one that gets edited

    new_name_stud = input("Enter the new name: ").upper()
    new_age_stud = int(input("Enter the new age of the student: "))
    new_program_stud = input("Enter the new program or course of the student: ").upper()
    new_status_stud = input("Are they Active or Inactive?: ").upper()

    student['name'] = new_name_stud
    student['age'] = new_age_stud
    student['program'] = new_program_stud
    student['status'] = new_status_stud

    print(f"Product '{new_name_stud}' updated.")
    return student

#DELETE A STUDENT FROM THE LIST
def delete_stud(students):

    student = search_student(students)

    students.remove(student) #the remove is a Python function that allows you to remove a value from a list
    print(f"The student {student['name']} are be deleted from the Data Base")


#SAVE FILE CSV
import csv

def save_csv(students):
    with open("List_of_Students.csv", "w") as file:
        writer = csv.writer(file) #the writer object

        writer.writerow(["ID", "        NAME", "         AGE", "PROGRAM", "STATUS"]) #titles

        for student in students: #each piece of information for a student is a row
            writer.writerow([
                student['id'],
                student['name'],
                student['age'],
                student['program'],
                student['status']
            ])

        print("Storage saved to List_of_Students.csv")

#UPLOAD THE FILE TO SAVE IT TO THE LIST
def load_csv(students):
    try:
        with open("List_of_Students.csv", "r") as file:
            reader = csv.reader(file)

            next(reader) #so that he doesn't get hold of the titles

            students.clear() #remove what's in students to avoid duplicates

            for everyline in reader:
                id, name, age, program, status = everyline #each value in the CSV file is separated into its variables
                students.append({
                    "id": int(id),
                    "name": name,
                    "age": int(age),
                    "program": program,
                    "status": status

                })

        print("Students loaded from List_of_Students.csv")

    except FileNotFoundError:
        print("File not found")