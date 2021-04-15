# import pymongo
# import time
# myclient = pymongo.MongoClient(
#     "mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# mydb = myclient["Chatbox"]
# mycol = mydb["UserDetails"]
# # =========================REMEMBER IMPORTANT FOR CHATS==================================================================
# # import tkinter as tk
# #
# # root = tk.Tk()
# # root.geometry('600x400+80+40')
# #
# #
# # class App:
# #     def __init__(self, root):
# #         self.entry_var = tk.StringVar()
# #         self.entry = tk.Entry(root, textvariable=self.entry_var)
# #         self.entry.bind('<Return>', self.show_output)
# #         self.entry.pack()
# #
# #     def show_output(self, event):
# #         print(self.entry_var.get())
# #
# #
# # App(root)
# # tk.mainloop()\
# # =======================================================================================================================
# #=======================================================================================================================
#
# try:
#     from tkinter import *
# except:
#     from tkinter import *
#
# class SampleApp(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         self.title("Chat Box")
#         self.geometry("1000x800")
#         self._frame = None
#         self.switch_frame(StartPage)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()
#
# class StartPage(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Label(self, text="Hi there Welcome to Online Chatting Room", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Label(self, text="Only benefit of this is no one knows you are here :):)", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Label(self, text="Choose Wisely:---------------", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text='New User', fg='red', command=lambda: master.switch_frame(NUser), width=50, height=2).pack()
#         Button(self, text='Login', fg='red', command=lambda: master.switch_frame(ULogin), width=50, height=2).pack()
#         Button(self, text='Login Super User', fg='red', command=lambda: master.switch_frame(SULogin), width=50, height=2).pack()
#         Button(self, text='Delete account', fg='red', command=lambda: master.switch_frame(DUser), width=50, height=2).pack()
#         Button(self, text='New Super User', fg='red', command=lambda: master.switch_frame(NSUser), width=50, height=2).pack()
#         Button(self, text='Find Friend By Id', fg='red', command=lambda: master.switch_frame(FFinder), width=50, height=2).pack()
# class FFinder(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Frame.configure(self, bg='blue')
#         Label(self, text="Find My Friend", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
# class NSUser(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Frame.configure(self, bg='blue')
#         Label(self, text="New Super User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
# class DUser(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Frame.configure(self, bg='blue')
#         Label(self, text="Delete User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
# class SULogin(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Frame.configure(self, bg='blue')
#         Label(self, text="Super User Login", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
# class KahesiModeOnn(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Frame.configure(self, bg='blue')
#         Label(self, text="Heya", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
# class ULogin(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         # Frame.configure(self, bg='red')
#         userid = StringVar()
#         paswrd = StringVar()
#         def some():
#             name = userid.get()
#             pass_wrd = paswrd.get()
#             myquery = {"UName": name}
#             mydoc = mycol.find(myquery)
#             for x in mydoc:
#                 if x["UPassword"] == pass_wrd:
#                     Button(self, text="Login Successful Click To Proceed", width=100, height=2, bd=5,
#                            command=lambda: master.switch_frame(KahesiModeOnn)).pack()
#                 else:
#                     Button(self, text="Login Failed Retry...", width=100, height=2, bd=5,
#                            command=lambda: master.switch_frame(ULogin)).pack()
#             userid.set("")
#             paswrd.set("")
#         Label(self, text="UserName", font=('Helvetica', 18, "bold")).pack()
#         Entry(self, bd=5, textvariable=userid).pack()
#         Label(self, text="Password", font=('Helvetica', 18, "bold")).pack()
#         Entry(self, bd=5, textvariable=paswrd).pack()
#         Button(self, text='Login', command=some, width=100, height=2, bd=5).pack()
#         Button(self, text="Go back to start page", width=100, height=2, bd=5,
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
# class NUser(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Frame.configure(self, bg='red')
#         Label(self, text="New User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()














# root.geometry("400x600+850+50")





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
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


# window in mainloop:
# root.mainloop()







from tkinter import PhotoImage
from tkinter import *
root =Tk()
root.geometry("1300x700")
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
root.title("Chat Box")
# setting switch state:
btnState = False
# loading Navbar icon image:
navIcon = PhotoImage(file="ham.png")
closeIcon = PhotoImage(file="goback.png")
login = PhotoImage(file=r"login.png", height=100, width=100)
signup = PhotoImage(file=r"signup.png", height=100, width=105)
find = PhotoImage(file=r"find.png", height=100, width=105)
delete = PhotoImage(file=r"delete.png", height=100, width=100)
photo1 = PhotoImage(file=r"heytest.png")
canvas1 = Canvas(root, width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=photo1,anchor="nw")







# top Navigation bar:
topFrame = Frame(root, bg=color["orange"])
canvas1.create_window(0,0, anchor="nw", window=topFrame, width="1300", height="125")
# topFrame.pack(side="top", fill=X)

# Header label text:
homeLabel = Label(topFrame, text="Chat Box", font="Bahnschrift 65", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = Label(root, text="", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)
b1=Button(root, text='   New User', font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=signup, compound = LEFT, anchor="nw")
b2=Button(root, text='   Login',  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound = LEFT, anchor="nw")
b3=Button(root, text='   Login Super User',  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound = LEFT, anchor="nw")
b4=Button(root, text='   Delete account',  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=delete, compound = LEFT, anchor="nw")
b5=Button(root, text='   New Super User',  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=signup, compound = LEFT, anchor="nw")
b6=Button(root, text='   Find Friend By Id',  font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=find, compound = LEFT, anchor="nw")
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
options = ["Profile", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:
for i in range(5):
    Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=150, y=10)

root.mainloop()