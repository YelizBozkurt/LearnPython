from tkinter import *


def record(x):
    s = len(enter.get())
    enter.insert(s, str(x))


account = 7
s1 = 0


def trantactions(x):
    global account
    account = x
    global s1
    s1 = float(enter.get())
    print(account)
    print(s1)
    enter.delete(0, "end")


s2 = 0


def calculate():
    global s2
    s2 = float(enter.get())
    print(s2)
    global account
    result = 0

    if account == 0:
        result = s1 + s2
    elif account == 1:
        result = s1 - s2
    elif account == 2:
        result = s1 * s2
    elif account == 3:
        result = s1 / s2
    enter.delete(0, "end")
    enter.insert(0, str(result))


window = Tk()
window.title("Calculator")
window.geometry("500x500")
enter = Entry(fg="RED", bg="GRAY", font="Verdana 14 bold", width=20, justify=RIGHT)
enter.place(x=80, y=20)
b = []
for i in range(1, 10):
    b.append(Button(text=str(i), font="Verdana 14 bold", width=4, command=lambda x=i: record(x)))

counter = 0
for i in range(0, 3):
    for j in range(0, 3):
        b[counter].place(x=80 + j * 70, y=80 + i * 70)
        counter += 1

process = []

for i in range(0, 4):
    process.append(Button(fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=lambda x=i: trantactions(x)))

process[0]["text"] = "+"
process[1]["text"] = "-"
process[2]["text"] = "*"
process[3]["text"] = "/"
for i in range(0, 4):
    process[i].place(x=300, y=80 + 50 * i)

noneb = Button(text=0, fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=lambda x=0: record(x))
noneb.place(x=80, y=280)
pointb = Button(text=".", fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=lambda x=".": record(x))
pointb.place(x=220, y=280)
equalb = Button(text="=", fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=calculate)
equalb.place(x=300, y=280)

window.mainloop()
