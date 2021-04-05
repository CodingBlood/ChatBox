# ======================================================================================================================
import pymongo

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
print("Hi there Welcome to Online Chating Room")
print("Only benefit of this is no one knows you are here :):)")
print("You have only 4 options, 3 of them are as follows and 4th is fuckoff")
print("1) New User")
print("2) Login")
print("3) Delete account")
print("Your Choice 1 or 2 or 3 or fuckoff : ")
x = int(input())


def NUser():
    print("No personal data required we dont wanna know who and why you are")
    print("UserName")
    username = input()
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
    print("New Used Has Been Created Successfully")


def NewGlobalMessage(username, x):
    pass


def GlobalChat(username):
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
    while x != "$_":
        print(">>")
        x = str(input())
        NewGlobalMessage(username, x)
    KahesiModeOnn(username)


def KahesiModeOnn(username):
    print("We At ChatBox Welcome you to our Application")
    print("We are Continuously working on adding More and more features but till then you can enjoy our Global chat")
    print("Enter 1 to gain access to Global Chat")
    x = int(input())
    if x == 1:
        GlobalChat(username)

def ULogin():
    print("UserName")
    username = input()
    print("Password")
    password = input()
    myquery = {"UName": "CodingBlood"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        if x["UPassword"] == password:
            print("LOGIN SUCCESSFUL!!!")
            KahesiModeOnn(username)


def DUser():
    pass


if x == 1:
    NUser()
elif x == 2:
    ULogin()
elif x == 3:
    DUser()
else:
    print("Sorry Wrong Choice, I guess you really like fucking around")
