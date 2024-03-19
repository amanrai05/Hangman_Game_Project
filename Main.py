import tkinter as tk
import random

class HangmanGame(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Hangman Game")
        self.geometry("400x300")
        
        self.word_label = tk.Label(self, text="", font=("Arial", 24))
        self.word_label.pack(pady=10)
        
        self.guess_entry = tk.Entry(self, font=("Arial", 16))
        self.guess_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)
        
        self.info_label = tk.Label(self, text="", font=("Arial", 12))
        self.info_label.pack(pady=5)
        
        self.new_game_button = tk.Button(self, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)
        
        self.instructions = """
        Hangman Game Instructions:
        - Guess the letters to complete the word.
        - You have 6 attempts to guess the word.
        - Avoid guessing double digits and special characters.
        """
        
        self.levels = {
            "Countries": ["USA", "Canada", "Japan", "India", "Brazil", "China", "Mexico"],
            "Fruits": ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Pineapple", "Watermelon"],
            "Flags": ["USA", "UK", "France", "Germany", "Canada", "Australia", "Japan"],
            "Capitals": ["Washington", "London", "Paris", "Berlin", "Ottawa", "Canberra", "Tokyo"]
        }
        
        self.new_game()
    
    def new_game(self):
        self.word = random.choice(self.levels[random.choice(list(self.levels.keys()))])
        self.remaining_attempts = 6
        self.guessed_letters = set()
        self.update_display()
    
    def update_display(self):
        displayed_word = "".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_label.config(text=displayed_word)
        self.info_label.config(text=f"Attempts remaining: {self.remaining_attempts}")
    
    def check_guess(self):
        guess = self.guess_entry.get().strip().upper()
        self.guess_entry.delete(0, tk.END)
        
        if guess.isalpha() and len(guess) == 1 and guess not in self.guessed_letters:
            self.guessed_letters.add(guess)
            if guess not in self.word:
                self.remaining_attempts -= 1
            self.update_display()
            if "_" not in self.word_label.cget("text"):
                self.info_label.config(text="Congratulations! You won!")
        else:
            self.info_label.config(text="Invalid input! ")
        
        if self.remaining_attempts == 0:
            self.info_label.config(text=f"Game over! The word was: {self.word}")
    
    def show_instructions(self):
        tk.messagebox.showinfo("Instructions", self.instructions)

if _name_ == "_main_":
    game = HangmanGame()
    game.mainloop()
