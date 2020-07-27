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
    pass
elif wish == 'C':
    c.execute("SELECT name FROM main.passwords")

    print(c.fetchall())

    which_one = input('Which one?: ')

    c.execute("SELECT password FROM main.passwords WHERE name=?", (which_one,))

    password_to_be_copied = str(c.fetchone())
    
    # Slice the string so that the parentheses don't get copied
    pyperclip.copy(password_to_be_copied[1:-2])

    close_connection()
