import time
import threading
import socket
import sqlite3

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


# def deposit(conn, account, amt):

def query(account):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM accounts WHERE account=?", (account,))
        print(c.fetchone())


def withdraw(account, amt):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('SELECT balance FROM accounts WHERE account=?', (account,))
        balance = c.fetchone()[0]

        if amt <= balance:
            balance -= amt
            c.execute('UPDATE accounts SET balance=? WHERE account=?', (balance, account))
            print("New balance", balance)
        else:
            print("WARNING! Tried to overdraw account", account)


# def safe_withdraw(account, amt):
#     with sqlite3.connect(DB) as conn:
#         c = conn.cursor()
#         c.execute(
#         "UPDATE accounts SET balance=((SELECT balance from accounts where account=?)-?) WHERE (account=? AND ((SELECT balance from accounts where account=?)-? >= 0))"
#         ,(account,amt,account,account,amt))
#         query(12345)

if __name__ == "__main__":
    init(reset=True)
    # query(12345)
    # # withdraw(12345, 1)
    # safe_withdraw(12345, 1)
    # threading.Thread(target=periodically_print_query()).start()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 22333))
    server_socket.listen(128)
    print("Listening for requests...")
    while True:
        (client, address) = server_socket.accept()
        threading.Thread(target = withdraw, args= (12345, 100)).start()





