import json
from tkinter import *
from tkinter import messagebox
import secrets
import string
import os

def generate_password():
    num_letters = 8
    num_digits = 4
    num_symbols = 4

    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Generate password
    password = (
        ''.join(secrets.choice(letters) for _ in range(num_letters)) +
        ''.join(secrets.choice(digits) for _ in range(num_digits)) +
        ''.join(secrets.choice(symbols) for _ in range(num_symbols))
    )

    # Shuffle the characters to make the password more random
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    final_password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, final_password)

def save_data():
    w_entry = website_entry.get()
    e_entry = email_entry.get()
    p_entry = password_entry.get()
    
    new_data = {
        w_entry: {
            "email": e_entry,
            "password": p_entry
        }
    }

    if len(w_entry) == 0 or len(p_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure to fill details correctly")
    else:
        is_ok = messagebox.askyesnocancel(title="Title", message=f"These are the details you have entered:\nEmail: {e_entry}\nPassword: {p_entry}")
        if is_ok:
            file_path = "newfile.json"
            try:
                with open(file_path, 'r') as file:
                    # Reading the data
                    data = json.load(file)
            except FileNotFoundError:
                data = {}
            except json.JSONDecodeError:
                # Handle the case where the file is empty or not properly formatted
                messagebox.showerror(title='Error', message="Error decoding JSON data in the file")
            else:
                # Updating the data
                data.update(new_data)
                with open(file_path, "w") as file:
                # Saving the data
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def find_password():
    # Load data from JSON file
    try:
        with open("newfile.json", "r") as file:
            data = json.load(file)
        # Get the entered website and email
        entered_website = website_entry.get()
        entered_email = email_entry.get()

        # Check if the entered website and email match any data in the file
        if entered_website in data and data[entered_website]["email"].lower() == entered_email.lower():
            messagebox.showinfo(title=entered_website, message=f"Email: {entered_email}\nPassword: {data[entered_website]['password']}")
        else:
            messagebox.showerror(title="No file found", message="File not available")
    except FileNotFoundError:
        # Handle the case where the file is empty or not properly formatted
        messagebox.showinfo(title="Error", message="Error decoding JSON data in the file")

# -----------------------------------------------------UI -----------------------------#

window = Tk()
window.title("Welocme to Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file=r"C:\Users\ASUS\Pictures\Screenshots\var.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=0)

website_label = Label(text="Website:", font=("italic", 20))
website_label.grid(row=1, column=0, sticky=W)

email_label = Label(text="Email/Username:", font=("italic", 20))
email_label.grid(row=2, column=0, sticky=W)

password_label = Label(text="Password:", font=("italic", 20))
password_label.grid(row=3, column=0, sticky=W)

# Change the width of the "Generate password" button to make it consistent
generate_button_width = 18

button_generate = Button(text="Generate Password", command=generate_password, width=generate_button_width)
button_generate.grid(column=3, row=3)

# Define the width of the "Search" button to match the "Generate password" button
button_search_width = generate_button_width

button_search = Button(text="Search", command=find_password, width=button_search_width)
button_search.grid(column=3, row=1)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "indra@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

add_button = Button(text="Add", width=36, bg="blue", command=save_data)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
