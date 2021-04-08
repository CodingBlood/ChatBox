from KThread import *


def main(username, x):
    import pymongo
    import os
    myclient = pymongo.MongoClient(
        "mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    os.system('cls' if os.name == 'nt' else 'clear')
    mydb = myclient["Chatbox"]
    mycol = mydb["PrivateChatGroups"]
    for iterate in mycol.find():
        if iterate["GName"] == x:
            print(iterate["GName"] + " : " + iterate["Desc"])
            print(iterate["Owner"])
            admins = ""
            for i in iterate["Admins"]["username"]:
                admins += i
            print("Our Esteemed Admins >> " + admins)
            members = ""
            for i in iterate["Members"]["username"]:
                members += i['username']
            print("Our Esteemed Members >> " + members)
            print()
            print()
            for chats in iterate["Chats"]:
                print(chats["username"] + " : " + chats["Message"])

    def task1():
        mydb = myclient["Chatbox"]
        mycol = mydb["PrivateChatGroups"]

        for change in mycol.watch(full_document='updateLookup'):
            print(change["fullDocument"]["Chats"][-1]["username"] + " : " + change["fullDocument"]["Chats"][-1]["Message"])

    def task2():
        while True:
            p = str(input())
            if p != "$_":
                mydict = {"username": username, "Message": p}
                PChat = mydb["PrivateChatGroups"]
                document = dict(PChat.find_one({'GName': x}))
                document['Chats'].append(mydict)
                PChat.update({'GName': x}, document)
            else:
                break
        return 0

    t1 = KThread(target=task1)
    t1.start()
    task2()
    t1.kill()
