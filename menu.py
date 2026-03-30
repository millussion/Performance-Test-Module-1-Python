from functions import *
students = []

def menu():
    running = True
    while running:
        print("\n WELCOME TO RIWI")
        print("1. Register Student")
        print("2. Show all registers")
        print("3. Search Student")
        print("4. Update Info")
        print("5. Delete Student")
        print("6. Save CSV")
        print("7. Load CSV")
        print("8. Exit")

        option = input("Select a option: ")

        if option == "1":
            add_student(students)
            print(students)
        elif option == "2":
            show_students(students)
        elif option == "3":
            search_student(students)
        elif option == "4":
            update_stud(students)
        elif option == "5":
            delete_stud(students)
        elif option == "6":
            save_csv(students)
        elif option == "7":
            load_csv(students)
            print(students)
        elif option == "8":
            print("Exiting...")
            running = False
        else:
            print("Invalid Option. Try from 1-8.")