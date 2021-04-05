import pymongo
myclient = pymongo.MongoClient(
    "mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["Chatbox"]
mycol = mydb["GlobalChat"]
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
    print(iterate["UName"].capitalize() + " : " + iterate["Message"])
for change in mycol.watch([{'$match': {'operationType': {'$in': ['insert']}}}]):
    print(change["fullDocument"]["UName"] + " : " + change["fullDocument"]["Message"])
