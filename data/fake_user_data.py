from faker import Faker
import sqlite3

con = sqlite3.connect("users.db")

cursor = con.cursor()

cursor.execute("""
    CREATE table IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(255) NOT NULL,
        USERNAME VARCHAR(255) NOT NULL UNIQUE,
        PASSWORD VARCHAR(255) NOT NULL    
    )
""")

fake = Faker()

for i in range(5):
    name = fake.name()
    usernamer = fake.user_name()
    password =fake.password()

    cursor.execute("""
        INSERT INTO USERS (NAME, USERNAME, PASSWORD)
        VALUES 
            (?, ?, ?)
    """, (name, usernamer, password))
    
con.commit()
con.close()