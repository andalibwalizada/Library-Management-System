import sqlite3
import tkinter as tk
from tkinter import ttk

def fetch_books(search="", status="All"):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    query = "SELECT id, title, author, genre, year, status FROM books WHERE 1=1"
    params = []

    if search:
        query += " AND (title LIKE ? OR author LIKE ? OR genre LIKE ?)"
        params += [f'%{search}%', f'%{search}%', f'%{search}%']
    if status != "All":
        query += " AND status = ?"
        params.append(status)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

def show_books():
    search_text = entry_search.get()
    current_status = status_var.get()
    books = fetch_books(search_text, current_status)
    for row in tree.get_children():
        tree.delete(row)
    for book in books:
        tree.insert('', tk.END, values=book)

root = tk.Tk()
root.title("Search & Filter Books")

tk.Label(root, text="Search (Title/Author/Genre):").grid(row=0, column=0, padx=4, pady=4, sticky="w")
entry_search = tk.Entry(root)
entry_search.grid(row=0, column=1, padx=4, pady=4, sticky="we")

tk.Label(root, text="Status:").grid(row=0, column=2, padx=4, pady=4, sticky="w")
status_var = tk.StringVar(value="All")
status_menu = tk.OptionMenu(root, status_var, "All", "available", "issued")
status_menu.grid(row=0, column=3, padx=4, pady=4, sticky="we")

tk.Button(root, text="Search/Filter", command=show_books).grid(row=0, column=4, padx=4, pady=4)

columns = ("ID", "Title", "Author", "Genre", "Year", "Status")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=110)
tree.grid(row=1, column=0, columnspan=5, padx=6, pady=6, sticky="nsew")

root.grid_columnconfigure(1, weight=1)

show_books()
root.mainloop()
