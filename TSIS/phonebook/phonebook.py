from connect import connect
import csv
import json


def search(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

def search_by_email():
    pattern = input("Enter email pattern: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, email
        FROM contacts
        WHERE email ILIKE %s
    """, (f"%{pattern}%",))

    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

def sort_contacts():
    print("1 - name")
    print("2 - birthday")

    choice = input("Sort by: ")

    if choice == "1":
        column = "name"
    elif choice == "2":
        column = "birthday"

    conn = connect()
    cur = conn.cursor()

    cur.execute(f"SELECT name, email, birthday FROM contacts ORDER BY {column}")
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"].strip()
            email = row["email"].strip() if row["email"] else None
            birthday = row["birthday"] if row["birthday"] else None
            group = row["group"].strip()
            phone = row["phone"].strip()
            p_type = row["type"].strip()

            cur.execute("""
                INSERT INTO contacts(name, email, birthday)
                VALUES (%s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET email = EXCLUDED.email,
                    birthday = EXCLUDED.birthday
            """, (name, email, birthday))

            cur.execute("CALL move_to_group(%s, %s)", (name, group))

            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, p_type))

    conn.commit()
    cur.close()
    conn.close()

    print("CSV import with full data completed!")

def insert_or_update(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()

    cur.close()
    conn.close()

def insert_many(names, phones):
    conn = connect()
    cur = conn.cursor()

    for i in range(len(names)):
        cur.execute(
            "CALL insert_or_update_user(%s, %s)",
            (names[i], phones[i])
        )

    conn.commit()
    cur.close()
    conn.close()

def pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()

def browse_pages():
    limit = 2
    offset = 0

    while True:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM get_paginated(%s, %s)",
            (limit, offset)
        )

        rows = cur.fetchall()

        for r in rows:
            print(r)

        cur.close()
        conn.close()

        cmd = input("(n) next | (p) prev | (q) quit: ")

        if cmd == "n":
            offset += limit
        elif cmd == "p" and offset > 0:
            offset -= limit
        elif cmd == "q":
            break

def delete(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()

def export_json(file_path="contacts.json"):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            c.id,
            c.name,
            c.email,
            c.birthday,
            g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)

    contacts = cur.fetchall()

    result = []

    for c in contacts:
        contact_id, name, email, birthday, group = c

        cur.execute("""
            SELECT phone, type
            FROM phones
            WHERE contact_id = %s
        """, (contact_id,))

        phones = cur.fetchall()

        phone_list = []
        for p in phones:
            phone_list.append({
                "phone": p[0],
                "type": p[1]
            })

        result.append({
            "name": name,
            "email": email,
            "birthday": str(birthday) if birthday else None,
            "group": group,
            "phones": phone_list
        })

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    cur.close()
    conn.close()

    print("Export completed!")

def import_json(file_path="contacts.json"):
    conn = connect()
    cur = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for contact in data:
        name = contact["name"]
        email = contact.get("email")
        birthday = contact.get("birthday")
        group = contact.get("group")
        phones = contact.get("phones", [])

        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists. (s)kip or (o)verwrite: ")

            if choice == "s":
                continue
            elif choice == "o":
                cur.execute("DELETE FROM contacts WHERE name = %s", (name,))

        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (name, email, birthday))

        contact_id = cur.fetchone()[0]

        if group:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))

        for p in phones:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (contact_id, p["phone"], p["type"]))

    conn.commit()
    cur.close()
    conn.close()

    print("Import completed!")

while True:
    print("1 - Insert/Update")
    print("2 - Insert many")
    print("3 - Insert from csv")
    print("4 - Search")
    print("5 - Search by Email")
    print("6 - Sort")
    print("7 - Navigate Pages")
    print("8 - Pagination")
    print("9 - Delete")
    print("10 - Export to JSON")
    print("11 - Import from JSON")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_or_update(input("Name: "), input("Phone: "))

    elif choice == "2":
        n = int(input("Count: "))
        names, phones = [], []

        for i in range(n):
            names.append(input("Name: "))
            phones.append(input("Phone: "))

        insert_many(names, phones)

    elif choice == "3":
        insert_from_csv("TSIS/phonebook/contacts.csv")

    elif choice == "4":
        search(input("Search: "))

    elif choice == "5":
        search_by_email()

    elif choice == "6":
        sort_contacts()

    elif choice == "7":
        browse_pages()

    elif choice == "8":
        pagination(int(input("Limit: ")), int(input("Offset: ")))

    elif choice == "9":
        delete(input("Value: "))
    
    elif choice == "10":
        export_json()

    elif choice == "11":
        import_json()

    elif choice == "0":
        break

    else:
        print("Invalid choice")