import sqlite3

connection = sqlite3.connect('data1.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_table1 = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
create_table2 = "CREATE TABLE IF NOT EXISTS stores (id INTEGER FOREING KEY, name text, items real)"
cursor.execute(create_table)
cursor.execute(create_table1)

# cursor.execute("INSERT INTO items VALUES('test', 12.33)")

connection.commit()

connection.close()
