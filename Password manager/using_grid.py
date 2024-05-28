import string
import random
import tkinter.messagebox as messagebox
from tkinter import *
import tkinter as tk
import sqlite3

#-----------------------------Create Database ------------------------------- #
#Creat a new sqlite3 database
conn = sqlite3.connect("password_manager.db")
#Create the cursor to intereact with the database
cursor = conn.cursor()
# Create the tables in the database
cursor.execute("CREATE TABLE IF NOT EXISTS passwords (website TEXT, username TEXT, password TEXT)")



#---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Define the alphabets and symbols to be used in the password
    alfabeth = lowercase_alphabets = list(string.ascii_lowercase)
    # Define the numbers and symbols to be used in the password
    numbers = random.sample(range(1, 10), 9)
    # Define the symbols to be used in the password
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    # Define the password length and randomly generate the password letters
    password_letters = random.sample(alfabeth, 7)
    # Define the numbers to be used in the password and radomly pick them
    password_numbers = random.sample(numbers, 2)
    # Define the symbols to be used in the password and radomliy pick them
    password_symbols = random.sample(symbols, 2)
    
    # Convert the numbers list to a list of strings so we can concatenate them
    password_numbers = [str(num) for num in password_numbers]
    # Concatenate the letters, numbers, and symbols into a single list
    password = password_numbers + password_letters + password_symbols
    # Randomly shuffle the list of letters, numbers, and symbols
    random.shuffle(password)
    # Convert the list of letters, numbers, and symbols to a string
    generated_password = "".join(password)
    # Insert the generated password into the entry field
    entry_password.delete(0, tk.END)  # Clear any existing text
    entry_password.insert(0, generated_password)  # Insert the generated password

#---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = entry_password.get()
    epost_username = epost_entry.get()
    # Insert the password into the database
    cursor.execute("INSERT INTO passwords VALUES (?,?,?)", (website, epost_username, password))
    # Commit the changes to the database
    conn.commit()
    conn.close()
    
 # Display a popup message
    messagebox.showinfo("Password Saved", "Your password has been stored.")
    
    # Ask the user if they want to add a new password
    response = messagebox.askyesno("Add New Password", "Do you want to add a new password?")
    
    if response:
        # Clear the input fields
        website_entry.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        epost_entry.delete(0, tk.END)
    else:
        # Close the window
        window.quit()


#create the window
window = tk.Tk()
window.title("Password Generator")

# Create a canvas to hold the logo image
canvas = Canvas(width=300, height=300)
logo_img = PhotoImage(file="Coding/Projects/Password manager/logo.png")
canvas.create_image(160, 100, image=logo_img)
canvas.grid(row=0, column=0, padx=25, pady=20)

# Create what we need for E-mail
epost_label = tk.Label(window, text=" Enter Email/Username")
epost_label.grid(row=1, column=0, sticky="w", padx=(25, 0))
epost_entry = tk.Entry(window, width=15)
epost_entry.grid(row=1, column=1, sticky="w", padx=(10, 0))

# Create what we need for website
website_label = tk.Label(window, text="Enter Website")
website_label.grid(row=2, column=0, sticky="w", padx=(25, 0))
website_entry = tk.Entry(window, width=15)
website_entry.grid(row=2, column=1, sticky="w", padx=(10, 0))

# Create a button to generate the password
pass_btn_generate = tk.Button(window, text="Generate Password", command=password_generator)
pass_btn_generate.grid(row=3, column=0, padx=(25, 0))

# Create a button to save the password
save_btn_generate = tk.Button(window, text="Save Password", command=save_password)
save_btn_generate.grid(row=3, column=1, padx=(10, 0))

# Create a text field (Entry widget) to display the generated password
entry_password = tk.Entry(window)
entry_password.grid(row=4, column=0, columnspan=2, padx=(25, 0), pady=(10, 0))

#... (other code)...
save_btn_generate = tk.Button(window, text="Save Password", command=save_password)
save_btn_generate.grid()

window.mainloop()