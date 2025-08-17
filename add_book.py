import sqlite3
import tkinter as tk
from tkinter import messagebox

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    year = entry_year.get()
    if not title or not author or not year:
        messagebox.showerror("Error", "Please fill in Title, Author, and Year!")
        return
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)',
                   (title, author, genre, year))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Book added successfully!")
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_year.delete(0, tk.END)

root = tk.Tk()
root.title("Add Book")

tk.Label(root, text="Title*").grid(row=0, column=0, pady=2)
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1, pady=2)

tk.Label(root, text="Author*").grid(row=1, column=0, pady=2)
entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1, pady=2)

tk.Label(root, text="Genre").grid(row=2, column=0, pady=2)
entry_genre = tk.Entry(root)
entry_genre.grid(row=2, column=1, pady=2)

tk.Label(root, text="Year*").grid(row=3, column=0, pady=2)
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1, pady=2)

tk.Button(root, text="Add Book", command=add_book).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
