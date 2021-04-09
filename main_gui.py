
# def ULogin():
#     w.pack_forget()
#     userid = StringVar()
#     paswrd = StringVar()
#
#     def some():
#         name = userid.get()
#         pass_wrd = paswrd.get()
#         print("The name is : " + name)
#         print("The password is : " + pass_wrd)
#         userid.set("")
#         paswrd.set("")
#         # l.destroy()
#
#     chatbox_home.title("Login")
#     Label(l, text='UserName', width=50, height=2).grid(row=0, column=0)
#     Label(l, text='Password', width=50, height=2).grid(row=1, column=0)
#     e1 = Entry(l, bd=5, textvariable=userid)
#     e2 = Entry(l, bd=5, textvariable=paswrd, show='*')
#     login = Button(l, text='Login', command=some, width=100, height=2, bd=5)
#     go_back = Button(l, text='Go Back', command=main, width=100, height=2, bd=5)
#     e1.grid(row=0, column=1, padx=100, pady=4)
#     e2.grid(row=1, column=1, padx=100, pady=4)
#     login.grid(row=2, columnspan=2, padx=100, pady=4)
#     go_back.grid(row=3, columnspan=2, padx=100, pady=4)
#     l.pack()

# =========================REMEMBER IMPORTANT FOR CHATS==================================================================
# import tkinter as tk
#
# root = tk.Tk()
# root.geometry('600x400+80+40')
#
#
# class App:
#     def __init__(self, root):
#         self.entry_var = tk.StringVar()
#         self.entry = tk.Entry(root, textvariable=self.entry_var)
#         self.entry.bind('<Return>', self.show_output)
#         self.entry.pack()
#
#     def show_output(self, event):
#         print(self.entry_var.get())
#
#
# App(root)
# tk.mainloop()\
# =======================================================================================================================
#=======================================================================================================================
try:
    from tkinter import *
except:
    from tkinter import *


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Chat Box")
        self.geometry("1000x800")
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Hi there Welcome to Online Chatting Room", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Label(self, text="Only benefit of this is no one knows you are here :):)", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Label(self, text="Choose Wisely:---------------", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text='New User', fg='red', command=lambda: master.switch_frame(NUser), width=50, height=2).pack()
        Button(self, text='Login', fg='red', command=lambda: master.switch_frame(ULogin), width=50, height=2).pack()
        Button(self, text='Login Super User', fg='red', command=lambda: master.switch_frame(SULogin), width=50, height=2).pack()
        Button(self, text='Delete account', fg='red', command=lambda: master.switch_frame(DUser), width=50, height=2).pack()
        Button(self, text='New Super User', fg='red', command=lambda: master.switch_frame(NSUser), width=50, height=2).pack()
        Button(self, text='Find Friend By Id', fg='red', command=lambda: master.switch_frame(FFinder), width=50, height=2).pack()
class FFinder(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='blue')
        Label(self, text="Find My Friend", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
class NSUser(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='blue')
        Label(self, text="New Super User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
class DUser(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='blue')
        Label(self, text="Delete User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class SULogin(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='blue')
        Label(self, text="Super User Login", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
class ULogin(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='red')
        userid = StringVar()
        paswrd = StringVar()
        def some():
            name = userid.get()
            pass_wrd = paswrd.get()
            print("The name is : " + name)
            print("The password is : " + pass_wrd)
            userid.set("")
            paswrd.set("")
        Label(self, text="UserName", font=('Helvetica', 18, "bold")).pack()
        Label(self, text="Password", font=('Helvetica', 18, "bold")).pack()
        Entry(self, bd=5, textvariable=userid).pack()
        Entry(self, bd=5, textvariable=paswrd).pack()
        Button(self, text='Login', command=some, width=100, height=2, bd=5).pack()
        Button(self, text="Go back to start page", width=100, height=2, bd=5,
                  command=lambda: master.switch_frame(StartPage)).pack()

class NUser(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='red')
        Label(self, text="New User", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
