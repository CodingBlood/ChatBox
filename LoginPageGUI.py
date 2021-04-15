from tkinter import *
import pymongo
import time
myclient = pymongo.MongoClient(
    "mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["Chatbox"]
mycol = mydb["UserDetails"]
def main():
    def some():
        name = userid.get()
        pass_wrd = paswrd.get()
        myquery = {"UName": name}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            if x["UPassword"] == pass_wrd:
                print("Login Successful")
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                b1.destroy()
                sb1 = Button(root1, text='  Global Chat', bg=color["nero"], fg=color["orange"],
                            font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login,
                            compound=LEFT,
                            anchor="nw", command=some)
                # canvas1.create_text(100, 245, "Username", width=50, height=1, fg=color["orange"])
                sl1 = Button(root1, text='  Public Chat Groups', bg=color["nero"], fg=color["orange"],
                            font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login,
                            compound=LEFT,
                            anchor="nw", command=some)
                sl2 = Button(root1, text='  Private Chat Groups', bg=color["nero"], fg=color["orange"],
                            font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login,
                            compound=LEFT,
                            anchor="nw", command=some)
                sl3 = Button(root1, text='  New Public Group', bg=color["nero"], fg=color["orange"],
                            font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login,
                            compound=LEFT,
                            anchor="nw", command=some)
                sl4 = Button(root1, text='  New Private Group', bg=color["nero"], fg=color["orange"],
                            font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login,
                            compound=LEFT,
                            anchor="nw", command=some)
                canvas1.create_window(400, 495, anchor="nw", window=sb1)
                canvas1.create_window(700, 245, anchor="nw", window=sl1)
                canvas1.create_window(700, 370, anchor="nw", window=sl2)
                canvas1.create_window(100, 245, anchor="nw", window=sl3)
                canvas1.create_window(100, 370, anchor="nw", window=sl4)
            else:
                print("Login Failed")
        userid.set("")
        paswrd.set("")
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
            root1.config(bg=color["nero"])

            # created animated Navbar opening:
            for x in range(-300, 0):
                navRoot.place(x=x, y=0)
                topFrame.update()

            # turing button ON:
            btnState = True
    root1 = Toplevel()
    root1.geometry("1300x700")
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
    root1.title("Chat Box")
    # setting switch state:
    global btnState
    btnState = False
    # loading Navbar icon image:
    navIcon = PhotoImage(file="ham.png")
    closeIcon = PhotoImage(file="goback.png")
    login = PhotoImage(file=r"login.png", height=100, width=100)
    signup = PhotoImage(file=r"signup.png", height=100, width=105)
    find = PhotoImage(file=r"find.png", height=100, width=105)
    delete = PhotoImage(file=r"delete.png", height=100, width=100)
    photo1 = PhotoImage(file=r"heytest.png")
    canvas1 = Canvas(root1, width=400, height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=photo1, anchor="nw")

    # top Navigation bar:
    topFrame = Frame(root1, bg=color["orange"])
    canvas1.create_window(0, 0, anchor="nw", window=topFrame, width="1300", height="125")
    # topFrame.pack(side="top", fill=X)

    # Header label text:
    homeLabel = Label(topFrame, text="Chat Box", font="Bahnschrift 95", bg=color["orange"], fg="gray17", height=2,
                      padx=20)
    homeLabel.pack(side="right")





    # Main label text:
    userid = StringVar()
    paswrd = StringVar()
    brandLabel = Label(root1, text="", font="System 30", bg="gray17", fg="green")
    brandLabel.place(x=100, y=250)
    b1 = Button(root1, text='             Login', bg=color["nero"], fg=color["orange"],
                font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT,
                anchor="nw", command=some)
    # canvas1.create_text(100, 245, "Username", width=50, height=1, fg=color["orange"])
    l1 = Entry(root1,font=('Malgun Gothic Semilight', 25, "bold"),bd=5, textvariable=userid)
    l2 = Entry(root1,font=('Malgun Gothic Semilight', 25, "bold"),bd=5, textvariable=paswrd, show='*')
    l3 = Label(root1, text='UserName', width=15, height=1, font=('Malgun Gothic Semilight', 25, "bold"),bd=5)
    l4 = Label(root1, text='Password', width=15, height=1, font=('Malgun Gothic Semilight', 25, "bold"),bd=5)
    canvas1.create_window(300, 495, anchor="nw", window=b1)
    canvas1.create_window(700, 245, anchor="nw", window=l1)
    canvas1.create_window(700, 370, anchor="nw", window=l2)
    canvas1.create_window(100, 245, anchor="nw", window=l3)
    canvas1.create_window(100, 370, anchor="nw", window=l4)










    # Navbar button:
    navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20,
                       command=switch)
    navbarBtn.place(x=10, y=10)

    # setting Navbar frame:
    navRoot = Frame(root1, bg="gray17", height=1000, width=300)
    navRoot.place(x=-300, y=0)
    Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

    # set y-coordinate of Navbar widgets:
    y = 180
    # option in the navbar:
    options = ["Login", "Login Super User", "New User", "New Super User", "Find Friend By Id", "Delete account"]
    # Navbar Option Buttons:
    for i in range(6):
        Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
               activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
        y += 40

    # Navbar Close Button:
    closeBtn = Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0,
                      command=switch)
    closeBtn.place(x=150, y=10)

    root1.mainloop()