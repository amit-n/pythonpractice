import random

def DisplayBoard(board):
    print("+---------++---------++---------+")
    for ikey, ivalue in board.items():
        if ivalue == "":
            pval=str(ikey)
        else:
            pval=str(ivalue)
        if ikey%3 ==0:
            print("    ",pval,"    " )
            print("+---------++---------++---------+")
        else:
            print("    ",pval,"    ", end="")

def MakeListOfFreeFields(board):
    list_spots=[]
    for ikey, ivalue in board.items():
        if ivalue =="":
            list_spots.append(ikey)
    return list_spots

def EnterMove(board):
    DisplayBoard(board)
    print("List of open positions:",MakeListOfFreeFields(board))
    myinput = int(input("Your turn!! Enter number of square you wish to play: [1-9]"))
    if myinput not in MakeListOfFreeFields(board):
        print("Enter proper values.")
        print("Only 3 wrong attempts allowed")
    print("Value is" ,str(myinput))
    board[myinput]="O"
    DisplayBoard(board)

def VictoryFor(board, sign):
    if sign=='O':
        player="You"
    else:
        player="Computer"
    for key in range(1,9,3):
        if(boardDict[key]==boardDict[key+1] == boardDict[key+2] ==sign):
            print(player+" win!!")
            return "Game Over"
    #    print("Value of key is %s" %key)
    
    for key in range(1,4):
        if(boardDict[key]==boardDict[key+3] == boardDict[key+6] ==sign):
            print(player+" win!!")
            return "Game Over"
    #    print("Value of key is %s" %key)
 
    if(boardDict[1]==boardDict[5] == boardDict[9] ==sign):
        print(player +" win!!")
        return "Game Over"
    elif(boardDict[3]==boardDict[5] == boardDict[7] ==sign):
        print(player+ " win!")
        return "Game Over"
    return "Game On"


def DrawMove(board):
    if VictoryFor(boardDict,sign="O")==VictoryFor(boardDict,sign="X"):
        print ( "Game Drawn")

boardDict={}
for i in range(1,10):
    boardDict[i]=""

boardDict[5]="X"

while True:
    print("Moves Left:",len(MakeListOfFreeFields(boardDict)))
    if len(MakeListOfFreeFields(boardDict)) == 0:
#        boardDict[int(MakeListOfFreeFields[0])]="X"
        DrawMove(boardDict)
        break
    EnterMove(boardDict)
    if VictoryFor(boardDict,sign="O")=="Game Over":
        break
    print("Computers turn")
    boardDict[int(random.choice(MakeListOfFreeFields(boardDict)))]="X"
    if VictoryFor(boardDict,sign="X")=="Game Over":
        break
    DisplayBoard(boardDict)

DisplayBoard(boardDict)
