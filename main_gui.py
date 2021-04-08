import tkinter.constants
from tkinter import *
def NUser():
    New_User = Tk()
    New_User.title("New User")
    some = Button(New_User, text='Go Back', command=New_User.destroy, width=50, height=2)
    some.pack()
    New_User.mainloop()
def ULogin():
    New_User = Tk()
    New_User.title("Login")
    some = Button(New_User, text='Go Back', command=New_User.destroy, width=50, height=2)
    some.pack()
    New_User.mainloop()
def SULogin():
    New_User = Tk()
    New_User.title("Super User Login")
    some = Button(New_User, text='Go Back', command=New_User.destroy, width=50, height=2)
    some.pack()
    New_User.mainloop()
def DUser():
    New_User = Tk()
    New_User.title("Delete User")
    some = Button(New_User, text='Go Back', command=New_User.destroy, width=50, height=2)
    some.pack()
    New_User.mainloop()
def NSUser():
    New_User = Tk()
    New_User.title("New Super User")
    some = Button(New_User, text='Go Back', command=New_User.destroy, width=50, height=2)
    some.pack()
    New_User.mainloop()
def FFinder():
    New_User = Tk()
    New_User.title("Find My Friend")
    some = Button(New_User, text='Go Back', command=New_User.destroy, width=50, height=2)
    some.pack()
    New_User.mainloop()

def main():
    chatbox_home = Tk()
    chatbox_home.title("Chat Box")
    w = Frame(chatbox_home)
    hello = Label(chatbox_home, text='Hi there Welcome to Online Chatting Room', width=50, height=2)
    hello.pack()
    some = Label(chatbox_home, text='Only benefit of this is no one knows you are here :):)', width=50, height=2)
    some.pack()
    choose = Label(chatbox_home, text='Choose Wisely:---------------', width=50, height=2)
    choose.pack()
    NUserButton = Button(chatbox_home, text='New User',fg='red', command=NUser, width=50, height=2)
    NUserButton.pack(side=TOP)
    Login = Button(chatbox_home, text='Login', fg='red', command=ULogin, width=50, height=2)
    Login.pack(side=TOP)
    User = Button(chatbox_home, text='Login Super User', fg='red', command=SULogin, width=50, height=2)
    User.pack(side=TOP)
    DelAcc = Button(chatbox_home, text='Delete account', fg='red', command=DUser, width=50, height=2)
    DelAcc.pack(side=TOP)
    SUser = Button(chatbox_home, text='New Super User', fg='red', command=NSUser, width=50, height=2)
    SUser.pack(side=TOP)
    findfriend = Button(chatbox_home, text='Find Friend By Id', fg='red', command=FFinder, width=50, height=2)
    findfriend.pack(side=TOP)
    w.pack()
    chatbox_home.mainloop()
# main()
while True:
    try:
        main()
    except:
        main()
    finally:
        main()