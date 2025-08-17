import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime

def fetch_issued_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, b.title, m.name, t.issue_date, t.return_date
        FROM transactions t
        JOIN books b ON t.book_id = b.id
        JOIN members m ON t.member_id = m.id
        WHERE b.status='issued'
    """)
    issued = cursor.fetchall()
    conn.close()
    return issued

def return_book():
    selection = book_var.get()
    if not selection:
        messagebox.showerror("Error", "Please select a book to return!")
        return
    if selection == "No issued books":
        return

    trans_id = int(selection.split(":")[0])
    actual_return = entry_actual_return.get()
    if not actual_return:
        actual_return = date.today().strftime("%Y-%m-%d")

    # Calculate fine
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT return_date FROM transactions WHERE id=?', (trans_id,))
    expected = cursor.fetchone()[0]
    expected_dt = datetime.strptime(expected, "%Y-%m-%d")
    actual_dt = datetime.strptime(actual_return, "%Y-%m-%d")
    fine = 0.0
    if actual_dt > expected_dt:
        days_late = (actual_dt - expected_dt).days
        fine = days_late * 1.00

    # Update transaction and book status
    cursor.execute('UPDATE transactions SET actual_return=?, fine=? WHERE id=?',
                   (actual_return, fine, trans_id))
    cursor.execute("""
        UPDATE books
        SET status='available'
        WHERE id=(SELECT book_id FROM transactions WHERE id=?)
    """, (trans_id,))
    conn.commit()
    conn.close()

    if fine > 0:
        messagebox.showinfo("Return Book", f"Book returned! Fine: ${fine:.2f}")
    else:
        messagebox.showinfo("Return Book", "Book returned successfully!")

    root.destroy()

# GUI
root = tk.Tk()
root.title("Return Book")

issued = fetch_issued_books()
if not issued:
    messagebox.showinfo("Info", "No issued books to return.")
    root.destroy()
else:
    options = [
        f"{row[0]}: {row[1]} | Member: {row[2]} | Due: {row[4]}"
        for row in issued
    ]
    book_var = tk.StringVar(value=options[0])

    tk.Label(root, text="Select Issued Book*").grid(row=0, column=0, pady=5, padx=5)
    book_menu = tk.OptionMenu(root, book_var, *options)
    book_menu.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(root, text="Actual Return Date (YYYY-MM-DD)").grid(row=1, column=0, pady=5, padx=5)
    entry_actual_return = tk.Entry(root)
    entry_actual_return.grid(row=1, column=1, pady=5, padx=5)
    entry_actual_return.insert(0, date.today().strftime("%Y-%m-%d"))

    tk.Button(root, text="Return Book", command=return_book).grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()
