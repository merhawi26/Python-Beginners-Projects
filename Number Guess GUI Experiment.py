import tkinter as tk


from tkinter import Label, Entry, Button, messagebox

import random


class NumberGuessGame:

    def __init__(self, random_value):
        self.random_value = random_value
        self.root = tk.Tk()
        self.root.title("Number Guess Game")
        self.root.geometry("500x300")
        self.root.configure(bg="#2F4F4F")

        self.entry_label = Label(self.root, text="Guess a number between 1 - 100")
        self.entry_label.pack(pady=10)

        self.entry = Entry(self.root)
        self.entry.pack(pady=10)

        self.try_button = Button(self.root, text="Guess", command=self.game)
        self.try_button.pack(pady=10)

        self.guessed_result_label = Label(
            self.root, text="", fg="yellow", bg="#2F4F4F", font=("Arial", 12, "bold")
        )
        self.guessed_result_label.pack(pady=10)
        self.root.mainloop()

    def game(self):
        input_from_user = self.user_input()

        if input_from_user > self.random_value:

            self.guess_result("Too high")

        elif input_from_user < self.random_value:

            self.guess_result("Too low")
        else:

            self.guess_result(
                f"Congratulations! You guessed right, the number was : {self.random_value}"
            )

    def user_input(self):

        try:
            input_from_user = int(self.entry.get())
            if 1 <= input_from_user <= 100:
                return input_from_user
            else:

                self.show_error_label(f"Please, Enter the value between 1 - 100")
                return None
        except:
            self.show_error_label(f"Please, Enter the correct value")

            return None

    def guess_result(self, message):
        self.guessed_result_label.config(text=message)

    def show_error_label(self, message):
        messagebox.showerror("Error", message)


random_value = random.randint(1, 100)
NumberGuessGame(random_value)
