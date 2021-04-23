import sqlite3
from sqlite3.dbapi2 import Cursor
conn = sqlite3.connect('kontakty.db')
conn.executescript("""DROP TABLE IF EXISTS pracownicy;
            CREATE TABLE IF NOT EXISTS pracownicy(
            NAME TEXT NOT NULL,
            SURNAME TEXT NOT NULL,
            TOWN TEXT NOT NULL,
            EARNINGS TEXT NOT NULL);""")
conn.execute("INSERT INTO pracownicy (NAME,SURNAME,TOWN,EARNINGS) VALUES ('JANEK', 'DZBANEK', 'WROCLAW','2300')")
conn.execute("INSERT INTO pracownicy (NAME,SURNAME,TOWN,EARNINGS) VALUES ('MICHAL', 'NIEKICHAL',  'GRABISZYNEK','2137')")
conn.execute("INSERT INTO pracownicy (NAME,SURNAME,TOWN,EARNINGS) VALUES ('MARCIN', 'PROCHOWICZ',  'SZCZECIN','32000')")
cursor = conn.execute("SELECT * FROM PRACOWNICY")
def add():
    name = input("Podaj imię")
    surname = input("Podaj nazwisko")
    town = input("Podaj miasto")
    earnings = input("Podaj zarobki")
    conn.execute("INSERT INTO pracownicy (NAME,SURNAME,TOWN,EARNINGS) VALUES ('{}''{}''{}''{}')".format(name,surname,town,earnings))
def all():
    row = cursor.fetchall()
    for row in row:
        print(row)
def sortedbyname():
    cur = conn.execute(f'SELECT * FROM pracownicy ORDER BY NAME ASC')
    for row in cur:
        print(row)
def leastearnings():
    cur = conn.execute(f'SELECT MIN(EARNINGS) FROM pracownicy')
    for row in cur:
        print(row)
def mostearnings():
    cur = conn.execute(f'SELECT MAX(EARNINGS) FROM pracownicy')
    for row in cur:
        print(row)
def deletowanie(imie):
    conn.execute("DELETE FROM pracownicy WHERE NAME = '%i'"%(imie))
    conn.commit()
    row = cursor.fetchall()
    for row in row:
        print(row)

deletowanie(input())