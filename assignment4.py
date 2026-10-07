import sqlite3

con = sqlite3.connect("employee2.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL,
    department TEXT
)
""")

con.commit()


def add_employee():
    id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    department = input("Enter department: ")

    cur.execute(
        "INSERT INTO employee VALUES (?, ?, ?, ?)",
        (id, name, salary, department)
    )

    con.commit()
    print("Employee added successfully")


def display_employee():
    cur.execute("SELECT * FROM employee")
    records = cur.fetchall()

    if len(records) == 0:
        print("No records found")
    else:
        for record in records:
            print(record)


def search_employee():
    id = int(input("Enter employee id: "))

    cur.execute(
        "SELECT * FROM employee WHERE id=?",
        (id,)
    )

    record = cur.fetchone()

    if record:
        print(record)
    else:
        print("Employee not found")


def update_employee():
    id = int(input("Enter employee id: "))

    cur.execute(
        "SELECT * FROM employee WHERE id=?",
        (id,)
    )

    record = cur.fetchone()

    if record:
        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))
        department = input("Enter new department: ")

        cur.execute("""
        UPDATE employee
        SET name=?, salary=?, department=?
        WHERE id=?
        """, (name, salary, department, id))

        con.commit()
        print("Employee updated successfully")
    else:
        print("Employee not found")


def delete_employee():
    id = int(input("Enter employee id: "))

    cur.execute(
        "DELETE FROM employee WHERE id=?",
        (id,)
    )

    con.commit()

    if cur.rowcount > 0:
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

con.close()