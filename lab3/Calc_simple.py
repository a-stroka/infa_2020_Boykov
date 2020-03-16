from tkinter import*
from tkinter import messagebox


def minus():
    try:
        l['text'] = float(e1.get()) - float(e2.get())
    except (ValueError, ZeroDivisionError):
        messagebox.showinfo("GUI Python",
                            "Нужно вводить числа, делить на ноль нельзя")
def plus():
    try:
        l['text'] = float(e1.get()) + float(e2.get())
    except (ValueError, ZeroDivisionError):
        messagebox.showinfo("GUI Python",
                            "Нужно вводить числа, делить на ноль нельзя")
def delenie():
    try:
        l['text'] = float(e1.get()) / float(e2.get())
    except (ValueError, ZeroDivisionError):
        messagebox.showinfo("GUI Python",
                            "Нужно вводить числа, делить на ноль нельзя")
def umnogenie():
    try:
        l['text'] = float(e1.get()) * float(e2.get())
    except (ValueError, ZeroDivisionError):
        messagebox.showinfo("GUI Python",
                            "Нужно вводить числа, делить на ноль нельзя")

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    l.config(text="")

root = Tk()
root.title("Простой калькулятор")

f_top = Frame(root)
f_bot = Frame(root)

e1 = Entry(f_top, width=3, font=("Arial", 20), justify=CENTER)
e2 = Entry(f_top, width=3, font=("Arial", 20), justify=CENTER)
b1 = Button(f_bot, width=5, height=2, text="-", command=minus)
b2 = Button(f_bot, width=5, height=2, text="+", command=plus)
b3 = Button(f_bot, width=5, height=2, text="/", command=delenie)
b4 = Button(f_bot, width=5, height=2, text="x", command=umnogenie)
b5 = Button(f_bot, width=5, height=2, text="C", command=clear)
l = Label(f_top, bg='black', fg='white',
          width=3, height=1, font=("Arial", 20), justify=CENTER)

f_top.pack(padx=10, pady=10)
f_bot.pack(padx=10, pady=10)

e1.pack(side=LEFT)
e2.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
l.pack(side=LEFT)


root.mainloop()