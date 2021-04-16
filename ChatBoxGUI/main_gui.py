import SignUpGUI
import LoginPageGUI
import SUserSignUpGUI
from tkinter import *
# # =========================REMEMBER IMPORTANT GENERATING THE EXE FILE==================================================================
# pyinstaller --onefile --icon=.\ChatBoxGUI\icon.ico  ".\ChatBoxGUI\main_gui.py"
# # =====================================================================================================================================

# setting switch function:


def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        # root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        # homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


root = Tk()
root.geometry("1300x700")
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
root.title("Chat Box")
# setting switch state:
btnState = False
# loading Navbar icon image:
navIcon = PhotoImage(file=r"./ChatBoxGUI/ham.png")
closeIcon = PhotoImage(file=r"./ChatBoxGUI/goback.png")
login = PhotoImage(file=r"./ChatBoxGUI/login.png", height=100, width=100)
signup = PhotoImage(file=r"./ChatBoxGUI/signup.png", height=100, width=105)
find = PhotoImage(file=r"./ChatBoxGUI/find.png", height=100, width=105)
delete = PhotoImage(file=r"./ChatBoxGUI/delete.png", height=100, width=100)
photo1 = PhotoImage(file=r"./ChatBoxGUI/heytest.png")
canvas1 = Canvas(root, width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=photo1, anchor="nw")

# top Navigation bar:
topFrame = Frame(root, bg=color["orange"])
canvas1.create_window(0, 0, anchor="nw", window=topFrame, width="1300", height="125")
# topFrame.pack(side="top", fill=X)

# Header label text:
homeLabel = Label(topFrame, text="Chat Box", font="Bahnschrift 95", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:

brandLabel = Label(root, text="", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)
b1 = Button(root, text='   New User', command=SignUpGUI.main, bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=signup, compound=LEFT, anchor="nw")
b2 = Button(root, text='   Login', command=LoginPageGUI.main, bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw")
b3 = Button(root, text='   Login Super User',  bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw")
b4 = Button(root, text='   Delete account', bg=color["nero"], fg=color["orange"],  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=delete, compound=LEFT, anchor="nw")
b5 = Button(root, text='   New Super User', command=SUserSignUpGUI.main, bg=color["nero"], fg=color["orange"],  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=signup, compound=LEFT, anchor="nw")
b6 = Button(root, text='   Find Friend By Id', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=find, compound=LEFT, anchor="nw")
canvas1.create_window(100, 370, anchor="nw", window=b1)
canvas1.create_window(100, 245, anchor="nw", window=b2)
canvas1.create_window(700, 245, anchor="nw", window=b3)
canvas1.create_window(100, 495, anchor="nw", window=b4)
canvas1.create_window(700, 370, anchor="nw", window=b5)
canvas1.create_window(700, 495, anchor="nw", window=b6)

# Navbar button:
navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 180
# option in the navbar:
options = ["Login", "Login Super User", "New User", "New Super User", "Find Friend By Id", "Delete account"]
# Navbar Option Buttons:
for i in range(6):
    Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=150, y=10)

root.mainloop()
