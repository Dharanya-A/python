
import sqlite3

# Create a new database and table for users
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


# Function to register a new user (Sign Up)
def signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Connect to the database and insert the new user
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        conn.close()

# Function to log in an existing user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match the stored records
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login successful!")        
        # Query to get all users in the database
        cursor.execute("SELECT username FROM users")
        users = cursor.fetchall()
        print("All users in the database:")
        for user in users:
            print(user[0])
        
    else:
        print("Invalid username or password.")
    
    conn.close()

# Main menu to choose sign-up or login
def main():
    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid option! Please choose again.")

# Run the program
if __name__ == '__main__':
    main()

# Connect to the SQLite database
connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    title TEXT NOT NULL,
    lyrics TEXT
)
''')
print("database created succesfully")
# Define songs with their titles and file paths for lyrics
songs = [
    ("Shape of tune", "C:\\PYTHON PROJECT\\song1.txt"),
    ("Believer", "C:\\PYTHON PROJECT\\song2.txt"),
     ("Someone you loved", "C:\\PYTHON PROJECT\\song3.txt"),
     ("None of my business", "C:\\PYTHON PROJECT\\song4.txt"),
     ("Let her go", "C:\\PYTHON PROJECT\\song5.txt")
]

# Insert each song's data into the database
for title, filepath in songs:
    with open(filepath, "r", encoding="utf-8") as file:
        lyrics = file.read()
        cursor.execute('''
            INSERT INTO songs (title, lyrics)
            VALUES (?, ?)
        ''', (title, lyrics))

# Commit the transaction
connection.commit()
print("Large data inserted successfully from files!")
# Define the song title you want to retrieve
title_to_search = input("Enter the title of the song: ")  # Change this title as needed
# Execute a query to fetch lyrics based on the song title
cursor.execute('''
    SELECT lyrics FROM songs
    WHERE title = ?
''', (title_to_search,))
# Fetch the result
result = cursor.fetchone()
# Check if any data was returned
if result:
    lyrics = result[0]
    print(f"Lyrics for '{title_to_search}':\n{lyrics}")
else:
    print(f"No song found with the title '{title_to_search}'")

# Close the connection
connection.close()
