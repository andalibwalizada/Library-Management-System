import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta

def fetch_members():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM members')
    members = cursor.fetchall()
    conn.close()
    return members

def fetch_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM books WHERE status = 'available'")
    books = cursor.fetchall()
    conn.close()
    return books

def issue_book():
    member = member_var.get()
    book = book_var.get()
    issue_date = entry_issue_date.get()
    return_date = entry_return_date.get()

    if not member or not book:
        messagebox.showerror("Error", "Select both member and book!")
        return

    member_id = int(member.split(":")[0])
    book_id = int(book.split(":")[0])

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (book_id, member_id, issue_date, return_date, fine) VALUES (?, ?, ?, ?, ?)',
                   (book_id, member_id, issue_date, return_date, 0.0))
    cursor.execute("UPDATE books SET status = 'issued' WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Book issued successfully!\nBook ID: {book_id}\nMember ID: {member_id}")

# GUI setup
root = tk.Tk()
root.title("Issue Book")

members = fetch_members()
books = fetch_books()

member_options = [f"{m[0]}: {m[1]}" for m in members]
book_options = [f"{b[0]}: {b[1]}" for b in books]

tk.Label(root, text="Select Member*").grid(row=0, column=0, pady=2)
member_var = tk.StringVar(value=member_options[0] if member_options else "")
member_menu = tk.OptionMenu(root, member_var, *member_options)
member_menu.grid(row=0, column=1, pady=2)

tk.Label(root, text="Select Book*").grid(row=1, column=0, pady=2)
book_var = tk.StringVar(value=book_options[0] if book_options else "")
book_menu = tk.OptionMenu(root, book_var, *book_options)
book_menu.grid(row=1, column=1, pady=2)

today = date.today()
return_by = today + timedelta(days=14)

tk.Label(root, text="Issue Date").grid(row=2, column=0, pady=2)
entry_issue_date = tk.Entry(root)
entry_issue_date.grid(row=2, column=1, pady=2)
entry_issue_date.insert(0, str(today))

tk.Label(root, text="Return Date").grid(row=3, column=0, pady=2)
entry_return_date = tk.Entry(root)
entry_return_date.grid(row=3, column=1, pady=2)
entry_return_date.insert(0, str(return_by))

tk.Button(root, text="Issue Book", command=issue_book).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

