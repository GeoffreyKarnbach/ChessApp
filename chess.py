from tkinter import*

lastRect=0
lastCoords=[]
modifiable=True

board=[["*" for lopp in range(8)] for loop in range(8)]
board[0]=["R1","k1","B1","Q1","K1","B1","k1","R1"]
board[1]=["P1" for loop in range(8)]
board[6]=["P2" for loop in range(8)]
board[7]=["R2","k2","B2","Q2","K2","B2","k2","R2"]

figures={"P1":"pawn1.png","k1":"knight1.png","B1":"bishop1.png","R1":"rooks1.png","Q1":"queen1.png","K1":"king1.png",\
        "P2":"pawn2.png","k2":"knight2.png","B2":"bishop2.png","R2":"rooks2.png","Q2":"queen2.png","K2":"king2.png"}

#figures["P1"] -> pawn1.png

'''
P = pawns
k = knights
B = bishops
R = rooks
Q = queen
K = king
'''

def array_to_fen(array):
    pass
    #"rnbnkqrb/pppppppp/8/8/8/8/PPPPPPPP/RNBNKQRB w KQkq - 0 1"

def get_moves(position):
    pass

def confirm_case(event):
    global lastCoords,modifiable
    if lastCoords!=[]:
        if modifiable:
            modifiable=False
        else:
            modifiable=True
    else:
        print("Select a case before confirming")


def click(event):
    global lastRect,lastCoords,modifiable
    if modifiable:
        if [(event.x//100)*100+2,(event.y//100)*100+2,(event.x//100)*100+98,(event.y//100)*100+98] == lastCoords:
            can.delete(lastRect)
            lastCoords=[]
        else:
            can.delete(lastRect)
            lastRect=can.create_rectangle((event.x//100)*100+2,(event.y//100)*100+2,(event.x//100)*100+98,(event.y//100)*100+98,outline="red",width=4)
            lastCoords=[(event.x//100)*100+2,(event.y//100)*100+2,(event.x//100)*100+98,(event.y//100)*100+98]
    else:
        print((lastCoords[0]-2)//100,(lastCoords[1]-2)//100)


def update_UI(board):
    for loop in range(8):
        for lopp in range(8):
            print(board[loop][lopp],end=" ")
        print()


def draw_board():
    colors=["black","white"]
    offset,current=0,0
    for loop in range(8):
        offset=(offset+1)%2
        current=offset
        for lopp in range(8):
            can.create_rectangle(lopp*100,loop*100,lopp*100+100,loop*100+100,fill=colors[current])
            current=(current+1)%2

fen=Tk()
fen.title("Chess")
fen.geometry("850x850")
fen.config(bg="grey")

can=Canvas(fen,width=797,height=797,bg="grey")
can.grid(column=0,row=0,padx=25,pady=25)

draw_board()
update_UI(board)

can.bind("<Button-1>",click)
fen.bind("<Return>",confirm_case)
fen.mainloop()