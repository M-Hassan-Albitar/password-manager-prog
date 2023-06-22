from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [choice(letters) for _ in range(randint(8, 10))]
    nr_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    nr_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = nr_letters + nr_symbols + nr_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_txt = website_entry.get()
    email_txt = email_entry.get()
    password_txt = password_entry.get()

    if len(website_txt) == 0 or len(password_txt) == 0:
        messagebox.showinfo(message="You can't leave any value empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_txt,
                                       message=f"Is it ok to save ?\nWebsite: {website_txt}\nEmail: {email_txt}\nPassword: {password_txt}")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website_txt} | {email_txt} | {password_txt}\n")
            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email / Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=36)
email_entry.insert(0, "mohamed@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate", command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=34, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

# Main Loop
window.mainloop()
