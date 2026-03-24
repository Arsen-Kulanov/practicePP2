import csv
from connect import connect

def insert_csv(file):
    conn = connect()
    cur = conn.cursor()

    with open(file, "r") as f:
        reader = csv.reader(f)
        for x in reader:
            cur.execute(
                "INSERT INTO contacts (name, number) VALUES (%s, %s)", (x[0], x[1])
            )
    conn.commit()
    cur.close()
    conn.close()

def insert_console():
    name = input("User name: ")
    number = input("Phone number: ")

    conn = connect()
    cur = conn.cursor()
    
    cur.execute(
        """
        INSERT INTO contacts (name, number) VALUES (%s, %s)
        """, (name, number)
    )
    conn.commit()
    cur.close()
    conn.close()

def update():
    id = input("ID of user you want to update: ")
    new_name = input("New user name: ")
    new_number = input("New phone number: ")
    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute(
        """
        UPDATE contacts SET name = %s WHERE id = %s
        """, (new_name, id)
    )
    if new_number:
        cur.execute(
        """
        UPDATE contacts SET number = %s WHERE id = %s
        """, (new_number, id)
    )
    conn.commit()
    cur.close()
    conn.close()

def search_filter_contacts():
    print("1 - by name")
    print("2 - by phone prefix")
    choice = input()
    
    if choice == "1":
        name = input("Name: ")
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM contacts WHERE name LIKE %s
            """, ('%'+name+'%',)
        )

        print(cur.fetchall())
        cur.close()
        conn.close()
    else:
        prefix = input("Phone prefix: ")
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM contacts WHERE number LIKE %s
            """, (prefix + '%',)
        )

        print(cur.fetchall())
        cur.close()
        conn.close()

def delete():
    print("1 - by name")
    print("2 - by phone number")
    print("3 - by id")
    choice = input()

    if choice == "1":
        name = input("Name: ")
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            """
            DELETE FROM contacts WHERE name=%s
            """, (name,)
        )

        conn.commit()
        cur.close()
        conn.close()

    elif choice == "2":
        number = input("Phone number: ")
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            """
            DELETE FROM contacts WHERE number=%s
            """, (number,)
        )

        conn.commit()
        cur.close()
        conn.close()

    else:
        id = input("ID: ")
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            """
            DELETE FROM contacts WHERE id=%s
            """, (id)
        )
        
        conn.commit()
        cur.close()
        conn.close()

while True:
    print("1 - Add from CSV")
    print("2 - Add from console")
    print("3 - Update")
    print("4 - Search")
    print("5 - Delete")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_csv("Practice7/contacts.csv")
    elif choice == "2":
        insert_console()
    elif choice == "3":
        update()
    elif choice == "4":
        search_filter_contacts()
    elif choice == "5":
        delete()
    elif choice == "0":
        break
    else:
        print("Enter a valid number!")