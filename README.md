# Performance Test – Module 1 Python

# Description
This project is a console-based student management system with data persistence developed in Python. It allows users to add, manage, edit, and delete students using CRUD operations and store the data in CSV files.

Running the program means starting it and depending on what the user wants to do, they will enter a option.

---
## Objective
The main objectives of this project are:
- To manage students using lists and dictionaries
- To implement CRUD operations (Create, Read, Update, Delete)
- To implement file persistence using CSV files
- To handle errors and validate user input
- To structure the code using functions and modules

## Functions

### CRUD Operations
- Add new students (ID, name, age, program and status)
- Show all registered students
- Search for a student by ID
- Update student information
- Delete students from the registry
  
### Data Persistence

#### Saving Data to a CSV File
- Exports the record to a CSV file (`List_of_Students.csv`)
- Includes headers: id, name, age, program and status
- Writes all student data in a structured format

#### Loading Data
- Reads the data from the CSV file
- Converts values ​​to the correct data type
- Deletes the current record before loading
- Handles errors such as missing files

## Data Structure

The record is stored as a list of dictionaries in a list.

Each student record contains:
- ID
- name
- age
- program
- status (ACTIVE/INACTIVE)

## Menu Options

The system is designed to display a menu with options such as:

1. Register Student
2. View All Registers
3. Search Student
4. Update Info
5. Delete Student
6. Save CSV
7. Load CSV
8. Exit


# Examples 

## Menu
 WELCOME TO RIWI
1. Register Student
2. Show all Students
3. Search Student
4. Update Info
5. Delete Student
6. Save CSV
7. Load CSV
8. Exit
Select a option:

## 1. Register Client
<img width="578" height="430" alt="image" src="https://github.com/user-attachments/assets/739ebdd1-45a7-4ce0-aaeb-dca34bff0025" />

## 2. Show all Students
<img width="559" height="353" alt="image" src="https://github.com/user-attachments/assets/d31c3d09-59f7-4757-8e2e-305f747a1ee2" />
  
## 3. Search Student
<img width="559" height="353" alt="image" src="https://github.com/user-attachments/assets/59a54825-a297-481d-ac0a-c4e20bd6c1f4" />

## 4. Update Info
<img width="570" height="457" alt="image" src="https://github.com/user-attachments/assets/cacefe0e-76d8-47b7-a527-75aae95f20c0" />

## 5. Delete Student
<img width="570" height="371" alt="image" src="https://github.com/user-attachments/assets/23731f98-77ea-4b8c-9417-fd5122209bb6" />

# Flow Chart 
![Pruebadedesempeño](https://github.com/user-attachments/assets/6c332105-ea6b-4f71-b5a5-dbf386c44619)
