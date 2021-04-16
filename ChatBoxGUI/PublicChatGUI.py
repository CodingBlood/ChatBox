from tkinter import *
from ChatBox.KThread import *
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["Chatbox"]
mycol = mydb["PublicChatGroups"]
def main(Gname,username):
    def some():
        x = message.get()
        message.set("")
        tasks(x)
    def tasks(x):
        def task2():
            mydict = {"username": str(username), "Message": x}
            PChat = mydb["PublicChatGroups"]
            document = dict(PChat.find_one({'GName': Gname}))
            document['Chats'].append(mydict)
            PChat.update({'GName': Gname}, document)
            return 0
        task2()

    def task1():
        mycol = mydb["PublicChatGroups"]
        for change in mycol.watch(full_document='updateLookup'):
            t.insert(END, change["fullDocument"]["Chats"][-1]["username"] + " : " + change["fullDocument"]["Chats"][-1][
                "Message"] + "\n")
        return 0

    t1 = KThread(target=task1)
    t1.start()
    root1 = Toplevel()
    root1.geometry("1300x700")
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
    root1.title("Chat Box")
    photo1 = PhotoImage(file=r"./ChatBoxGUI/heytest.png")
    hi = 0
    h = Scrollbar(root1, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(root1)
    v.pack(side=RIGHT, fill=Y)
    t = Text(root1, width=15, height=37, wrap=NONE,xscrollcommand=h.set, yscrollcommand=v.set)
    t.bind("<Key>", lambda e: "break")
    for iterate in mycol.find():
        if Gname == iterate["GName"]:
            for chats in iterate["Chats"]:
                t.insert(END, chats["username"] + " : " + chats["Message"] + "\n")

    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    canvas1 = Canvas(root1, width=400, height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=photo1, anchor="nw")
    message = StringVar()
    b1 = Button(root1, text='SEND IT NOW --->>>',command=some, bg=color["nero"], fg=color["orange"], font=('Malgun Gothic Semilight', 10), width=20, height=3)
    l1 = Entry(root1, font=('Malgun Gothic Semilight', 25), bd=5, textvariable=message)
    canvas1.create_window(1125, 5, anchor="nw", window=b1)
    canvas1.create_window(5, 5, anchor="nw", window=l1, width=1100,height=60)
    root1.mainloop()


