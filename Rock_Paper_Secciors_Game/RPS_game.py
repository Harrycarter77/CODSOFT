import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("300x275")

user_score = 0
computer_score = 0

def check_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or (user == "Scissors" and computer == "Paper") or (user == "Paper" and computer == "Rock"):
        return "Win"
    else:
        return "Lose"

def user_choice(choice):
    global user_score, computer_score
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = check_winner(choice, computer_choice)
    
    if result == "Win":
        user_score += 1
    elif result == "Lose":
        computer_score += 1
    
    result_message = f"You chose {choice}\nComputer chose {computer_choice}\nResult: {result}"
    messagebox.showinfo("Result", result_message)
    update_score()
    play_again()

def update_score():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def play_again():
    play_again_response = messagebox.askquestion("Play Again", "Do you want to play another round?")
    if play_again_response == 'no':
        root.quit()

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score()

rock_button = tk.Button(root, text="Rock", width=20, command=lambda: user_choice('Rock'))
paper_button = tk.Button(root, text="Paper", width=20, command=lambda: user_choice('Paper'))
scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: user_choice('Scissors'))

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=('Helvetica', 14))
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Helvetica', 14))

user_score_label.pack(pady=5)
computer_score_label.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", width=20, command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
