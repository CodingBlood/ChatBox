from tkinter import *
from ChatBox.KThread import *
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["Chatbox"]
mycol = mydb["UserDetails"]
def main(username):
    def some():
        x = message.get()
        message.set("")
        tasks(x)
    def tasks(x):
        def task1():
            mycol = mydb["GlobalChat"]
            for change in mycol.watch([{'$match': {'operationType': {'$in': ['insert']}}}]):
                # print(change)
                t.insert(END, change["fullDocument"]["UName"] + " : " + change["fullDocument"]["Message"] + "\n")
                # print("ended")
                break
            return 0
        def task2():
            GChat = mydb["GlobalChat"]
            mydict = {"UName": str(username), "Message": x}
            GChat.insert_one(mydict)
            return 0
        t1 = KThread(target=task1)
        # t1.setDaemon(True)
        t1.start()
        task2()
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
    mydb = myclient["Chatbox"]
    GChat = mydb["GlobalChat"]
    for iterate in GChat.find({}, {"_id": 0, "UName": 1, "Message": 1}):
        t.insert(END, iterate["UName"].capitalize() + " : " + iterate["Message"] + "\n")
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