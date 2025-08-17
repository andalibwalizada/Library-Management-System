import tkinter as tk
import subprocess

root = tk.Tk()
root.title('Library Management System')
root.geometry('300x380')

def run_script(filename):
    subprocess.Popen(['python', filename])

# Add buttons for your features
tk.Button(root, text="Add Book", command=lambda: run_script('add_book.py'), width=24, height=2).pack(pady=6)
tk.Button(root, text="View Books", command=lambda: run_script('view_books.py'), width=24, height=2).pack(pady=6)
tk.Button(root, text="Search/Filter Books", command=lambda: run_script('search_books.py'), width=24, height=2).pack(pady=6)
tk.Button(root, text="Add Member", command=lambda: run_script('add_member.py'), width=24, height=2).pack(pady=6)
tk.Button(root, text="View Transactions", command=lambda: run_script('view_transactions.py'), width=24, height=2).pack(pady=6)
tk.Button(root, text="Issue Book", command=lambda: run_script('issue_book.py'), width=24, height=2).pack(pady=6)
tk.Button(root, text="Return Book", command=lambda: run_script('return_book.py'), width=24, height=2).pack(pady=6)

tk.Label(root, text="Welcome to Your Library System!", fg="blue", font=("Arial", 11)).pack(pady=18)
root.mainloop()
