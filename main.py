# =======================================================================================================================
#  Enter "auto-py-to-exe" this in terminal to generate the exe file
#  Note:-   "pip install auto-py-to-exe" this is already done in this virtual environment
# ======================================================================================================================
import pymongo
import os
import subprocess
import threading
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
    import GlobalChat
    GlobalChat.main(username)
    # import os
    # os.system("exec ChangeStream")
    # subprocess.call(['python', 'GlobalChat.py'])
    KahesiModeOnn(username)
def PuGrp(username):
    print("Heyaaa!!!")
    print("Public Chat Groups You have Joined Are As Follows")
    pug_details = mydb["PublicChatGroups"]
    for iterate in pug_details.find():
        print(iterate["GName"] + " : " + iterate["Desc"])
        print(iterate["Owner"] + " --- Origin : " + iterate["Origin"])
        admins = ""
        for i in iterate["Admins"]["username"]:
            admins += i
        print("Our Esteemed Admins >> " + admins)
        members = ""
        for i in iterate["Members"]["username"]:
            members += i
        print("Our Esteemed Members >> " + members)
        print()
        print()
    print("Enter 1 To Join a new Group")
    print("Enter Group Name To Chat")
    x = input()
    import PublicChats
    PublicChats.main(username, x)

    KahesiModeOnn(username)
def PriGrp(username):
    print("Heyaaa!!!")
    print("Private Chat Groups You have Joined Are As Follows")
    prg_details = mydb["PrivateChatGroups"]
    for iterate in prg_details.find():
        print(iterate["GName"] + " : " + iterate["Desc"])
        print(iterate["Owner"])
        admins = ""
        for i in iterate["Admins"]["username"]:
            admins += i
        print("Our Esteemed Admins >> " + admins)
        members = ""
        for i in iterate["Members"]["username"]:
            members += i
        print("Our Esteemed Members >> " + members)
        print()
        print()
    print("Enter 1 To Join a new Group")
    print("Enter Group Name To Chat")
    x = input()
    # for iterate in prg_details.find():
    #     if iterate["SKey"]:
    #
    # if x ==
    import PrivateChats
    PrivateChats.main(username, x)
    KahesiModeOnn(username)
def KahesiModeOnn(username):
    print("We At ChatBox Welcome you to our Application")
    print("We are Continuously working on adding More and more features but till then you can enjoy our Global chat")
    print("Enter 1 to gain access to Global Chat")
    print("Enter 2 to gain access to LOGOUT")
    print("Enter 3 to go to your Public Chat Groups")
    print("Enter 4 to go to your Public Chat Groups")
    print("Enter 5 to create New Public Group")
    print("Enter 6 to create New Private Group")
    x = int(input())
    if x == 1:
        GlobalChat(username, 0)
    elif x == 2:
        main()
    elif x == 3:
        PuGrp(username)
    elif x == 4:
        PriGrp(username)
    elif x == 5:
        NPuGrp(username)
    elif x == 6:
        NPriGrp(username)
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
def NPuGrp(username):
    print("Create A New Public Group Over Here")
    print("Enter Name Of Your Group '$-' to go back")
    GName = str(input())
    if GName == '$-':
        main()
    myquery = {"Gname": GName}
    mycol = mydb["PublicChatGroups"]
    mydoc = mycol.find(myquery)
    for x in mydoc:
        res = not bool(x)
        while not res:
            print("Group with Same Name Already Exists")
            NPuGrp(username)
    print("Enter Description Of Your Group")
    Desc = str(input())
    print("Enter Place Of Group's Origin")
    Origin = str(input())
    mydict = {"GName": GName,
              "Desc": Desc,
              "Origin": Origin,
              "Owner": username,
              "Admins": {
                  "username": [username]
              },
              "Members": {
                  "username": [username]
              },
              "Chats": [
                  {
                      "username": username,
                      "Message": "Booyahh! Welcome To My Own Public Group"
                  }
              ]
              }
    x = mycol.insert_one(mydict)
    print("New Group Has Been Created Successfully")
    main()
def NPriGrp(username):
    print("Create A New Private Group Over Here")
    print("Enter Name Of Your Group '$-' to go back")
    GName = str(input())
    myquery = {"Gname": GName, "Owner": username}
    if GName == '$-':
        main()
    mycol = mydb["PrivateChatGroups"]
    mydoc = mycol.find(myquery)
    for x in mydoc:
        res = not bool(x)
        while not res:
            print("Similar Group Already Exists Already Exists")
            NPriGrp(username)
    print("Enter Description Of Your Group")
    Desc = str(input())
    print("Enter Your Groups Security Key")
    Skey = str(input())
    mydict = {"GName": GName,
              "Desc": Desc,
              "SKey": Skey,
              "Owner": username,
              "Admins": {
                  "username": [username]
              },
              "Members": {
                  "username": [username]
              },
              "Chats": [
                  {
                      "username": username,
                      "Message": "Booyahh! Welcome To My Own Public Group"
                  }
              ]
              }
    x = mycol.insert_one(mydict)
    print("New Group Has Been Created Successfully")
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
    print("3) Public Groups Details")
    print("4) Private Groups Details")
    print("5) Go Back")
    x = int(input())
    if x == 1:
        u_details = mydb["UserDetails"]
        for iterate in u_details.find({}, {"_id": 0, "UName": 1, "UPassword": 1}):
            print(iterate["UName"].capitalize())
        SuperKahesiModeOnn(username)
    elif x == 2:
        su_details = mydb["SuperUserDetails"]
        for iterate in su_details.find({}, {"_id": 0, "UName": 1, "UPassword": 1}):
            print(iterate["UName"].capitalize())
        SuperKahesiModeOnn(username)
    elif x == 3:
        pug_details = mydb["PublicChatGroups"]
        for iterate in pug_details.find():
            print(iterate["GName"] + " : " + iterate["Desc"])
            print(iterate["Owner"] + " --- Origin : " + iterate["Origin"])
            admins = ""
            for i in iterate["Admins"]["username"]:
                admins += i
            print("Our Esteemed Admins >> " + admins)
            members = ""
            for i in iterate["Members"]["username"]:
                members += i
            print("Our Esteemed Members >> " + members)
            print()
            print()
        SuperKahesiModeOnn(username)
    elif x == 4:
        prg_details = mydb["PrivateChatGroups"]
        for iterate in prg_details.find():
            print(iterate["GName"] + " : " + iterate["Desc"])
            print(iterate["Owner"] )
            admins = ""
            for i in iterate["Admins"]["username"]:
                admins += i
            print("Our Esteemed Admins >> " + admins)
            members = ""
            for i in iterate["Members"]["username"]:
                members += i
            print("Our Esteemed Members >> " + members)
            print()
            print()
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
    print("6) Find Friend By Id")
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
        FFinder()
    else:
        print("Sorry Wrong Choice, I guess you really like fucking around")
        main()
main()