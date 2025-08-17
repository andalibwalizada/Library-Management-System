import sqlite3
import tkinter as tk
from tkinter import ttk

def fetch_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, author, genre, year, status FROM books')
    rows = cursor.fetchall()
    conn.close()
    return rows

def show_books():
    books = fetch_books()
    for row in tree.get_children():
        tree.delete(row)
    for book in books:
        tree.insert('', tk.END, values=book)

root = tk.Tk()
root.title("View Books")

columns = ("ID", "Title", "Author", "Genre", "Year", "Status")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill=tk.BOTH, expand=True)
tk.Button(root, text="Refresh", command=show_books).pack(pady=10)

show_books()
root.mainloop()