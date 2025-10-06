import tkinter
from  tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10)) ]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4)) ]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password_f = "".join(password_list)
    password.insert(0, password_f)
    pyperclip.copy(password_f) # The generated password will automatically pasted

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if not website_name.get() or not user_name.get() or not password.get():
        messagebox.showinfo(title = "OOPs", message = "Some Entries are Missing")
    else:
        is_ok = messagebox.askokcancel(title = website_name.get(), message = f"These are the details entered : "
                              f"\nEmail:{user_name} \npassword:{password} \nIs it ok to save?")
        if is_ok:
            with open("password.txt","a") as file:

                file.write(f"\nWebsite = {website_name.get()}") # will only take string to convert website_name to string by .get()
                file.write(f"\nUser Name = {user_name.get()}")
                file.write(f"\nPassword =  {password.get()}\n")
                website_name.delete(0,"end")
                user_name.delete(0,"end")
                password.delete(0,"end")
                website_name.focus_set()



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50)

canvas = tkinter.Canvas(width = 200, height = 200)
lock_pic = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = lock_pic)
canvas.grid(row = 0 , column = 1,)

website_label = tkinter.Label(text = "Website")
website_label.grid(row = 1 , column = 0)

email_label = tkinter.Label(text = "Email/Username")
email_label.grid(row = 2 , column = 0)

password_label = tkinter.Label(text = "Password")
password_label.grid(row = 3 , column = 0)

generate_button = tkinter.Button(text = "Generate Password",command = generate_password)
generate_button.grid(row = 3 , column = 2)

add_button = tkinter.Button(text = "Add",width = 36,command = save)
add_button.grid(row = 4 , column = 1,columnspan = 2)

website_name = tkinter.Entry(width = 35)
website_name.grid(row = 1 , column = 1, columnspan = 2)
website_name.focus_set()

user_name = tkinter.Entry(width = 35)
user_name.grid(row = 2 , column = 1, columnspan = 2)

password = tkinter.Entry(width = 18)
password.grid(row = 3 , column = 1)


window.mainloop()