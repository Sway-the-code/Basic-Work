import pickle

FILENAME = "employees.dat"

# Function to add an employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    emp_data = {'ID': emp_id, 'Name': name, 'Salary': salary}
    
    try:
        with open(FILENAME, "ab") as file:
            pickle.dump(emp_data, file)
        print("Employee added successfully!\n")
    except Exception as e:
        print("Error while adding employee:", e)

# Function to display all employees
def display_employees():
    try:
        with open(FILENAME, "rb") as file:
            print("\nEmployee Records:")
            while True:
                try:
                    emp_data = pickle.load(file)
                    print(emp_data)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found!")

# Function to search for an employee
def search_employee(emp_id):
    try:
        with open(FILENAME, "rb") as file:
            while True:
                try:
                    emp_data = pickle.load(file)
                    if emp_data['ID'] == emp_id:
                        print("Employee Found:", emp_data)
                        return
                except EOFError:
                    break
        print("Employee not found!")
    except FileNotFoundError:
        print("No records found!")

# Function to update an employee
def update_employee(emp_id):
    employees = []
    updated = False
    try:
        with open(FILENAME, "rb") as file:
            while True:
                try:
                    emp_data = pickle.load(file)
                    if emp_data['ID'] == emp_id:
                        emp_data['Name'] = input("Enter new name: ")
                        emp_data['Salary'] = float(input("Enter new salary: "))
                        updated = True
                    employees.append(emp_data)
                except EOFError:
                    break
        with open(FILENAME, "wb") as file:
            for emp in employees:
                pickle.dump(emp, file)
        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee not found!")
    except FileNotFoundError:
        print("No records found!")

# Function to delete an employee
def delete_employee(emp_id):
    employees = []
    deleted = False
    try:
        with open(FILENAME, "rb") as file:
            while True:
                try:
                    emp_data = pickle.load(file)
                    if emp_data['ID'] != emp_id:
                        employees.append(emp_data)
                    else:
                        deleted = True
                except EOFError:
                    break
        with open(FILENAME, "wb") as file:
            for emp in employees:
                pickle.dump(emp, file)
        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")
    except FileNotFoundError:
        print("No records found!")

# Menu
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            search_employee(emp_id)
        elif choice == '4':
            emp_id = input("Enter Employee ID to update: ")
            update_employee(emp_id)
        elif choice == '5':
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(emp_id)
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the menu

menu()
