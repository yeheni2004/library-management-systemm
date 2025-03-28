import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
from datetime import date

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # replace with your MySQL password
    database="library_management"
)

cursor = db.cursor()

# Member Management
def member_management():
    member_window = tk.Toplevel()
    member_window.title("Member Management")
    member_window.attributes('-fullscreen', True)
    
    # Set background image
    bg_img = Image.open("library_logo.jpg")
    bg_img = bg_img.resize((member_window.winfo_screenwidth(), member_window.winfo_screenheight()), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(member_window, image=bg_photo)
    bg_label.photo = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def add_member():
        name = entry_name.get()
        address = entry_address.get()
        phone = entry_phone.get()

        cursor.execute("INSERT INTO Members (name, address, phone) VALUES (%s, %s, %s)", (name, address, phone))
        db.commit()
        messagebox.showinfo("Member Management", "Member added successfully")
        entry_name.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

    def update_member():
        member_id = entry_member_id.get()
        name = entry_name.get()
        address = entry_address.get()
        phone = entry_phone.get()

        cursor.execute("UPDATE Members SET name=%s, address=%s, phone=%s WHERE member_id=%s", (name, address, phone, member_id))
        db.commit()
        messagebox.showinfo("Member Management", "Member updated successfully")
        entry_member_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

    def delete_member():
        member_id = entry_member_id.get()
        
        cursor.execute("DELETE FROM Members WHERE member_id=%s", (member_id,))
        db.commit()
        messagebox.showinfo("Member Management", "Member deleted successfully")
        entry_member_id.delete(0, tk.END)

    def view_members():
        cursor.execute("SELECT * FROM Members")
        members = cursor.fetchall()

        member_list.delete(0, tk.END)
        for member in members:
            member_list.insert(tk.END, f"ID: {member[0]}, Name: {member[1]}, Address: {member[2]}, Phone: {member[3]}")

    lbl_member_id = tk.Label(member_window, text="Member ID", bg='lightyellow')
    lbl_member_id.pack(pady=5)
    entry_member_id = tk.Entry(member_window)
    entry_member_id.pack(pady=5)

    lbl_name = tk.Label(member_window, text="Name", bg='lightyellow')
    lbl_name.pack(pady=5)
    entry_name = tk.Entry(member_window)
    entry_name.pack(pady=5)

    lbl_address = tk.Label(member_window, text="Address", bg='lightyellow')
    lbl_address.pack(pady=5)
    entry_address = tk.Entry(member_window)
    entry_address.pack(pady=5)

    lbl_phone = tk.Label(member_window, text="Phone", bg='lightyellow')
    lbl_phone.pack(pady=5)
    entry_phone = tk.Entry(member_window)
    entry_phone.pack(pady=5)

    btn_add_member = tk.Button(member_window, text="Add Member", command=add_member, bg='lightblue')
    btn_add_member.pack(pady=5)

    btn_update_member = tk.Button(member_window, text="Update Member", command=update_member, bg='lightblue')
    btn_update_member.pack(pady=5)

    btn_delete_member = tk.Button(member_window, text="Delete Member", command=delete_member, bg='lightblue')
    btn_delete_member.pack(pady=5)

    btn_view_members = tk.Button(member_window, text="View Members", command=view_members, bg='lightblue')
    btn_view_members.pack(pady=5)

    # Exit Button
    btn_exit = tk.Button(member_window, text="Exit", command=member_window.destroy, bg='red')
    btn_exit.pack(pady=10, side=tk.BOTTOM)

    member_list = tk.Listbox(member_window, height=20, width=80, font=("Arial", 12))
    member_list.pack(pady=10)

# Book Management
def book_management():
    book_window = tk.Toplevel()
    book_window.title("Book Management")
    book_window.attributes('-fullscreen', True)

    # Set background image
    bg_img = Image.open("library_logo2.jpg")
    bg_img = bg_img.resize((book_window.winfo_screenwidth(), book_window.winfo_screenheight()), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(book_window, image=bg_photo)
    bg_label.photo = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def add_book():
        title = entry_title.get()
        author = entry_author.get()
        genre = entry_genre.get()

        cursor.execute("INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)", (title, author, genre))
        db.commit()
        messagebox.showinfo("Book Management", "Book added successfully")
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_genre.delete(0, tk.END)

    def update_book():
        book_id = entry_book_id.get()
        title = entry_title.get()
        author = entry_author.get()
        genre = entry_genre.get()

        cursor.execute("UPDATE Books SET title=%s, author=%s, genre=%s WHERE book_id=%s", (title, author, genre, book_id))
        db.commit()
        messagebox.showinfo("Book Management", "Book updated successfully")
        entry_book_id.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_genre.delete(0, tk.END)

    def delete_book():
        book_id = entry_book_id.get()
        
        cursor.execute("DELETE FROM Books WHERE book_id=%s", (book_id,))
        db.commit()
        messagebox.showinfo("Book Management", "Book deleted successfully")
        entry_book_id.delete(0, tk.END)

    def view_books():
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()

        book_list.delete(0, tk.END)
        for book in books:
            book_list.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")

    lbl_book_id = tk.Label(book_window, text="Book ID", bg='lightyellow')
    lbl_book_id.pack(pady=5)
    entry_book_id = tk.Entry(book_window)
    entry_book_id.pack(pady=5)

    lbl_title = tk.Label(book_window, text="Title", bg='lightyellow')
    lbl_title.pack(pady=5)
    entry_title = tk.Entry(book_window)
    entry_title.pack(pady=5)

    lbl_author = tk.Label(book_window, text="Author", bg='lightyellow')
    lbl_author.pack(pady=5)
    entry_author = tk.Entry(book_window)
    entry_author.pack(pady=5)

    lbl_genre = tk.Label(book_window, text="Genre", bg='lightyellow')
    lbl_genre.pack(pady=5)
    entry_genre = tk.Entry(book_window)
    entry_genre.pack(pady=5)

    btn_add_book = tk.Button(book_window, text="Add Book", command=add_book, bg='lightblue')
    btn_add_book.pack(pady=5)

    btn_update_book = tk.Button(book_window, text="Update Book", command=update_book, bg='lightblue')
    btn_update_book.pack(pady=5)

    btn_delete_book = tk.Button(book_window, text="Delete Book", command=delete_book, bg='lightblue')
    btn_delete_book.pack(pady=5)

    btn_view_books = tk.Button(book_window, text="View Books", command=view_books, bg='lightblue')
    btn_view_books.pack(pady=5)

    # Exit Button
    btn_exit = tk.Button(book_window, text="Exit", command=book_window.destroy, bg='red')
    btn_exit.pack(pady=10, side=tk.BOTTOM)

    book_list = tk.Listbox(book_window, height=20, width=80, font=("Arial", 12))
    book_list.pack(pady=10)

# Borrowing Management
def borrowing_management():
    borrowing_window = tk.Toplevel()
    borrowing_window.title("Borrowing Management")
    borrowing_window.attributes('-fullscreen', True)

    # Set background image
    bg_img = Image.open("library_logo3.jpg")
    bg_img = bg_img.resize((borrowing_window.winfo_screenwidth(), borrowing_window.winfo_screenheight()), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(borrowing_window, image=bg_photo)
    bg_label.photo = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def add_borrowing():
        member_id = entry_member_id.get()
        book_id = entry_book_id.get()
        borrowed_date = entry_borrowed_date.get()
        return_date = entry_return_date.get()

        cursor.execute("INSERT INTO Borrowings (member_id, book_id, borrowed_date, return_date) VALUES (%s, %s, %s, %s)",
                       (member_id, book_id, borrowed_date, return_date))
        db.commit()
        messagebox.showinfo("Borrowing Management", "Borrowing record added successfully")
        entry_member_id.delete(0, tk.END)
        entry_book_id.delete(0, tk.END)
        entry_borrowed_date.delete(0, tk.END)
        entry_return_date.delete(0, tk.END)

    def update_borrowing():
        borrowing_id = entry_borrowing_id.get()
        member_id = entry_member_id.get()
        book_id = entry_book_id.get()
        borrowed_date = entry_borrowed_date.get()
        return_date = entry_return_date.get()

        cursor.execute("UPDATE Borrowings SET member_id=%s, book_id=%s, borrowed_date=%s, return_date=%s WHERE borrowing_id=%s",
                       (member_id, book_id, borrowed_date, return_date, borrowing_id))
        db.commit()
        messagebox.showinfo("Borrowing Management", "Borrowing record updated successfully")
        entry_borrowing_id.delete(0, tk.END)
        entry_member_id.delete(0, tk.END)
        entry_book_id.delete(0, tk.END)
        entry_borrowed_date.delete(0, tk.END)
        entry_return_date.delete(0, tk.END)

    def delete_borrowing():
        borrowing_id = entry_borrowing_id.get()
        
        cursor.execute("DELETE FROM Borrowings WHERE borrowing_id=%s", (borrowing_id,))
        db.commit()
        messagebox.showinfo("Borrowing Management", "Borrowing record deleted successfully")
        entry_borrowing_id.delete(0, tk.END)

    def view_borrowings():
        cursor.execute("SELECT * FROM Borrowings")
        borrowings = cursor.fetchall()

        borrowing_list.delete(0, tk.END)
        for borrowing in borrowings:
            borrowing_list.insert(tk.END, f"ID: {borrowing[0]}, Member ID: {borrowing[1]}, Book ID: {borrowing[2]}, Borrowed: {borrowing[3]}, Return: {borrowing[4]}")

    lbl_borrowing_id = tk.Label(borrowing_window, text="Borrowing ID", bg='lightyellow')
    lbl_borrowing_id.pack(pady=5)
    entry_borrowing_id = tk.Entry(borrowing_window)
    entry_borrowing_id.pack(pady=5)

    lbl_member_id = tk.Label(borrowing_window, text="Member ID", bg='lightyellow')
    lbl_member_id.pack(pady=5)
    entry_member_id = tk.Entry(borrowing_window)
    entry_member_id.pack(pady=5)

    lbl_book_id = tk.Label(borrowing_window, text="Book ID", bg='lightyellow')
    lbl_book_id.pack(pady=5)
    entry_book_id = tk.Entry(borrowing_window)
    entry_book_id.pack(pady=5)

    lbl_borrowed_date = tk.Label(borrowing_window, text="Borrowed Date (YYYY-MM-DD)", bg='lightyellow')
    lbl_borrowed_date.pack(pady=5)
    entry_borrowed_date = tk.Entry(borrowing_window)
    entry_borrowed_date.pack(pady=5)

    lbl_return_date = tk.Label(borrowing_window, text="Return Date (YYYY-MM-DD)", bg='lightyellow')
    lbl_return_date.pack(pady=5)
    entry_return_date = tk.Entry(borrowing_window)
    entry_return_date.pack(pady=5)

    btn_add_borrowing = tk.Button(borrowing_window, text="Add Borrowing", command=add_borrowing, bg='lightblue')
    btn_add_borrowing.pack(pady=5)

    btn_update_borrowing = tk.Button(borrowing_window, text="Update Borrowing", command=update_borrowing, bg='lightblue')
    btn_update_borrowing.pack(pady=5)

    btn_delete_borrowing = tk.Button(borrowing_window, text="Delete Borrowing", command=delete_borrowing, bg='lightblue')
    btn_delete_borrowing.pack(pady=5)

    btn_view_borrowings = tk.Button(borrowing_window, text="View Borrowings", command=view_borrowings, bg='lightblue')
    btn_view_borrowings.pack(pady=5)

    # Exit Button
    btn_exit = tk.Button(borrowing_window, text="Exit", command=borrowing_window.destroy, bg='red')
    btn_exit.pack(pady=10, side=tk.BOTTOM)

    borrowing_list = tk.Listbox(borrowing_window, height=20, width=80, font=("Arial", 12))
    borrowing_list.pack(pady=10)

# User Management
def user_management():
    user_window = tk.Toplevel()
    user_window.title("User Management")
    user_window.attributes('-fullscreen', True)

    # Set background image
    bg_img = Image.open("library_logo4.jpg")
    bg_img = bg_img.resize((user_window.winfo_screenwidth(), user_window.winfo_screenheight()), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(user_window, image=bg_photo)
    bg_label.photo = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def add_user():
        username = entry_username.get()
        password = entry_password.get()

        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        messagebox.showinfo("User Management", "User added successfully")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    def update_user():
        user_id = entry_user_id.get()
        username = entry_username.get()
        password = entry_password.get()

        cursor.execute("UPDATE Users SET username=%s, password=%s WHERE user_id=%s", (username, password, user_id))
        db.commit()
        messagebox.showinfo("User Management", "User updated successfully")
        entry_user_id.delete(0, tk.END)
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    def delete_user():
        user_id = entry_user_id.get()
        
        cursor.execute("DELETE FROM Users WHERE user_id=%s", (user_id,))
        db.commit()
        messagebox.showinfo("User Management", "User deleted successfully")
        entry_user_id.delete(0, tk.END)

    def view_users():
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()

        user_list.delete(0, tk.END)
        for user in users:
            user_list.insert(tk.END, f"ID: {user[0]}, Username: {user[1]}")

    lbl_user_id = tk.Label(user_window, text="User ID", bg='lightyellow')
    lbl_user_id.pack(pady=5)
    entry_user_id = tk.Entry(user_window)
    entry_user_id.pack(pady=5)

    lbl_username = tk.Label(user_window, text="Username", bg='lightyellow')
    lbl_username.pack(pady=5)
    entry_username = tk.Entry(user_window)
    entry_username.pack(pady=5)

    lbl_password = tk.Label(user_window, text="Password", bg='lightyellow')
    lbl_password.pack(pady=5)
    entry_password = tk.Entry(user_window)
    entry_password.pack(pady=5)

    btn_add_user = tk.Button(user_window, text="Add User", command=add_user, bg='lightblue')
    btn_add_user.pack(pady=5)

    btn_update_user = tk.Button(user_window, text="Update User", command=update_user, bg='lightblue')
    btn_update_user.pack(pady=5)

    btn_delete_user = tk.Button(user_window, text="Delete User", command=delete_user, bg='lightblue')
    btn_delete_user.pack(pady=5)

    btn_view_users = tk.Button(user_window, text="View Users", command=view_users, bg='lightblue')
    btn_view_users.pack(pady=5)

    # Exit Button
    btn_exit = tk.Button(user_window, text="Exit", command=user_window.destroy, bg='red')
    btn_exit.pack(pady=10, side=tk.BOTTOM)

    user_list = tk.Listbox(user_window, height=20, width=80, font=("Arial", 12))
    user_list.pack(pady=10)

# Main Application
window = tk.Tk()
window.title("Library Management System")
window.attributes('-fullscreen', True)

# Background image for main window
bg_img_main = Image.open("library_logo1.jpg")
bg_img_main = bg_img_main.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_photo_main = ImageTk.PhotoImage(bg_img_main)
bg_label_main = tk.Label(window, image=bg_photo_main)
bg_label_main.photo = bg_photo_main
bg_label_main.place(x=0, y=0, relwidth=1, relheight=1)

btn_member_management = tk.Button(window, text="Member Management", command=member_management, bg='lightblue', height=3, width=25)
btn_member_management.pack(pady=10)

btn_book_management = tk.Button(window, text="Book Management", command=book_management, bg='lightblue', height=3, width=25)
btn_book_management.pack(pady=10)

btn_borrowing_management = tk.Button(window, text="Borrowing Management", command=borrowing_management, bg='lightblue', height=3, width=25)
btn_borrowing_management.pack(pady=10)

btn_user_management = tk.Button(window, text="User Management", command=user_management, bg='lightblue', height=3, width=25)
btn_user_management.pack(pady=10)

# Exit Button
btn_exit = tk.Button(window, text="Exit", command=window.destroy, bg='red', height=3, width=25)
btn_exit.pack(pady=10, side=tk.BOTTOM)

window.mainloop()
