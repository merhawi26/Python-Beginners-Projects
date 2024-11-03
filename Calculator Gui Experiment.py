import tkinter as tk
from tkinter import Label, Entry, Button, LabelFrame, messagebox


class Calculator:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Calculator Experiment")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")

        self.num1_entry_label = Label(self.root, text="Enter the first number : ")
        self.num1_entry_label.grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = Entry(self.root)
        self.num1_entry.grid(row=0, column=1)
        self.num1_entry_label.config(font=("Arial", 10))

        self.num2_entry_label = Label(self.root, text="Enter the second number : ")
        self.num2_entry_label.grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = Entry(self.root)
        self.num2_entry.grid(row=1, column=1)
        self.num2_entry_label.config(font=("Arial", 10))

        # Creating frame for the operations
        self.operations_frame = LabelFrame(self.root, text="Operations\n ")
        self.operations_frame.grid(row=2, column=0, columnspan=6, pady=10)
        self.operations_frame.config(bg="green", font=("Arial", 12, "bold"))

        self.add_button = Button(self.operations_frame, text="Sum", command=self.add)
        self.add_button.grid(row=0, column=0)

        self.difference_button = Button(
            self.operations_frame, text="Difference", command=self.subtract
        )
        self.difference_button.grid(row=0, column=1)

        self.product_button = Button(
            self.operations_frame, text="Product", command=self.multiply
        )
        self.product_button.grid(row=0, column=2)

        self.quotient_button = Button(
            self.operations_frame, text="Quotient", command=self.divide
        )
        self.quotient_button.grid(row=0, column=3)

        self.result_label = Label(self.root, text=" ")
        self.result_label.grid(row=3, column=0, columnspan=6)
        self.result_label.config(font=("Arial", 12, "bold"), fg="#FF0000")

        self.root.mainloop()

    def add(self):
        num1, num2 = self.get_inputs()
        result = num1 + num2
        # messagebox.showinfo("Success", f"Summation Result : {result}")
        self.show_result(f"Summation Result : {result}")

    def subtract(self):
        num1, num2 = self.get_inputs()
        result = num1 - num2
        # messagebox.showinfo("Success", f"Difference Result : {result}")
        self.show_result(f"Difference Result : {result}")

    def multiply(self):
        num1, num2 = self.get_inputs()
        result = num1 * num2
        # messagebox.showinfo("Success", f"Multiplication Result : {result}")
        self.show_result(f"Multiplication Result : {result}")

    def divide(self):
        num1, num2 = self.get_inputs()
        try:
            result = num1 / num2
            # messagebox.showinfo("Success", f"Quotient Result : {result}")
            self.show_result(f"Quotient Result : {result}")
        except ZeroDivisionError:
            # messagebox.showerror("Error", "Division by zero is not allowed.")
            self.show_error("Division by zero is not allowed.")
            return None

    def get_inputs(self):
        if self.num1_entry.get() and self.num2_entry.get() != "":
            num1, num2 = float(self.num1_entry.get()), float(self.num2_entry.get())
            return num1, num2
        else:
            # messagebox.showerror("Error", "Please enter valid numbers.")
            self.show_error("Please enter valid numbers.")

    def show_result(self, message):
        self.result_label.config(text=message)

    def show_error(self, message):
        messagebox.showerror("Error", message)


Calculator()
