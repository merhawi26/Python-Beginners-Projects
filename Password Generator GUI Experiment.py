import random
import tkinter as tk

from tkinter import Label, Button, Entry, messagebox


class Password:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#2F4F4F")

        self.entry_label = Label(
            self.root,
            text="Enter the length of the password",
            fg="#FFD700",
            bg="#2A2A2A",
        )
        self.entry_label.pack(pady=10)

        self.entry = Entry(
            self.root, width=30, bg="#D3D3D3", fg="#000000", font=("Helvetica", 10)
        )
        self.entry.pack(pady=10)

        self.generate_button = Button(
            self.root, text="Generate", command=self.generate_password
        )
        self.generate_button.pack(pady=10)

        self.generated_result_label = Label(
            self.root, text="", fg="yellow", bg="#2F4F4F"
        )
        self.generated_result_label.pack(pady=10)

        self.root.mainloop()

    def generate_password(self):
        length = self.password_length()
        count = 0
        password = ""
        while count < self.password_length():
            password += random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
            )
            count += 1
        print(f"password :  {password}")  # Displays on command line
        self.generated_result(f"Generated Password : {password}")
        with open("password.txt", "w") as file:
            file.write(password)

    def password_length(self):
        try:
            length = int(self.entry.get())
            return length

        except:
            messagebox.showerror("Error", "Please, Enter integer value")
            return None

    def generated_result(self, message):
        self.generated_result_label.config(text=message)


Password()
