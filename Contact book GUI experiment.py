import tkinter as tk
from tkinter import messagebox, simpledialog, font as tkfont


class ContactBook:
    def __init__(self):
        self.contact_book = []
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Contact Book")
        self.root.geometry("500x600")
        self.root.configure(bg="#2A2A2A")

        # Font Styles
        header_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        button_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        # Header Label
        self.header_label = tk.Label(
            self.root,
            text="My Contact Book",
            font=header_font,
            fg="#FFD700",
            bg="#2A2A2A",
        )
        self.header_label.pack(pady=(10, 10))

        # Display Box
        self.text_box = tk.Text(
            self.root,
            height=15,
            width=50,
            bg="#FFF8DC",
            fg="#000000",
            font=("Helvetica", 10),
            relief="sunken",
            bd=2,
        )
        self.text_box.pack(pady=(10, 10))

        # Buttons
        buttons_frame = tk.Frame(self.root, bg="#2A2A2A")
        buttons_frame.pack(pady=20)

        self.create_button(
            "Add Contact", self.add, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "View Contacts", self.view, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "Search Contact", self.search, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "Update Contact", self.update, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "Delete Contact", self.delete, buttons_frame, button_font, "#FF6347"
        )
        self.create_button(
            "Exit", self.root.destroy, buttons_frame, button_font, "#FF6347"
        )

        self.root.mainloop()

    def create_button(self, text, command, frame, font, color):
        button = tk.Button(
            frame,
            text=text,
            command=command,
            font=font,
            bg=color,
            fg="#FFFFFF",
            relief="flat",
            width=15,
        )
        button.pack(pady=5, padx=5)

    def add(self):
        name, phone, email, address = (
            simpledialog.askstring("Input", "Enter the name:").lower(),
            simpledialog.askstring("Input", "Enter the phone number:"),
            simpledialog.askstring("Input", "Enter the email:").lower(),
            simpledialog.askstring("Input", "Enter the address:").lower(),
        )

        if name and phone:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address,
            }
            self.contact_book.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")

        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def view(self):
        self.text_box.delete(1.0, tk.END)
        if not self.contact_book:
            self.text_box.insert(tk.END, "No contacts found.\n")
        else:

            for contact in self.contact_book:
                self.text_box.insert(tk.END, f"Name: {contact['name']}\n")
                self.text_box.insert(tk.END, f"Phone: {contact['phone']}\n")
                self.text_box.insert(tk.END, f"Email: {contact['email']}\n")
                self.text_box.insert(tk.END, f"Address: {contact['address']}\n\n")

    def search(self):
        search_name = simpledialog.askstring(
            "Search", "Enter the name to search:"
        ).lower()
        found = False
        self.text_box.delete(1.0, tk.END)
        for contact in self.contact_book:
            if contact["name"] == search_name:
                self.text_box.insert(tk.END, f"Contact Found:\n")
                self.text_box.insert(tk.END, f"Name: {contact['name']}\n")
                self.text_box.insert(tk.END, f"Phone: {contact['phone']}\n")
                self.text_box.insert(tk.END, f"Email: {contact['email']}\n")
                self.text_box.insert(tk.END, f"Address: {contact['address']}\n\n")
                found = True
                break
        if not found:
            messagebox.showinfo("Not Found", "Contact Not Found")

    def update(self):
        name_to_update = simpledialog.askstring(
            "Update", "Enter the name of the contact to update:"
        ).lower()
        for contact in self.contact_book:
            if contact["name"] == name_to_update:
                new_name = (
                    simpledialog.askstring(
                        "Update", "Enter new name (leave blank to keep current):"
                    )
                    or contact["name"]
                )
                new_phone = (
                    simpledialog.askstring(
                        "Update", "Enter new phone (leave blank to keep current):"
                    )
                    or contact["phone"]
                )
                new_email = (
                    simpledialog.askstring(
                        "Update", "Enter new email (leave blank to keep current):"
                    )
                    or contact["email"]
                )
                new_address = (
                    simpledialog.askstring(
                        "Update", "Enter new address (leave blank to keep current):"
                    )
                    or contact["address"]
                )

                contact.update(
                    {
                        "name": new_name.lower(),
                        "phone": new_phone,
                        "email": new_email,
                        "address": new_address.lower(),
                    }
                )
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.view()
                return
        messagebox.showinfo("Not Found", "Contact Not Found")

    def delete(self):
        delete_name = simpledialog.askstring(
            "Delete", "Enter the name of the contact to delete:"
        ).lower()
        for contact in self.contact_book:
            if contact["name"] == delete_name:
                self.contact_book.remove(contact)

                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.view()
                return
        messagebox.showinfo("Not Found", "Contact Not Found")


# Instantiate the ContactBook GUI
ContactBook()
