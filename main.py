#=======================================================================================================================
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
    GlobalChat(username)


def Write_Message(iterate):
    print(iterate["UName"].capitalize() + " : " + iterate["Message"])


def GlobalChat(username):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("NOTE:- ENTER YOUR MESSAGE AFTER >> AND ENTER $_ TO EXIT... ")
    print(
        '''
        =============================================================================================================================
        |   GGGGGGGGGGGGG                                                       CCCCCCCCCCCCCC                                      |
        |   GGGGGGGGGGGGG                                                       CCCCCCCCCCCCCC                                      |
        |   GGG                                                                 CCC                                                 |
        |   GGG                                                                 CCC                                                 |
        |   GGG     GGGGG   LL        OOOOOOO   BBBBBB  AAAAAAAA    LL          CCC             HH    HH    AAAAAAA    TTTTTTTT     |
        |   GGG     GGGGG   LL        O     O   B    B  A      A    LL          CCC             HH    HH    AA   AA       TT        |
        |   GGG        GG   LL        O     O   BBBBBB  AAAAAAAA    LL          CCC             HHHHHHHH    AAAAAAA       TT        |
        |   GGGGGGGGGGGGG   LL        O     O   B    B  A      A    LL          CCCCCCCCCCCCCC  HH    HH    AA   AA       TT        |
        |   GGGGGGGGGGGGG   LLLLLLLL  OOOOOOO   BBBBBB  A      A    LLLLLLLL    CCCCCCCCCCCCCC  HH    HH    AA   AA       TT        |
        =============================================================================================================================
        ''')
    x = ""

    mydb = myclient["Chatbox"]
    GChat = mydb["GlobalChat"]
    for iterate in GChat.find({}, {"_id": 0, "UName": 1, "Message": 1}):
        Write_Message(iterate)
    while True :
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
        GlobalChat(username)
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
    pass

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hi there Welcome to Online Chating Room")
    print("Only benefit of this is no one knows you are here :):)")
    print("You have only 4 options, 3 of them are as follows and 4th is fuckoff")
    print("1) New User")
    print("2) Login")
    print("3) Delete account")
    print("Your Choice 1 or 2 or 3 or fuckoff : ")
    x = int(input())
    if x == 1:
        NUser()
    elif x == 2:
        ULogin()
    elif x == 3:
        DUser()
    else:
        print("Sorry Wrong Choice, I guess you really like fucking around")
        main()
main()