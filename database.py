import sqlite3
from tkinter.constants import COMMAND

conn = sqlite3.connect('Product-database.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS history(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            tid TEXT,
            stamp TEXT,
            product TEXT,
            price REAL,
            quan REAL,
            total REAL )""")

print('succes')

def insert_history(data):
    ID = None
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quan = data['quan']
    total = data['total']
    with conn:
        command = 'INSERT INTO history VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(ID,tid,stamp,product,price,quan,total))
        conn.commit()

    print('insert !!')

transection = {'tid':'123123',
                'stamp':'2021-12-14 11:35:32',
                'product':'ทุเรียน',
                'price':2112,
                'quan':12,
                'total':12121}

#insert_history(transection)

def View_history():
    with conn:
        c.execute("SELECT * FROM history")
        data = c.fetchall()
        print(data)

View_history()