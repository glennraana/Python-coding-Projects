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
    # Define the numbers to be used in the password
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


#---------------------------- GUI SETUP ------------------------------- #
# Define the windo( Canvas)
window = tk.Tk()
window.title("Password Generator")

canvas = Canvas(width=300, height=200)
logo_img = PhotoImage(file="Coding/Projects/Password manager/logo.png")
canvas.create_image(150, 100, image=logo_img)
canvas.pack(padx=10, pady=10)


# Create what we need for E-mai/Username input
epost_label = tk.Label(window, text=" Enter Username")
epost_label.pack()
epost_entry = tk.Entry(window, width=20, border=10)
epost_entry.pack()

#Create what we need for website input
website_label = tk.Label(window, text="Enter Website", border=10)
website_label.pack()
website_entry = tk.Entry(window, width=20, border=10)
website_entry.pack()
# # Create a button
# pass_btn_generate = tk.Button(window, text="Generate Password", command=password_generator, width=20)
# pass_btn_generate.pack()    

# Create a text field (Entry widget) to display the generated password
password_label = tk.Label(window, text="Push the button to generate", border=10)
password_label.pack()
pass_btn_generate = tk.Button(window, text="Generate Password", command=password_generator, width=15)
pass_btn_generate.pack()
entry_password = tk.Entry(window, width=20, border=10)
entry_password.pack()


# Create the buttons for Save

save_btn_generate = tk.Button(window, text="Save to file", command=save_password, width=15, border=10)
save_btn_generate.pack() 



# Let the script run
window.mainloop()
