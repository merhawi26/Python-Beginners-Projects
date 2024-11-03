import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage


class TodoList:

    def __init__(self):
        # Creating window
        self.window = tk.Tk()
        self.icon = PhotoImage(file="logoo.png")
        self.window.iconphoto(True, self.icon)
        self.window.title("Todo List")
        self.window.geometry("400x300")

        # Writing welcome text while the opened
        self.label = tk.Label(self.window, text="Welcome")
        self.label.pack(pady=10)

        # Entry where the user enters the new task
        self.entry = tk.Entry(self.window, width=40, fg="grey")
        self.entry.insert(0, "Write the new task here")
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_focus_out)
        self.entry.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # View task button
        self.view_button = tk.Button(
            self.window, text="View Task", command=self.view_task
        )
        self.view_button.pack(pady=5)
        # Mark as Completed button
        self.complete_button = tk.Button(
            self.window, text="Mark Completed Task", command=self.task_completed
        )
        self.complete_button.pack(pady=5)

        self.window.mainloop()

    def add_task(self):

        new_task = self.entry.get()
        if new_task and new_task != "Write the new task here":
            with open("Todo.txt", "a") as file:
                file.write(new_task + "\n")

            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Write the new task here")
            self.entry.config(fg="grey")
            messagebox.showinfo("Success", "Task Added Successfully")
        else:
            messagebox.showinfo("Warning", "Please, Enter a valid task ")

    def view_task(self):
        try:
            with open("Todo.txt", "r") as file:
                tasks = file.readlines()
                task_list = ""
                for i, j in enumerate(tasks, 1):
                    task_list += f"{i}. {j.strip()}\n"
                messagebox.showinfo("Todo List", task_list)
        except FileNotFoundError:
            messagebox.showinfo("Warning", "No tasks present")

    def task_completed(self):
        try:
            with open("Todo.txt", "r") as file:
                task = file.readlines()
                task_list = ""
                # task_list = "\n".join(f"{i}. {j.strip()}" for i, j in enumerate(task, 1))
                for i, j in enumerate(task, 1):
                    task_list += f"{i}.{j.strip()}\n"

                completed_task = int(
                    simpledialog.askstring(
                        "Task Completed", f"Select a task number : \n{task_list}"
                    )
                )

                completed_task_desc = task[completed_task - 1].strip()
                task.remove(task[completed_task - 1])

                with open("Todo.txt", "w") as file:
                    file.writelines(task)
                messagebox.showinfo(
                    "Success", f"You have completed : {completed_task_desc}"
                )
        except (IndexError, ValueError):
            messagebox.showwarning("Warning", "The task is not found in your todo list")

    def on_entry_click(self, event):

        if self.entry.get() == "Write the new task here":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="white")

    def on_focus_out(self, event):

        if self.entry.get() == "":
            self.entry.insert(0, "Write the new task here")
            self.entry.config(fg="grey")


TodoList()
