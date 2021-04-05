# =======================================================================================================================
#  Enter "auto-py-to-exe" this in terminal to generate the exe file
#  Note:-   "pip install auto-py-to-exe" this is already done in this virtual environment
# ======================================================================================================================
import pymongo
import os
from subprocess import *
os.system('cls' if os.name == 'nt' else 'clear')
myclient = pymongo.MongoClient(
    "mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["Chatbox"]
mycol = mydb["UserDetails"]


# ======================================================================================================================
# mydict = { "UName": "KahesiBot4", "UPassword": "GrippenBot4" }
# x = mycol.insert_one(mydict)
# for x in mycol.find():
#   print(x["UName"])
# ======================================================================================================================
# for x in mycol.find({},{ "_id": 0, "UName": 1, "UPassword": 1 }):          #1--> mean print   2--->mean not print   (Note this only hides _id)
#   print(x)
# ======================================================================================================================
# myquery = { "UName": "CodingBlood" }              #to find all UName whos values is CodingBlood
# myquery = { "address": { "$gt": "S" } }           #to find all address which start with S or are greater than S
# myquery = { "address": { "$regex": "^S" } }       #to find all address which start with S
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)
# ======================================================================================================================


def NUser():
    print("No personal data required we dont wanna know who and why you are")
    print("UserName Or '$-' to go back")
    username = input()
    if username == '$-':
        main()
    myquery = {"UName": username}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        res = not bool(x)
        while not res:
            print("Username Already Exists")
            NUser()
    print("Password")
    password = input()
    mydict = {"UName": username, "UPassword": password}
    x = mycol.insert_one(mydict)
    print("New User Has Been Created Successfully")
    main()


def NewGlobalMessage(username, x):
    mydb = myclient["Chatbox"]
    GChat = mydb["GlobalChat"]
    mydict = {"UName": username, "Message": x}
    temperory_variable = GChat.insert_one(mydict)
    GlobalChat(username, 1)


def Write_Message(iterate):
    print(iterate["UName"].capitalize() + " : " + iterate["Message"])


def DeOrActivate(what):
    # changeStream = 1
    if what == 1:
        changeStream = os.startfile(r"ChangeStream.exe")
        return changeStream
    # elif what == 0:
        # os.close(changeStream)

def GlobalChat(username, ChangeStreamVaraible):
    os.system('cls' if os.name == 'nt' else 'clear')
    if(ChangeStreamVaraible == 0):
        DeOrActivate(1)
        ChangeStreamVaraible += 1
    print("NOTE:- ENTER YOUR MESSAGE AFTER >> AND ENTER $_ TO EXIT... ")
    while True:
        print(">>")
        x = str(input())
        if x != "$_":
            NewGlobalMessage(username, x)
        else:
            # DeOrActivate(0)
            KahesiModeOnn(username)


def KahesiModeOnn(username):
    print("We At ChatBox Welcome you to our Application")
    print("We are Continuously working on adding More and more features but till then you can enjoy our Global chat")
    print("Enter 1 to gain access to Global Chat")
    print("Enter 2 to gain access to LOGOUT")
    x = int(input())
    if x == 1:
        GlobalChat(username, 0)
    elif x == 2:
        main()


def ULogin():
    print("Username:")
    username = input()
    print("Password")
    password = input()
    myquery = {"UName": username}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if x["UPassword"] == password:
            print("LOGIN SUCCESSFUL!!!")
            KahesiModeOnn(username)
        else:
            print("LoginFailed")
            print()
            print()
            main()


def DUser():
    main()


def NSUser():
    main()

def NPuGrp():
    main()


def NPriGrp():
    main()

def FFinder():
    main()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hi there Welcome to Online Chatting Room")
    print("Only benefit of this is no one knows you are here :):)")
    print("Choose Wisely:---------------")
    print("1) New User")
    print("2) Login")
    print("3) Delete account")
    print("4) New Super User")
    print("5) New Public Group")
    print("6) New Private Group")
    print("7) Find Friend By Id")
    print("My Dear Friend Enter Your Choice Here >> ")
    x = int(input())
    if x == 1:
        NUser()
    elif x == 2:
        ULogin()
    elif x == 3:
        DUser()
    elif x == 4:
        NSUser()
    elif x == 5:
        NPuGrp()
    elif x == 6:
        NPriGrp()
    elif x == 7:
        FFinder()
    else:
        print("Sorry Wrong Choice, I guess you really like fucking around")
        main()


main()
