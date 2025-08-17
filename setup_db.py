import sqlite3

# Connect/Create database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year INTEGER,
    status TEXT DEFAULT 'available'
)
''')

# Members table
cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT,
    join_date TEXT
)
''')

# Transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    issue_date TEXT,
    return_date TEXT,
    fine REAL,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(member_id) REFERENCES members(id)
)
''')

conn.commit()
conn.close()
print("Database and tables created successfully!")
