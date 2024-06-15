#------------------------------------Importing modules---------------------------#

import requests
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#----------------------API Function Chuck Norris jokes--------------------------#

# I want to make a function that connects to the API and returns a joke
def chuck_joke():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxx",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    json_data = response.json()
    chuck_joke = json_data["value"]
    return chuck_joke

#-------------------------------API Functions: Google Translate--------------------#

# I want to make a function that connects the API, and then use the API to translate the joke to Norwegian.

def translate_joke():
    url = "https://google-translator9.p.rapidapi.com/v2"
    payload = {
        "q": chuck_joke(),
        "source": "en",
        "target": "no-NO",
        "format": "text"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
        "X-RapidAPI-Host": "google-translator9.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    json_data = response.json()
    translated_text = json_data["data"]["translations"][0]["translatedText"]
    return translated_text
#---------------------------GUI Setup------------------------------------------------------#
# using Tkinter to make a GUI Setup
window = tk.Tk()
window.title("Chuck Norris Joke Machine")

# Load double background images
logo_img = PhotoImage(file="/Users/glenn/Documents/Visual code workspace/Coding/Projects/Chuck Norris App/card_back.png")
overlay_img = PhotoImage(file="/Users/glenn/Documents/Visual code workspace/Coding/Projects/Chuck Norris App/card_front.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=logo_img)
canvas.create_image(400, 263, image=overlay_img)
canvas.pack(padx=50, pady=50)

# Create a label to display the joke on the picture.
printed_joke = translate_joke()
joke_label = Label(window, text=printed_joke, font=("Inter", 40, "bold"), fg="black", bg="white", wraplength=650)
joke_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# Create a button function to get a new joke
def get_new_joke():
    global printed_joke
    printed_joke = translate_joke()
    joke_label.config(text=printed_joke)

new_joke_button = Button(window, text="Get New Joke", command=get_new_joke, font=("Helvetica", 18), width=30, height=3, bd=1, bg="#4CAF50", fg="Black")
new_joke_button.pack(pady=20)

window.mainloop()
