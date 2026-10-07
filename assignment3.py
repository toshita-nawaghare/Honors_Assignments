import sqlite3


class Employee:

    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY,
            name TEXT,
            salary REAL,
            department TEXT
        )
        """)

        self.con.commit()

    def add(self):
        id = int(input("Enter employee id: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        self.cur.execute(
            "INSERT INTO employee VALUES (?, ?, ?, ?)",
            (id, name, salary, department)
        )

        self.con.commit()
        print("Employee added successfully")

    def display(self):
        self.cur.execute("SELECT * FROM employee")
        records = self.cur.fetchall()

        if len(records) == 0:
            print("No records found")
        else:
            for row in records:
                print(row)

    def search(self):
        id = int(input("Enter employee id: "))

        self.cur.execute(
            "SELECT * FROM employee WHERE id=?",
            (id,)
        )

        record = self.cur.fetchone()

        if record:
            print(record)
        else:
            print("Employee not found")

    def update(self):
        id = int(input("Enter employee id: "))

        self.cur.execute(
            "SELECT * FROM employee WHERE id=?",
            (id,)
        )

        record = self.cur.fetchone()

        if record:
            name = input("Enter new name: ")
            salary = float(input("Enter new salary: "))
            department = input("Enter new department: ")

            self.cur.execute("""
            UPDATE employee
            SET name=?, salary=?, department=?
            WHERE id=?
            """, (name, salary, department, id))

            self.con.commit()
            print("Employee updated successfully")
        else:
            print("Employee not found")

    def delete(self):
        id = int(input("Enter employee id: "))

        self.cur.execute(
            "DELETE FROM employee WHERE id=?",
            (id,)
        )

        self.con.commit()

        if self.cur.rowcount > 0:
            print("Employee deleted successfully")
        else:
            print("Employee not found")


obj = Employee()

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
        obj.add()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.search()
    elif choice == 4:
        obj.update()
    elif choice == 5:
        obj.delete()
    elif choice == 6:
        print("Program ended")
        break
    else:
        print("Invalid choice")