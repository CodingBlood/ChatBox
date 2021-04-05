# =======================================================================================================================
#  Enter "auto-py-to-exe" this in terminal to generate the exe file
#  Note:-   "pip install auto-py-to-exe" this is already done in this virtual environment
# ======================================================================================================================
import pymongo
import os
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


def GlobalChat(username, ChangeStreamVaraible):
    os.system('cls' if os.name == 'nt' else 'clear')
    if(ChangeStreamVaraible == 0):
        os.startfile(r"ChangeStream.exe")
        ChangeStreamVaraible += 1
    print("NOTE:- ENTER YOUR MESSAGE AFTER >> AND ENTER $_ TO EXIT... ")
    while True:
        print(">>")
        x = str(input())
        if x != "$_":
            NewGlobalMessage(username, x)
        else:
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
    print("Enter Security Key Now!! >> ")
    security_key = str(input())
    if security_key != "9211BadAss!)@(#*$&%^BadAss9211":
        main()
    mycol = mydb["SuperUserDetails"]
    print("No personal data required we don't wanna know who and why you are")
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

def NPuGrp():
    main()


def NPriGrp():
    main()

def FFinder():
    mycol = mydb["UserDetails"]
    print("Username:")
    username = input()
    myquery = {"UName": username}
    mydoc = mycol.find(myquery)
    if len(mydoc[0]) == 0:
        print("No Such User Found")
    else:
        print("Congratulations We Found your User!!!!")
        print(mydoc[0]["UName"])


def SuperKahesiModeOnn(username):
    print("Welcome Master. What can I show to please you...?")
    print("1) User Details")
    print("2) Super User Details")
    print("3) Go Back")
    x = int(input())
    if x == 1:
        Udetails = mydb["UserDetails"]
        for iterate in Udetails.find({}, {"_id": 0, "UName": 1, "Message": 1}):
            print(iterate["UName"].capitalize())
            SuperKahesiModeOnn(username)
    elif x ==2:
        SUDetails = mydb["SuperUserDetails"]
        for iterate in SUDetails.find({}, {"_id": 0, "UName": 1, "Message": 1}):
            print(iterate["UName"].capitalize())
            SuperKahesiModeOnn(username)
    else:
        main()


def SULogin():
    mycol = mydb["SuperUserDetails"]
    print("Username:")
    username = input()
    print("Password")
    password = input()
    myquery = {"UName": username}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if x["UPassword"] == password:
            print("LOGIN SUCCESSFUL!!!")
            SuperKahesiModeOnn(username)
        else:
            print("LoginFailed")
            print()
            print()
            main()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hi there Welcome to Online Chatting Room")
    print("Only benefit of this is no one knows you are here :):)")
    print("Choose Wisely:---------------")
    print("1) New User")
    print("2) Login")
    print("3) Login Super User")
    print("4) Delete account")
    print("5) New Super User")
    print("6) New Public Group")
    print("7) New Private Group")
    print("8) Find Friend By Id")
    print("My Dear Friend Enter Your Choice Here >> ")
    x = int(input())
    if x == 1:
        NUser()
    elif x == 2:
        ULogin()
    elif x == 3:
        SULogin()
    elif x == 4:
        DUser()
    elif x == 5:
        NSUser()
    elif x == 6:
        NPuGrp()
    elif x == 7:
        NPriGrp()
    elif x == 8:
        FFinder()
    else:
        print("Sorry Wrong Choice, I guess you really like fucking around")
        main()


main()
