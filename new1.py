from tkinter import *
from PIL import Image, ImageTk
import os
from random import randint

root = Tk()
root.title("Rock Paper Scissors")

# Function to get the screen width and height
def get_screen_size():
    return root.winfo_screenwidth(), root.winfo_screenheight()

# Load background image with error handling
try:
    bg_path = "new1.png"  # Replace with your background image file path
    if os.path.exists(bg_path):
        screen_width, screen_height = get_screen_size()
        bg_img = Image.open(bg_path)
        bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)  # Resize image using LANCZOS filter
        bg_img = ImageTk.PhotoImage(bg_img)
    else:
        raise FileNotFoundError(f"Error: Background image '{bg_path}' not found.")
except Exception as e:
    print(f"Error loading background image: {e}")
    bg_img = None

if bg_img:
    bg_label = Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the background label to cover the whole window

root.configure(background="#2c3e50")  # Set root background to Dark Blue Gray

# Load images with error handling
try:
    rock_img_user = ImageTk.PhotoImage(Image.open("user_rock.png"))
    paper_img_user = ImageTk.PhotoImage(Image.open("user_paper.png"))
    scissors_img_user = ImageTk.PhotoImage(Image.open("user_scissors.png"))
    rock_img_com = ImageTk.PhotoImage(Image.open("com_rock.png"))
    paper_img_com = ImageTk.PhotoImage(Image.open("com_paper.png"))
    scissors_img_com = ImageTk.PhotoImage(Image.open("com_scissors.png"))
except Exception as e:
    print(f"Error loading images: {e}")
    root.destroy()

# Insert pictures
user_label = Label(root, image=rock_img_user)
com_label = Label(root, image=rock_img_com)
user_label.grid(row=1, column=0, padx=20, pady=20)
com_label.grid(row=1, column=4, padx=20, pady=20)

# Scores
playerscore = Label(root, text=0, font=("Arial", 25), bg="#f39c12", fg="#2c3e50")  # Orange background, Dark Blue Gray text
computerscore = Label(root, text=0, font=("Arial", 25), bg="#f39c12", fg="#2c3e50")  # Orange background, Dark Blue Gray text
playerscore.grid(row=1, column=1, padx=20)
computerscore.grid(row=1, column=3, padx=20)

# Indicators
user_indicator = Label(root, text="USER", font=("Arial", 16), bg="#f39c12", fg="#2c3e50")  # Orange background, Dark Blue Gray text
com_indicator = Label(root, text="COMPUTER", font=("Arial", 16), bg="#f39c12", fg="#2c3e50")  # Orange background, Dark Blue Gray text
user_indicator.grid(row=0, column=1, padx=20)
com_indicator.grid(row=0, column=3, padx=20)

# Messages
msg = Label(root, text="", font=("Arial", 16), bg="#e74c3c", fg="white")  # Red background, white text
msg.grid(row=4, column=2, pady=20)

# Update message
def update_message(text):
    msg.config(text=text)

# Update score
def update_user_score():
    score = int(playerscore["text"])
    score += 1
    playerscore.config(text=str(score))

def update_com_score():
    score = int(computerscore["text"])
    score += 1
    computerscore.config(text=str(score))

# Determine winner
def determine_winner(player, computer):
    if player == computer:
        update_message("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        update_message("You win!")
        update_user_score()
    else:
        update_message("You lose!")
        update_com_score()

# Update choices
choices = ["rock", "paper", "scissors"]
def update_choice(player_choice):
    computer_choice = choices[randint(0, 2)]
    
    if computer_choice == "rock":
        com_label.config(image=rock_img_com)
    elif computer_choice == "paper":
        com_label.config(image=paper_img_com)
    else:
        com_label.config(image=scissors_img_com)
    
    if player_choice == "rock":
        user_label.config(image=rock_img_user)
    elif player_choice == "paper":
        user_label.config(image=paper_img_user)
    else:
        user_label.config(image=scissors_img_user)
    
    determine_winner(player_choice, computer_choice)

# Restart game
def restart_game():
    playerscore.config(text="0")
    computerscore.config(text="0")
    msg.config(text="")
    user_label.config(image=scissors_img_user)
    com_label.config(image=scissors_img_com)

# Buttons
rock_btn = Button(root, text="ROCK", width=25, height=2, bg="#3498db", fg="white", command=lambda: update_choice("rock"))  # Light Blue background, white text
paper_btn = Button(root, text="PAPER", width=25, height=2, bg="#2ecc71", fg="white", command=lambda: update_choice("paper"))  # Green background, white text
scissors_btn = Button(root, text="SCISSORS", width=25, height=2, bg="#e74c3c", fg="white", command=lambda: update_choice("scissors"))  # Red background, white text
restart_btn = Button(root, text="RESTART", width=25, height=2, bg="#9b59b6", fg="white", command=restart_game)  # Purple background, white text

rock_btn.grid(row=2, column=1, pady=10)
paper_btn.grid(row=2, column=2, pady=10)
scissors_btn.grid(row=2, column=3, pady=10)
restart_btn.grid(row=3, column=2, pady=10)

root.mainloop()
