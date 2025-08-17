import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import date

def add_member():
    name = entry_name.get()
    contact = entry_contact.get()
    join_date = entry_join_date.get()
    if not name:
        messagebox.showerror("Error", "Please enter member name!")
        return
    if not join_date:
        join_date_value = date.today().strftime("%Y-%m-%d")
    else:
        join_date_value = join_date
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO members (name, contact, join_date) VALUES (?, ?, ?)',
                   (name, contact, join_date_value))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Member added successfully!")
    entry_name.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_join_date.delete(0, tk.END)

root = tk.Tk()
root.title("Add Member")

tk.Label(root, text="Name*").grid(row=0, column=0, pady=2)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, pady=2)

tk.Label(root, text="Contact").grid(row=1, column=0, pady=2)
entry_contact = tk.Entry(root)
entry_contact.grid(row=1, column=1, pady=2)

tk.Label(root, text="Join Date (YYYY-MM-DD)").grid(row=2, column=0, pady=2)
entry_join_date = tk.Entry(root)
entry_join_date.grid(row=2, column=1, pady=2)
entry_join_date.insert(0, date.today().strftime("%Y-%m-%d"))

tk.Button(root, text="Add Member", command=add_member).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
