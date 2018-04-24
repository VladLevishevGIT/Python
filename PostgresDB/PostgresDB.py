import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (number INTEGER, revision INTEGER, timestamp LONG)")
    conn.commit()
    conn.close()


def insert_row(item, quantity, price):
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view_all():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_row(item):
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()


def update_row(quantity, price, item):
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
insert_row("Book 2", 10, 2.5)
insert_row("Book 3", 100, 0.3)
# print(view_all())

# delete_row("Book 2")
# update_row(1000, 0.05, "Book 1")

print(view_all())