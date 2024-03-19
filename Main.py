import tkinter as tk
import random

class HangmanGame:
    def _init_(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.words_animals = ['dog', 'cat', 'elephant', 'giraffe', 'lion']
        self.words_countries = ['india', 'france', 'canada', 'brazil', 'australia']
        self.words_flags = ['usa', 'uk', 'germany', 'japan', 'italy']
        self.words = self.words_animals + self.words_countries + self.words_flags

        self.word = random.choice(self.words)
        self.guesses = []
        self.attempts = 6

        self.word_display = tk.StringVar()
        self.word_display.set('_ ' * len(self.word))

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, textvariable=self.word_display, font=('Arial', 18))
        self.word_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.guess_label = tk.Label(self.root, text="Guess a letter:", font=('Arial', 14))
        self.guess_label.grid(row=1, column=0, padx=10, pady=10)

        self.guess_entry = tk.Entry(self.root, font=('Arial', 14))
        self.guess_entry.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess, font=('Arial', 14))
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts}", font=('Arial', 14))
        self.attempts_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        if guess in self.guesses:
            tk.messagebox.showwarning("Warning", "You already guessed that letter!")
        elif guess in self.word:
            self.guesses.append(guess)
            self.update_word_display()
            if '_' not in self.word_display.get():
                tk.messagebox.showinfo("Congratulations", f"You won! The word was: {self.word}")
                self.reset_game()
        else:
            self.attempts -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            if self.attempts == 0:
                tk.messagebox.showerror("Game Over", f"Sorry, you lost! The word was: {self.word}")
                self.reset_game()

        self.guess_entry.delete(0, tk.END)

    def update_word_display(self):
        display = ''
        for char in self.word:
            if char in self.guesses:
                display += char + ' '
            else:
                display += '_ '
        self.word_display.set(display)

    def reset_game(self):
        self.word = random.choice(self.words)
        self.guesses = []
        self.attempts = 6
        self.word_display.set('_ ' * len(self.word))
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

if _name_ == "_main_":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()
