import tkinter as tk
from tkinter import Entry, Label, messagebox, Button
import random


class RockPaperScissorGame:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissor Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#2F4F4F")

        self.entry_label = Label(
            self.root,
            text="Enter your choose ROCK-r, PAPER-p, SCISSOR-s\nPlayer: ",
            fg="white",
            bg="#2F4F4F",
            font=("Arial", 10),
        )
        self.entry_label.pack(pady=10)
        self.entry = Entry(self.root)
        self.entry.pack(pady=10)

        self.play_button = Button(self.root, text="Play", command=self.game)
        self.play_button.pack(pady=10)

        self.wins_label = Label(
            self.root, text="", fg="yellow", bg="#2F4F4F", font=("Arial", 12, "bold")
        )
        self.wins_label.pack(pady=10)

        self.root.mainloop()

    def game(self):

        player = self.get_inputs()
        computer_choice = random.choice(["r", "p", "s"])

        if (
            (player == "r" and computer_choice == "s")
            or (player == "s" and computer_choice == "p")
            or (player == "p" and computer_choice == "r")
        ):

            self.wins_results(
                f"Player wins😎\nPlayer chose : {player}\nComputer chose : {computer_choice} "
            )

        elif (
            (player == "s" and computer_choice == "r")
            or (player == "p" and computer_choice == "s")
            or (player == "r" and computer_choice == "p")
        ):

            self.wins_results(
                f"Computer wins😎\nPlayer chose : {player}\nComputer chose: {computer_choice} "
            )

        elif player not in ["r", "s", "p"]:
            self.show_error("Wrong value inserted! Try again")

        else:
            self.wins_results(
                f"Game Tie😎\nPlayer chose : {player}\nComputer chose : {computer_choice} "
            )

    def get_inputs(self):
        player = self.entry.get().lower()
        return player

    def wins_results(self, message):
        self.wins_label.config(text=message)

    def show_error(self, message):
        messagebox.showerror("Error", message)
        self.entry.delete(0, tk.END)


RockPaperScissorGame()
