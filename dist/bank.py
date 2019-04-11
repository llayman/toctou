import socket
import sqlite3
import threading

DB = './bank_db.sqlite'

def init(reset=False):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        try:
            c.execute('''SELECT COUNT(*) FROM accounts''')
            if reset:
                c.execute('''DROP TABLE accounts''')
                c.execute('''CREATE TABLE accounts (account INTEGER, balance REAL)''')
                c.execute('''INSERT INTO accounts VALUES (12345, 10000.00)''')
        except sqlite3.OperationalError:
            c.execute('''CREATE TABLE accounts (account INTEGER, balance REAL)''')
            c.execute('''INSERT INTO accounts VALUES (12345, 10000.00)''')


def query(account):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT balance FROM accounts WHERE account=?", (account,))
        result = c.fetchone()
        if result:
            print('Account: {}, Current balance: {}'.format(account, result[0]))
        else:
            print("Account number", account, "does not exist.")


if __name__ == "__main__":
    init(reset=True)
    query(12345)
    query(5555)






