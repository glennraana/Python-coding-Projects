# Importing the need for the project
import turtle
import pandas as pd

# Setting up the turtle screen 
screen = turtle.Screen()
screen.title("Map Game")
image = "Coding/Projects/map_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create my turtle
my_turtle = turtle.Turtle()
my_turtle.speed("fast")
my_turtle.hideturtle()

# Load the data and make a date frame out of it 
data = pd.read_csv("Coding/Projects/map_game/50_states.csv")

# make a function for the x cordinates if i want to reuse them
def cordinates_x(state):
    for index, row in data.iterrows():
        if state == row["state"]:
            return row["x"]
# make a function for Y cordinates if i want to reuse them
def cordinates_y(state):
    for index, row in data.iterrows():
        if state == row["state"]:
            return row["y"]
# making a variable for the While loop so the program can keep going until 50 states are right
guessed_states = []
score = 0
# The program 
while len (guessed_states) < 50:
    # The message box on the screen 
    answer_state = screen.textinput(title=f"{len(guessed_states)} /50 states correct", prompt="What's another State name? ").title()
    # The logic 
    if answer_state in data["state"].values:
        guessed_states.append(answer_state)
        go_to_x = cordinates_x(answer_state)
        go_to_y = cordinates_y(answer_state)
        my_turtle.penup()
        my_turtle.goto(go_to_x, go_to_y)
        my_turtle.pendown()
        my_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
        score +=1
    else:
        # We want to be able to play again, so we print the score and ask them if they want play again
        play_again = screen.textinput(title=f"Not a State, your final score is: {score}", prompt="Do you want to play again? Yes or No").lower()
        if play_again == "yes":
            guessed_states = []
            score = 0
        else:
            break

    
# Keep the window open
turtle.mainloop()



































# x_cor = [] 
# y_cor = []

# for index, row in data.iterrows():
#     if state == row["state"]:
#         x_cor.append(row["x"])
#         y_cor.append(row["y"])
        
# print(x_cor, y_cor)
