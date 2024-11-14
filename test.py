import sqlite3
import tkinter as tk
from tkinter import messagebox
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')
conn.commit()
conn.close()
def signup():
    username = entry_username.get()
    password = entry_password.get()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()  
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    finally:
        conn.close()
def login():
    username = entry_username.get()
    password = entry_password.get()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Login", "Login successful!")
        cursor.execute("SELECT username FROM users")
        users = cursor.fetchall()
        users_list = "\n".join([user[0] for user in users])
        messagebox.showinfo("All Users", f"All users in the database:\n{users_list}")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
    conn.close()
def get_lyrics():
    title_to_search = entry_song_title.get()
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT lyrics FROM songs WHERE title = ?", (title_to_search,))
    result = cursor.fetchone()
    if result:
        lyrics = result[0]
        lyrics_window = tk.Toplevel(root)
        lyrics_window.title(f"Lyrics for '{title_to_search}'")
        text = tk.Text(lyrics_window, wrap="word")
        text.insert("1.0", lyrics)
        text.pack(expand=True, fill="both")
    else:
        messagebox.showinfo("Not Found", f"No song found with the title '{title_to_search}'")
    conn.close()
root = tk.Tk()
root.title("User and Lyrics Database")
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_password = tk.Entry(root, show="*", width=30)
entry_password.grid(row=1, column=1, padx=10, pady=10)
btn_signup = tk.Button(root, text="Sign Up", width=15, command=signup)
btn_signup.grid(row=2, column=0, padx=10, pady=10)
btn_login = tk.Button(root, text="Log In", width=15, command=login)
btn_login.grid(row=2, column=1, padx=10, pady=10)
tk.Label(root, text="Enter Song Title:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_song_title = tk.Entry(root, width=30)
entry_song_title.grid(row=3, column=1, padx=10, pady=10)
btn_get_lyrics = tk.Button(root, text="Get Lyrics", width=20, command=get_lyrics)
btn_get_lyrics.grid(row=4, columnspan=2, padx=10, pady=10)
def setup_song_database():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        title TEXT NOT NULL,
        lyrics TEXT
    )
    ''')
    songs = [
        ("Shape of tune", "C:\\PYTHON PROJECT\\song1.txt"),
        ("Believer", "C:\\PYTHON PROJECT\\song2.txt"),
        ("Someone you loved", "C:\\PYTHON PROJECT\\song3.txt"),
        ("None of my business", "C:\\PYTHON PROJECT\\song4.txt"),
        ("Let her go", "C:\\PYTHON PROJECT\\song5.txt")
    ]
    for title, filepath in songs:
        with open(filepath, "r", encoding="utf-8") as file:
            lyrics = file.read()
            cursor.execute('''
                INSERT INTO songs (title, lyrics)
                VALUES (?, ?)
            ''', (title, lyrics))
    connection.commit()
    connection.close()
setup_song_database()
root.mainloop()
