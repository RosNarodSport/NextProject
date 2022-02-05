import sqlite3

base = sqlite3.connect('db/users.db')
cur = base.cursor()