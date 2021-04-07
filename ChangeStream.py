from KThread import *
def main(username):
    import pymongo
    import os
    import threading
    import sys
    hi =0
    myclient = pymongo.MongoClient(
        "mongodb+srv://CodingBlood:kartik2002@cluster0.njrx7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    os.system('cls' if os.name == 'nt' else 'clear')
    mydb = myclient["Chatbox"]
    mycol = mydb["GlobalChat"]
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
    def task1():
        mycol = mydb["GlobalChat"]
        for change in mycol.watch([{'$match': {'operationType': {'$in': ['insert']}}}]):
            if hi == 1:
                print("nowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
                mycol = mydb["UserDetails"]
                break
            elif hi == 0:
                print(change["fullDocument"]["UName"] + " : " + change["fullDocument"]["Message"])
        return 0

    # if(ChangeStreamVaraible == 0):
    #     os.startfile(r"ChangeStream.exe")
    #     ChangeStreamVaraible += 1
    def task2():
        while True:
            x = str(input())
            if x != "$_":
                GChat = mydb["GlobalChat"]
                mydict = {"UName": username, "Message": x}
                temperory_variable = GChat.insert_one(mydict)
            else:
                # import main
                # main.KahesiModeOnn(username)
                # mycol = mydb["UserDetails"]
                hi = 1
                break
        return 0


    t1 = KThread(target=task1)
    # t2 = threading.Thread(target=task2, name='t2')
    t1.setDaemon(True)
    t1.start()
    task2()
    t1.kill()
    # t2.start()
    # t2.join()
    print(t1.is_alive())
