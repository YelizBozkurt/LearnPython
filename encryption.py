from tkinter import *

informations = ("Yeliz", "1234")
trial_right = 3

def Login():
    global trial_right
    if trial_right <= 0:
        return False

    uName = name.get()
    chipher = password.get()
    print(uName, "-", chipher)
    print("Being checked...")

    if (uName == informations[0] and chipher == informations[1]):
        print("Your login has been confirmed")
        result.config(text="ID: 12345, Driving license number: 345")
        ClearScreen()
    else:
        print("Informations are wrong")
        trial_right -= 1
        result.config(text=f"Informations are wrong! Remaining trials: {trial_right}")

def ClearScreen():
    welcome.config(text="Welcome to Yeliz's system..")
    nameask.destroy()
    name.destroy()
    passwordask.destroy()
    password.destroy()
    btn.destroy()

window = Tk()
window.title("Login Screen")
window.geometry("400x400+100+100")

welcome = Label(window, text="Welcome, please enter your information")
welcome.pack()

nameask = Label(window, text="User Name: ")
nameask.pack()

name = Entry(window)
name.pack()

passwordask = Label(window, text="Password: ")
passwordask.pack()

password = Entry(window)
password.pack()

btn = Button(window, text="Login", command=Login)
btn.pack()

result = Label(window, text="No login yet")
result.pack()

window.mainloop()