from connect import connect


def search(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def insert_or_update(name, number):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s)", (name, number))
    conn.commit()

    cur.close()
    conn.close()


def insert_many(names, number):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_many_users(%s, %s, %s)",
        (names, number, None)
    )

    conn.commit()

    cur.close()
    conn.close()


def pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()


while True:
    print("1 - Insert or Update")
    print("2 - Insert many users")
    print("3 - Search")
    print("4 - Pagination")
    print("5 - Delete")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone: ")
        insert_or_update(name, number)

    elif choice == "2":
        n = int(input("How many users? "))
        names = []
        numbers = []

        for i in range(n):
            name = input(f"Name {i+1}: ")
            number = input(f"Phone {i+1}: ")
            names.append(name)
            numbers.append(number)

        insert_many(names, numbers)

    elif choice == "3":
        pattern = input("Enter pattern: ")
        search(pattern)

    elif choice == "4":
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        pagination(limit, offset)

    elif choice == "5":
        value = input("Enter name or phone: ")
        delete(value)

    elif choice == "0":
        break

    else:
        print("Enter a valid number!")