from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
# window.minsize(width=400, height=300)
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
generate_btn = Button(text="Generate")
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=34, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

# Main Loop
window.mainloop()
