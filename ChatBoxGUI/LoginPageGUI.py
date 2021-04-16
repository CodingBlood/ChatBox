from tkinter import *
import pymongo

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
                def Gchat():
                    import GlobalChatGUI
                    GlobalChatGUI.main(str(name))
                def PuGrp():
                    sb1.destroy()
                    sl1.destroy()
                    sl2.destroy()
                    sl3.destroy()
                    sl4.destroy()
                    def PuGrpChat(Grpname):
                        from ChatBoxGUI import PublicChatGUI
                        PublicChatGUI.main(Grpname, name)
                    #===========================================================================================================================
                    #===========================================================================================================================
                    #===========================================================================================================================
                    #================NOT WORKING================================================================================================
                    # def JoinGrp():
                    #
                    join = Button(root1, text='+', bg=color["nero"], fg=color["orange"],
                                 font=('Malgun Gothic Semilight', 15), width=2, bd=5, height=1, command=PuGrpChat)
                    canvas1.create_window(65, 190, anchor="nw", window=join)
                    #===========================================================================================================================
                    #===========================================================================================================================
                    #===========================================================================================================================
                    #===========================================================================================================================
                    pug_details = mydb["PublicChatGroups"]
                    b=245
                    turn=0
                    for iterate in pug_details.find():
                        for member in iterate["Members"]['username']:
                            if member['username'] == name:
                                Gname = iterate["GName"]
                                pgrp = Button(root1, text=iterate["GName"], bg=color["nero"], fg=color["orange"],
                                              font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5,image=login,
                                              compound=LEFT,
                                              anchor="nw", command=lambda Grpname=Gname: PuGrpChat(Grpname))
                                if turn >= 3:
                                    m = 700
                                else:
                                    m = 100
                                canvas1.create_window(m, b, anchor="nw", window=pgrp)
                                b += 120
                                turn += 1



                def PrGrp():
                    sb1.destroy()
                    sl1.destroy()
                    sl2.destroy()
                    sl3.destroy()
                    sl4.destroy()

                    def PrGrpChat(Grpname):
                        from ChatBoxGUI import PrivateChatGUI
                        PrivateChatGUI.main(Grpname, name)

                    # ===========================================================================================================================
                    # ===========================================================================================================================
                    # ===========================================================================================================================
                    # ================NOT WORKING================================================================================================
                    # def JoinGrp():
                    #
                    join = Button(root1, text='+', bg=color["nero"], fg=color["orange"],
                                  font=('Malgun Gothic Semilight', 15), width=2, bd=5, height=1, command=PrGrpChat)
                    canvas1.create_window(65, 190, anchor="nw", window=join)
                    # ===========================================================================================================================
                    # ===========================================================================================================================
                    # ===========================================================================================================================
                    # ===========================================================================================================================
                    pug_details = mydb["PrivateChatGroups"]
                    b = 245
                    turn = 0
                    for iterate in pug_details.find():
                        for member in iterate["Members"]['username']:
                            if member['username'] == name:
                                Gname = iterate["GName"]
                                pgrp = Button(root1, text=iterate["GName"], bg=color["nero"], fg=color["orange"],
                                              font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5,
                                              image=login,
                                              compound=LEFT,
                                              anchor="nw", command=lambda Grpname=Gname: PrGrpChat(Grpname))
                                if turn >= 3:
                                    m = 700
                                else:
                                    m = 100
                                canvas1.create_window(m, b, anchor="nw", window=pgrp)
                                b += 120
                                turn += 1

                def NPuGrp():
                    ngn = StringVar()
                    ngd = StringVar()
                    ngo = StringVar()
                    sb1.destroy()
                    sl1.destroy()
                    sl2.destroy()
                    sl3.destroy()
                    sl4.destroy()
                    def submit():
                        GName=ngn.get()
                        Desc=ngd.get()
                        # username=userid.get()
                        Origin=ngo.get()
                        myquery = {"Gname": GName}
                        mycol = mydb["PublicChatGroups"]
                        mydoc = mycol.find(myquery)
                        for x in mydoc:
                            res = not bool(x)
                            while not res:
                                print("Group with Same Name Already Exists")
                                NPuGrp()
                        mydict = {"GName": GName,
                                  "Desc": Desc,
                                  "Origin": Origin,
                                  "Owner": name,
                                  "Admins": {
                                      "username": [name]
                                  },
                                  "Members": {
                                      "username": [{
                                          "username": name,
                                      }
                                      ]
                                  },
                                  "Chats": [
                                      {
                                          "username": name,
                                          "Message": "Booyahh! Welcome To My Own Public Group"
                                      }
                                  ]
                                  }
                        temp = mycol.insert_one(mydict)
                        from ChatBoxGUI import PublicChatGUI
                        PublicChatGUI.main(GName, name)
                    submit = Button(root1,command=submit , text='      CreateGroup', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw")
                    name_of_group = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=ngn)
                    desc_of_group = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=ngd)
                    origin_of_group = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=ngo)
                    name_of_group1 = Label(root1, text='Group Name', width=18, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
                    desc_of_group1 = Label(root1, text='Description Of Group', width=18, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
                    origin_of_group1 = Label(root1, text='Origin Of Group', width=18, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
                    canvas1.create_window(300, 585, anchor="nw", window=submit)
                    canvas1.create_window(700, 210, anchor="nw", window=name_of_group)
                    canvas1.create_window(700, 335, anchor="nw", window=desc_of_group)
                    canvas1.create_window(100, 210, anchor="nw", window=name_of_group1)
                    canvas1.create_window(700, 460, anchor="nw", window=origin_of_group)
                    canvas1.create_window(100, 460, anchor="nw", window=origin_of_group1)
                    canvas1.create_window(100, 335, anchor="nw", window=desc_of_group1)

                def NPriGrp():
                    Ngn = StringVar()
                    Ngd = StringVar()
                    NgS = StringVar()
                    sb1.destroy()
                    sl1.destroy()
                    sl2.destroy()
                    sl3.destroy()
                    sl4.destroy()
                    def submit():
                        GName=Ngn.get()
                        Desc=Ngd.get()
                        Skey=NgS.get()
                        myquery = {"Gname": GName, "Owner": name}
                        mycol = mydb["PrivateChatGroups"]
                        mydoc = mycol.find(myquery)
                        for x in mydoc:
                            res = not bool(x)
                            while not res:
                                print("Similar Group Already Exists Already Exists")
                                NPriGrp()
                        mydict = {"GName": GName,
                                  "Desc": Desc,
                                  "SKey": Skey,
                                  "Owner": name,
                                  "Admins": {
                                      "username": [name]
                                  },
                                  "Members": {
                                      "username": [{
                                          "username": name,
                                      }
                                      ]
                                  },
                                  "Chats": [
                                      {
                                          "username": name,
                                          "Message": "Booyahh! Welcome To My Own Public Group"
                                      }
                                  ]
                                  }
                        temp = mycol.insert_one(mydict)
                        from ChatBoxGUI import PrivateChatGUI
                        PrivateChatGUI.main(GName, name)
                    submit = Button(root1,command=submit , text='      CreateGroup', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw")
                    Name_of_group = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=Ngn)
                    Desc_of_group = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=Ngd)
                    Skey_of_group = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=NgS, show='*')
                    Desc_of_group1 = Label(root1, text='Description Of Group', width=18, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
                    Name_of_group1 = Label(root1, text='Group Name', width=18, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
                    Skey_of_group1 = Label(root1, text='Security Key', width=18, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
                    canvas1.create_window(300, 585, anchor="nw", window=submit)
                    canvas1.create_window(700, 210, anchor="nw", window=Name_of_group)
                    canvas1.create_window(700, 335, anchor="nw", window=Desc_of_group)
                    canvas1.create_window(100, 210, anchor="nw", window=Name_of_group1)
                    canvas1.create_window(700, 460, anchor="nw", window=Skey_of_group)
                    canvas1.create_window(100, 460, anchor="nw", window=Skey_of_group1)
                    canvas1.create_window(100, 335, anchor="nw", window=Desc_of_group1)
                sb1 = Button(root1, text='  Global Chat', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT,anchor="nw", command=Gchat)
                sl1 = Button(root1, text='  Public Chat Groups', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw", command=PuGrp)
                sl2 = Button(root1, text='  Private Chat Groups', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw", command=PrGrp)
                sl3 = Button(root1, text='  New Public Group', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw", command=NPuGrp)
                sl4 = Button(root1, text='  New Private Group', bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 25, "bold"), width=500, height=100, bd=5, image=login, compound=LEFT, anchor="nw", command=NPriGrp)
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
    navIcon = PhotoImage(file=r"./ChatBoxGUI/ham.png")
    closeIcon = PhotoImage(file=r"./ChatBoxGUI/goback.png")
    login = PhotoImage(file=r"./ChatBoxGUI/login.png", height=100, width=100)
    photo1 = PhotoImage(file=r"./ChatBoxGUI/heytest.png")
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
    l1 = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=userid)
    l2 = Entry(root1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5, textvariable=paswrd, show='*')
    l3 = Label(root1, text='UserName', width=15, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
    l4 = Label(root1, text='Password', width=15, height=1, font=('Malgun Gothic Semilight', 25, "bold"), bd=5)
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