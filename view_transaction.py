import sqlite3
import tkinter as tk
from tkinter import ttk

def fetch_transactions():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT transactions.id, books.title, members.name,
               transactions.issue_date, transactions.return_date, transactions.fine
        FROM transactions
        JOIN books ON transactions.book_id = books.id
        JOIN members ON transactions.member_id = members.id
        ORDER BY transactions.id DESC
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

root = tk.Tk()
root.title("View Transactions")

columns = ("ID", "Book Title", "Member Name", "Issue Date", "Return Date", "Fine")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def show_transactions():
    transactions = fetch_transactions()
    for row in tree.get_children():
        tree.delete(row)
    for tx in transactions:
        tree.insert('', tk.END, values=tx)

tk.Button(root, text="Refresh", command=show_transactions).pack(pady=10)

show_transactions()
root.mainloop()
