import tkinter as tk
from tkinter import messagebox
import random
import string

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.words = ["hangman", "python", "game", "player", "score", "hello", "world"]  # Add more words here
        self.current_word = random.choice(self.words)
        self.guesses = set()
        self.attempts = 6
        self.level = 1
        self.score = 0
        self.timer = None

        self.create_widgets()

    def create_widgets(self):
        self.instruction_button = tk.Button(self.root, text="Instructions", command=self.show_instructions)
        self.instruction_button.pack()

        self.word_label = tk.Label(self.root, text="Word: " + self.hide_word())
        self.word_label.pack()

        self.attempts_label = tk.Label(self.root, text="Attempts left: " + str(self.attempts))
        self.attempts_label.pack()

        self.level_label = tk.Label(self.root, text="Level: " + str(self.level))
        self.level_label.pack()

        self.score_label = tk.Label(self.root, text="Score: " + str(self.score))
        self.score_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.make_guess)
        self.submit_button.pack()

    def hide_word(self):
        return ''.join([letter if letter in self.guesses else '_' for letter in self.current_word])

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            messagebox.showerror("Invalid Guess", "Please enter a single letter.")
            return

        if guess in self.guesses:
            messagebox.showinfo("Duplicate Guess", "You have already guessed this letter.")
            return

        self.guesses.add(guess)
        if guess not in self.current_word:
            self.attempts -= 1
            self.update_attempts()

        self.update_word()

        if self.attempts == 0:
            self.game_over()

        if self.hide_word() == self.current_word:
            self.level += 1
            self.score += 10
            self.start_next_level()

    def update_attempts(self):
        self.attempts_label.config(text="Attempts left: " + str(self.attempts))

    def update_word(self):
        self.word_label.config(text="Word: " + self.hide_word())

    def start_next_level(self):
        self.current_word = random.choice(self.words)
        self.guesses = set()
        self.attempts = 6
        self.level_label.config(text="Level: " + str(self.level))
        self.attempts_label.config(text="Attempts left: " + str(self.attempts))
        self.score_label.config(text="Score: " + str(self.score))
        self.update_word()

    def game_over(self):
        messagebox.showinfo("Game Over", "You ran out of attempts. The word was: " + self.current_word)
        self.root.destroy()

    def show_instructions(self):
        instructions = """
        Hangman Game Instructions:
        - Guess the letters to reveal the word.
        - You have limited attempts.
        - Each correct guess earns you points.
        - Press 'Submit Guess' to make a guess.
        - Have fun!
        """
        messagebox.showinfo("Instructions", instructions)

def main():
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
