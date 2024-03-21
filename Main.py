import tkinter as tk
import random
import string

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.words = ["python", "hangman", "game", "player", "score", "level"]
        self.allowed_attempts = 6
        self.current_word = ""
        self.guesses = set()
        self.score = 0
        self.level = 1

        self.word_label = tk.Label(root, text="")
        self.word_label.pack()

        self.input_label = tk.Label(root, text="Enter a letter:")
        self.input_label.pack()
        
        self.input_entry = tk.Entry(root)
        self.input_entry.pack()
        
        self.submit_button = tk.Button(root, text="Submit", command=self.make_guess)
        self.submit_button.pack()

        self.level_label = tk.Label(root, text="Level: {}".format(self.level))
        self.level_label.pack()

        self.attempts_label = tk.Label(root, text="")
        self.attempts_label.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.timer_label = tk.Label(root, text="")
        self.timer_label.pack()

        self.instructions_button = tk.Button(root, text="Instructions", command=self.display_instructions)
        self.instructions_button.pack()

        self.update_word_to_guess()
        self.update_attempts_label()

    def update_word_to_guess(self):
        self.current_word = random.choice(self.words)
        masked_word = "".join([letter if letter in self.guesses else "_" for letter in self.current_word])
        self.word_label.config(text=masked_word)

    def make_guess(self):
        letter = self.input_entry.get().lower()
        if letter in string.ascii_lowercase and letter not in self.guesses:
            self.guesses.add(letter)
            if letter not in self.current_word:
                self.allowed_attempts -= 1
            self.update_word_to_guess()
            self.update_attempts_label()
            self.check_win_loss()
        else:
            tk.messagebox.showerror("Error", "Invalid input. Please enter a valid lowercase letter.")

    def update_attempts_label(self):
        self.attempts_label.config(text="Attempts left: {}".format(self.allowed_attempts))

    def check_win_loss(self):
        if all(letter in self.guesses for letter in self.current_word):
            self.score += 10
            self.level += 1
            self.level_label.config(text="Level: {}".format(self.level))
            tk.messagebox.showinfo("Congratulations!", "You won! Your score is {}.".format(self.score))
            self.reset_game()
        elif self.allowed_attempts == 0:
            tk.messagebox.showinfo("Game Over", "You lost. The word was '{}'.".format(self.current_word))
            self.reset_game()

    def reset_game(self):
        self.current_word = ""
        self.guesses = set()
        self.allowed_attempts = 6
        self.update_word_to_guess()
        self.update_attempts_label()

    def display_instructions(self):
        instructions = """
        Hangman Game Instructions:

        - Guess the letters to complete the hidden word.
        - You have 6 attempts to guess the word correctly.
        - Each correct guess earns you 10 points.
        - The game gets harder as you progress to higher levels.
        - Good luck!
        """
        tk.messagebox.showinfo("Instructions", instructions)


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
