import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.number = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess the number between 1 and 100:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=10)
        
        self.hint_label = tk.Label(root, text="")
        self.hint_label.pack(pady=10)
        
    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return
        
        self.attempts += 1
        
        if user_guess == self.number:
            messagebox.showinfo("Congratulations!", f"You guessed the correct number {self.number} in {self.attempts} attempts.")
            self.root.destroy()
        else:
            hint = provide_hint(user_guess, self.number)
            self.hint_label.config(text=hint)
            self.entry.delete(0, tk.END)

def provide_hint(user_guess, number):
    if user_guess > number:
        return "The random number is lower than your guess."
    else:
        return "The random number is higher than your guess."

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
