import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["python", "developer", "computer", "network", "programming"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e1e")

        self.score = 0
        self.max_attempts = 6

        title = tk.Label(
            root,
            text=" HANGMAN GAME",
            font=("Arial", 24, "bold"),
            bg="#1e1e1e",
            fg="#00ffcc"
        )
        title.pack(pady=10)

        self.score_label = tk.Label(
            root,
            text=f"Score: {self.score}",
            font=("Arial", 14),
            bg="#1e1e1e",
            fg="white"
        )
        self.score_label.pack()

        self.word_label = tk.Label(
            root,
            text="",
            font=("Consolas", 28, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.word_label.pack(pady=20)

        self.attempt_label = tk.Label(
            root,
            text="Attempts Left: 6",
            font=("Arial", 14),
            bg="#1e1e1e",
            fg="#ff6666"
        )
        self.attempt_label.pack()

        self.entry = tk.Entry(
            root,
            font=("Arial", 16),
            width=5,
            justify="center"
        )
        self.entry.pack(pady=15)

        self.guess_btn = tk.Button(
            root,
            text="Guess",
            font=("Arial", 14, "bold"),
            bg="#00cc99",
            fg="white",
            command=self.check_guess
        )
        self.guess_btn.pack()

        self.guessed_label = tk.Label(
            root,
            text="Guessed Letters: ",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="white"
        )
        self.guessed_label.pack(pady=15)

        self.new_game()

    def new_game(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = []
        self.attempts = self.max_attempts
        self.update_display()

    def update_display(self):
        display = ""

        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        self.word_label.config(text=display)
        self.attempt_label.config(
            text=f"Attempts Left: {self.attempts}"
        )

        self.guessed_label.config(
            text="Guessed Letters: " +
            ", ".join(self.guessed_letters)
        )

        self.score_label.config(
            text=f"Score: {self.score}"
        )

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning(
                "Invalid Input",
                "Enter a single alphabet letter!"
            )
            return

        if guess in self.guessed_letters:
            messagebox.showinfo(
                "Already Guessed",
                "You already guessed that letter!"
            )
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.attempts -= 1

        self.update_display()

        won = all(
            letter in self.guessed_letters
            for letter in self.word
        )

        if won:
            self.score += 10

            play_again = messagebox.askyesno(
                "Congratulations!",
                f"You guessed '{self.word}'!\nPlay Again?"
            )

            if play_again:
                self.new_game()
            else:
                self.root.quit()

        elif self.attempts == 0:
            play_again = messagebox.askyesno(
                "Game Over",
                f"The word was '{self.word}'.\nPlay Again?"
            )

            if play_again:
                self.new_game()
            else:
                self.root.quit()


root = tk.Tk()
game = HangmanGame(root)
root.mainloop()