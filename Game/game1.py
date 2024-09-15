 # Import Required Libraries
import tkinter as tk
import random
from tkinter import messagebox


 ### Define the Game Logic
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Pink', 'Orange', 'Purple', 'Brown']

def pick_random_color():
    return random.choice(colors)

def check_guess(player_guess, correct_color):
    if player_guess == correct_color:
        messagebox.showinfo("Correct!", "You guessed the color correctly!")
    else:
        messagebox.showerror("Incorrect", f"Wrong guess! The correct color was {correct_color}.")
    start_new_round()



## Create the GUI
class ColorGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Color Guessing Game")
        self.geometry("400x400")
        self.configure(bg="white")
        
        self.color_label = tk.Label(self, text="", bg="white", width=20, height=10)
        self.color_label.pack(pady=50)
        
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack()

        self.buttons = []
        for color in colors:
            button = tk.Button(self.buttons_frame, text=color, width=15, height=2,
                               command=lambda c=color: check_guess(c, self.current_color))
            button.pack(side=tk.LEFT, padx=5)
            self.buttons.append(button)
        
        self.start_new_round()

    def start_new_round(self):
        self.current_color = pick_random_color()
        self.color_label.config(bg=self.current_color.lower())

if __name__ == "__main__":
    game = ColorGuessingGame()
    game.mainloop()

