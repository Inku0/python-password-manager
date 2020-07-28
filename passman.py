import random
import sqlite3
import pyperclip

conn = sqlite3.connect('passwords.db')

c = conn.cursor()


def close_connection():
    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()


wish = input('What do you wish to do? (N)ew password, (E)dit a password or (C)opy a password: ')

if wish == 'N':

    letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    length = input('Length: ')

    try:
        val = int(length)
    except ValueError:
        print('Only integers are accepted!')
        raise SystemExit

    given_name = input('Name: ')

    generated_password = list(letters)[random.randint(0, 93)]

    for i in range(int(length)):
        generated_password += list(letters)[random.randint(0, 93)]

    print(generated_password)

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (name text, password text)''')

    # Insert a row of data
    c.execute("INSERT INTO passwords (name, password) VALUES(?, ?)",
              (given_name, generated_password))

    close_connection()

elif wish == 'E':
    c.execute("SELECT name FROM passwords")

    print(c.fetchall())

    which_one = input('Which one?: ')

    changed_password = input('What would you like to change it to?: ')

    c.execute("UPDATE passwords SET password = (?) WHERE name = ?", (changed_password, which_one))

    close_connection()
elif wish == 'C':
    c.execute("SELECT name FROM passwords")

    print(c.fetchall())

    which_one = input('Which one?: ')

    c.execute("SELECT password FROM passwords WHERE name=?", (which_one,))

    password_to_be_copied = str(c.fetchone())

    pyperclip.copy(password_to_be_copied[1:-2])

    close_connection()
