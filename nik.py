def printboard(x,y):
    zero = "x" if x[0] else ("o" if y[0] else 0)
    one = "x" if x[1] else ("o" if y[1] else 1)
    two = "x" if x[2] else ("o" if y[2] else 2)
    three = "x" if x[3] else ("o" if y[3] else 3)
    four= "x" if x[4] else ("o" if y[4] else 4)
    five = "x" if x[5] else ("o" if y[5] else 5)
    six = "x" if x[6] else ("o" if y[6] else 6)
    seven = "x" if x[7] else ("o" if y[7] else 7)
    eight= "x" if x[8] else ("o" if y[8] else 8)
    print(f"{zero} | {one} | {two}  ")
    print(f"- | - | -")
    print(f"{three} | {four } | {five}")
    print(f"- | - | -")
    print(f"{six} | {seven} | {eight}")
def checkwin(x,y):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        sum=x[i[0]]+x[i[1]]+x[i[2]]
        sum2=y[i[0]]+y[i[1]]+y[i[2]]
        if(sum==3):
            printboard(x, y)
            print("x won")

            return 1
        elif(sum2==3):
            printboard(x,y)
            print("y won")
            return 0
    return -1

if __name__ == "__main__":
    x=[0,0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0,0]
    print("welcome to tic tac toe")
    turn=1
    while True:
        printboard(x,y)
        if(turn==1):
            print("X chance")
            val=int(input("enter ur choice"))
            x[val]=1
        else:
            print("Y chance")
            val=int(input("enter ur choice"))
            y[val]=1
        cwin=checkwin(x,y)
        if(cwin!=-1):
            break
        turn =1-turn


