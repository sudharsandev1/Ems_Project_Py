# function to add employees 
employees={}

def add_employee(emp_id, name, age,salary,depatment):

    employees[emp_id]={
        "Name": name,
        "Age" : age,
        "Salary": salary,
        "Department":depatment
    }
    

    print (f" Employee {name} added succesfully !")
# func - view employees...
def view_employee():
    if employees:
        for emp_id , emp_details in employees.items():
            print(f"\nID :{ emp_id} ,Details :{ emp_details}")
    else:
        print("\n No Employees added Yet !!")

#func - update employees
def update_employee(emp_id, name=None, age=None,salary=None,depatment=None):
    try : 
        if emp_id in employees:
            if name:
                employees[emp_id]['Name'] =name
            if age :
                employees [emp_id]['Age'] =age
            if salary :
                employees [emp_id] ['salary'] =salary
            if depatment:
                employees [emp_id] ['department']=depatment
        else:
            print(f"Employees With ID {emp_id} not found !!")
    except KeyError as e:
        print(f"Error Updating Employee Details :{e}")

#func -   remove
def remove_employee(emp_id):
    try:
        emp =employees.pop(emp_id)
        print(f"Employees {emp['Name']} Removed Succesfully")
    except KeyError:
        print(f" Empoyee with Id {emp_id} not found")


def save_to_file(filename):
    try:

        with open(filename,"w") as file:
            for emp_id,details in employees.items():
                line=f"{emp_id}:-> {details['Name']} {details['Age']}{details['Salary']}{details['Department']}\n"
        print ("Employees data is saved successfully")
    except Exception as e:
        print(f"Error :{e}")

def load_from_file(filename):
    try:
        with open(filename,"w") as file:
            global employees
            employees ={}
            for line in file:
                emp_data =line.strip().split(',')
                emp_id,name,age,salary,department =emp_data
                employees[emp_id]={
                    "Name":name,
                    "Age":age,
                    "Salary":salary,
                    "Department":department
                }
        print("Employees data  load  succesfully")
    except FileNotFoundError:
        print(f"file {filename} not found")


def menu():




    while True:
        print("Welcome To The Employee Management System:")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save to File")
        print("6. Load from file")
        print("7. Exit")


        choice=input("Enter Your Choice :")

        if choice =="1":
            emp_id= input("Enter Employee Id:")
            name=input("Enter Employee Name :")
            age =input("Enter Employee Age :")
            salary =input(" Enter Employee salary :")
            depatment =input(" Enter Department :")
            add_employee( emp_id, name, age,salary,depatment)


        elif choice=="2":
            view_employee()

        elif choice=="3":
            emp_id =input("Enter Employee ID is update :")
            name =input("Enter Your Name (Leave Blank to Skip):")or None
            age =input("Enter Your age (Leave Blank to Skip):")or None
            salary =input("Enter Your salary (Leave Blank to Skip):")or None
            depatment =input("Enter Your department (Leave Blank to Skip):")or None
            update_employee(emp_id, name, age,salary,depatment)

        elif choice=="4":
            emp_id =input("Enter Employee  ID to Remove :")
            remove_employee(emp_id)

        elif choice=="5":
            filename =input("Enter filename to save to")
            save_to_file(filename)

        elif choice=="6":
            filename =input("Enter File name to load from : ")
            load_from_file(filename)

        elif choice=="7":
            break



menu()