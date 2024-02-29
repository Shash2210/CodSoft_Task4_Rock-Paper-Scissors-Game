#!/usr/bin/env python
# coding: utf-8

# In[13]:


import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose."

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_choices_and_result(user_choice, computer_choice, result)
    show_game_frame()

def display_choices_and_result(user_choice, computer_choice, result):
    result_label.config(text=result)
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")

    if 'win' in result:
        user_score_var.set(user_score_var.get() + 1)
    elif 'lose' in result:
        computer_score_var.set(computer_score_var.get() + 1)

    score_label.config(text=f"Score: You - {user_score_var.get()}, Computer - {computer_score_var.get()}")

    
def show_play_frame():
    play_frame.pack()
    game_frame.pack_forget()    

def on_choice_change(*args):
    play_game()


def play_again():
    user_score_var.set(0)
    computer_score_var.set(0)
    
    result_label.config(text="")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    score_label.config(text="Score: You - 0, Computer - 0")
    
    show_play_frame()
    
    
def exit_game():
    final_score_message = ""
    if user_score_var.get() > computer_score_var.get():
        final_score_message = "🎉Congratulations! You win!🎉"
    elif user_score_var.get() < computer_score_var.get():
        final_score_message = "😔Better luck next time!😔"
    elif user_score_var.get() == computer_score_var.get():
        final_score_message = "It's a tie! You can break the tie and win by continuing👍"    

    exit_confirmation = messagebox.askyesno("Exit Game", f"Score: You - {user_score_var.get()}, Computer - {computer_score_var.get()}\n\n{final_score_message}\n\nDo you really want to exit?")
    if exit_confirmation:
        root.destroy()
        
        
        
def show_game_frame():
    play_frame.pack_forget()
    game_frame.pack()

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()

user_choice_var = tk.StringVar()
user_choice_var.trace_add('write', on_choice_change)


play_frame = tk.Frame(root)
play_frame.pack(pady=50)

rules_label_play_frame = tk.Label(play_frame, text="Rules:\nRock defeats Scissors\nPaper defeats Rock\nScissors defeat Paper", font=("Helvetica", 16), pady=50)
rules_label_play_frame.pack()


play_button = tk.Button(play_frame, text="Play", command=show_game_frame, font=("Helvetica", 16), padx=20, pady=10)
play_button.pack(pady=10)


game_frame = tk.Frame(root)

rules_label = tk.Label(game_frame, text="Rules:\nRock defeats Scissors\nPaper defeats Rock\nScissors defeat Paper", font=("Helvetica", 16), pady=50)
rules_label.pack()

choices_frame = tk.Frame(game_frame)
choices_frame.pack(pady=20)

rock_button = tk.Button(choices_frame, font=("Helvetica", 13), text="Rock", command=lambda: user_choice_var.set("rock"), padx=20, pady=10)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(choices_frame, text="Paper", font=("Helvetica", 13), command=lambda: user_choice_var.set("paper"), padx=20, pady=10)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(choices_frame, text="Scissors", font=("Helvetica", 13), command=lambda: user_choice_var.set("scissors"), padx=20, pady=10)
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(game_frame, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

user_choice_label = tk.Label(game_frame, text="", font=("Helvetica", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(game_frame, text="", font=("Helvetica", 12))
computer_choice_label.pack()

score_label = tk.Label(game_frame, text="Score: You - 0, Computer - 0", font=("Helvetica", 12, "italic"))
score_label.pack()

exit_button = tk.Button(game_frame, text="Exit", command=exit_game, font=("Helvetica", 15), padx=20, pady=10)
exit_button.pack(pady=20)

play_again_button = tk.Button(game_frame, text="Play Again", command=play_again, font=("Helvetica", 15), padx=20, pady=10)
play_again_button.pack(pady=10)

game_frame.pack_forget()

root.mainloop()


# In[ ]:




