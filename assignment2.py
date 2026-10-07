import pandas as pd
import os

file = "employee.csv"

if os.path.exists(file):
    df = pd.read_csv(file)
else:
    df = pd.DataFrame(columns=["id", "name", "salary", "department"])


def add_employee():
    global df

    id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    department = input("Enter department: ")

    new_employee = pd.DataFrame(
        [[id, name, salary, department]],
        columns=["id", "name", "salary", "department"]
    )

    df = pd.concat([df, new_employee], ignore_index=True)
    df.to_csv(file, index=False)

    print("Employee added successfully")


def display_employee():
    if df.empty:
        print("No records found")
    else:
        print(df)


def search_employee():
    id = int(input("Enter employee id: "))

    result = df[df["id"] == id]

    if result.empty:
        print("Employee not found")
    else:
        print(result)


def update_employee():
    global df

    id = int(input("Enter employee id: "))

    if id in df["id"].values:
        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))
        department = input("Enter new department: ")

        df.loc[df["id"] == id, "name"] = name
        df.loc[df["id"] == id, "salary"] = salary
        df.loc[df["id"] == id, "department"] = department

        df.to_csv(file, index=False)
        print("Employee updated successfully")
    else:
        print("Employee not found")


def delete_employee():
    global df

    id = int(input("Enter employee id: "))

    if id in df["id"].values:
        df = df[df["id"] != id]
        df.to_csv(file, index=False)
        print("Employee deleted successfully")
    else:
        print("Employee not found")


while True:
    print("\nEmployee Management")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_employee()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        print("Program ended")
        break
    else:
        print("Invalid choice")