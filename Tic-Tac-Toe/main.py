lst=[["","",""],
     ["","",""],
     ["","",""]]


def Display(lst):
    r=0
    c=0
    for i in range(0,3):
        if(i>0):
            print("━━ ━━━ ━━")


        for j in range(0,3):

            if(j>0):
                print(" | ",end="")
            
            if(lst[i][j]==""):
                print(" ",end="")
            elif(lst[i][j]=='x'):
                print("X",end="")
            else:
                print("O",end="")
        print("")

def Checker(lst):
    if(lst[0][0]==lst[0][1]==lst[0][2]!=""):
        return lst[0][0]
    
    if(lst[1][0]==lst[1][1]==lst[1][2]!=""):
        return lst[1][0]
    
    if(lst[2][0]==lst[2][1]==lst[2][2]!=""):
        return lst[2][0]

    if(lst[0][0]==lst[1][0]==lst[2][0]!=""):
        return lst[0][0]
    
    if(lst[0][1]==lst[1][1]==lst[2][1]!=""):
        return lst[0][1]
    
    if(lst[0][2]==lst[1][2]==lst[2][2]!=""):
        return lst[0][2]
    
    if(lst[0][0]==lst[1][1]==lst[2][2]!=""):
        return lst[0][0]
    
    if(lst[2][0]==lst[1][1]==lst[0][2]!=""):
        return lst[2][0]
    
    for i in range(0,3):
        for j in range (0,3):
            if(lst[i][j]==""):
                return ""
    
    return "d"


def O_Best_Move(lst,depth,c):
    if(Checker(lst)=='x'):
        depth[0]=c
        return 1
    if(Checker(lst)=='d'):
        return 0
    score=1
    for i in range (0,3):
        for j in range(0,3):
            if(lst[i][j]==""):
                lst[i][j]='o'
                c+=1
                temp=X_Best_Move(lst,depth,c)
                c-=1
                score=min(temp,score)
                lst[i][j]=""
    return score 

def X_Best_Move(lst,depth,c):
    if(Checker(lst)=='o'):
        return -1
    if(Checker(lst)=='d'):
        return 0
    score=-1
    for i in range (0,3):
        for j in range(0,3):
            if lst[i][j]=="":
                lst[i][j]='x'
                c+=1
                temp=O_Best_Move(lst,depth,c)
                c-=1
                score=max(score,temp)
                lst[i][j]=""
    return score

while True:
    Display(lst)
    print("")

    print("Please Enter your move in this format (row,column) :", end=" ")
    rin, cin = map(int, input().split())

    if(rin<0 or rin>3 or cin<0 or cin>3 or lst[rin-1][cin-1]!=""):
        print("Invalid Input!")
    else:
        lst[rin-1][cin-1]='o'


        c=Checker(lst)
        if (c=='o'):
            print("Human Win!")
            break
        elif(c=="d"):
            print("Draw!")
            break

        t=list()
        high=-1
        score=0
        depth=[0]
        depthc=24
        c=0
        for i in range (0,3):
            for j in range (0,3):
                if(lst[i][j]==""):
                    lst[i][j]='x'
                    score=O_Best_Move(lst,depth,c)
                    if score>=high:
                        if score>high:
                            depthc=24
                        high=score
                        if (depthc>depth[0]):
                            depthc=depth[0]
                            t=(i,j)
                    lst[i][j]=""
        print(t)
        lst[t[0]][t[1]]='x'
        if(Checker(lst)=='x'):
            Display(lst)
            print("Bot Win!")
            break