
from PIL import Image
from collections import deque

cell_size=20
def Pix(r,c,cell_size,pixels,t):
    for i in range(c,c+cell_size):
        for j in range(r,r+cell_size):
            pixels[i,j]=t

def S_Finder(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst[i])):
            if(maze[i][j]=='s'):
                return (i,j)

def Img(maze,img_name,Path_Set=None):
    if Path_Set==None:
        img=Image.new('RGB',(len(maze[0])*cell_size,len(maze)*cell_size),'white')
        pixels=img.load()
        r=0
        for i in maze:
            c=0
            for j in i:
                if j=='#':
                    Pix(r,c,cell_size,pixels,(0,0,0))
                elif j=='e':
                    Pix(r,c,cell_size,pixels,(255,0,0))
                elif j=='s':
                    Pix(r,c,cell_size,pixels,(0,128,0))
                else:
                    Pix(r,c,cell_size,pixels,(255,255,255))
                c+=cell_size
            r+=cell_size
        img.save(img_name)
    else:
        img=Image.new('RGB',(len(maze[0])*cell_size,len(maze)*cell_size),'white')
        pixels=img.load()
        r=0
        for i in maze:
            c=0
            for j in i:
                if (r,c) in Path_Set:
                    Pix(r,c,cell_size,pixels,(255, 255, 0))
                elif j=='#':
                    Pix(r,c,cell_size,pixels,(0,0,0))
                elif j=='e':
                    Pix(r,c,cell_size,pixels,(255,0,0))
                elif j=='s':
                    Pix(r,c,cell_size,pixels,(0,128,0))
                else:
                    Pix(r,c,cell_size,pixels,(255,255,255))
                c+=cell_size
            r+=cell_size
        img.save(img_name)

def Read(file):
    f=open(file,'r')
    lst=f.read().splitlines()
    maze=[]
    for i in lst:
        maze.append(list(i))
    return maze

def Path_mod(path):
    for i in range(0,len(path)):
        path[i]=(path[i][0]*cell_size,path[i][1]*cell_size)



class Operation:
    def __init__(self,maze,visited,path):
        self.maze=maze
        self.visited=visited
        self.path=path

    def Ans_Check(self,x,y):
        if(self.maze[x][y]=='e'):
            return True
        else:
            return False
    def Valid_Path(self,x,y):
        if( x>-1 and x<len(self.maze) and y>-1 and y<len(self.maze[0]) and self.maze[x][y]!='#' and (x,y) not in self.visited):
            return True
        else:
            return False

class DFS(Operation):
    def __init__(self, maze, visited, path):
        super().__init__(maze, visited, path)
    
    def Start(self,x,y):
        self.visited.add((x,y))
        if self.Ans_Check(x,y)==True:
            print(self.path)
            pp=[]
            pp=self.path.copy()
            pp.pop()
            Path_mod(pp)
            Path_Set=set(pp)
            Img(maze,'maze_Ans_DFS.png',Path_Set)
        else:
            if(self.Valid_Path(x-1,y)==True):
                self.path.append((x-1,y))
                self.Start(x-1,y)
                self.path.pop()
            if(self.Valid_Path(x,y-1)==True):
                self.path.append((x,y-1))
                self.Start(x,y-1)
                self.path.pop()
            if(self.Valid_Path(x+1,y)==True):
                self.path.append((x+1,y))
                self.Start(x+1,y)
                self.path.pop()
            if(self.Valid_Path(x,y+1)==True):
                self.path.append((x,y+1))
                self.Start(x,y+1)
                self.path.pop()
    def Ans(self):
        print(self.ans_path)
        return self.ans_path

class BFS(Operation):
    def __init__(self, maze, visited, path):
        super().__init__(maze, visited, path)
    def Path_In(self,x,y,q,parent_track):
        if(self.Valid_Path(x-1,y)==True):
            q.append((x-1,y))
            parent_track[(x-1,y)]=(x,y)
        if(self.Valid_Path(x,y-1)==True):
            q.append((x,y-1))
            parent_track[(x,y-1)]=(x,y)
        if(self.Valid_Path(x+1,y)==True):
            q.append((x+1,y))
            parent_track[(x+1,y)]=(x,y)
        if(self.Valid_Path(x,y+1)==True):
            q.append((x,y+1))
            parent_track[(x,y+1)]=(x,y)
            
    def Path_Ans(self,x,y,t1,t2,parent_track):
        h1=t1
        h2=t2
        while(1>0):
            t=parent_track[(h1,h2)]
            h1=t[0]
            h2=t[1]
            if(h1==x and h2==y):
                break
            self.path.append((h1,h2))

    def Start(self,x,y):
        q=deque()
        parent_track=dict()
        self.visited.add((x,y))
        self.Path_In(x,y,q,parent_track)
        while(len(q)>0):
            t=q.popleft()
            self.visited.add((t[0],t[1]))
            if (self.Ans_Check(t[0],t[1])==True):
                self.Path_Ans(x,y,t[0],t[1],parent_track)
                print(self.path)

                pp=self.path.copy()
                Path_mod(pp)
                Path_Set=set(pp)
                Img(maze,'maze_Ans_BFS.png',Path_Set)

                break
            else:
                self.Path_In(t[0],t[1],q,parent_track)

maze=Read('2nd_maze.txt')
s1=set()
s2=set()
lst1=[]
lst2=[]
st_index=S_Finder(maze)
m1=BFS(maze,s1,lst2)
m1.Start(st_index[0],st_index[1])
m2=DFS(maze,s2,lst2)
m2.Start(st_index[0],st_index[1])
Img(maze,'maze.png')