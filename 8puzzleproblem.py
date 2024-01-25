from copy import deepcopy

from pyautogui import sleep


moves=[[1,0],[0,1],[-1,0],[0,-1]]
initial=[[1,2,3],[4,0,6],[7,5,8]]
goal=[[1,2,3],[4,5,6],[7,8,0]]
class node:
    def __init__(self,matrix,depth,whitespace):
        self.matrix = matrix
        self.depth = depth
        self.whitespace = whitespace
        self.heuristic=calculate_hueristic(self.matrix)+self.depth
        
    def print_mat(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(self.matrix[i][j],end=" ")
            print()
        
def isvalid(i,j):
    if i>0 and j>0 and i<len(goal) and j<len(goal):
        return True 
    else: return False
    
def calculate_hueristic(matrix):
    val=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]!=goal[i][j]:
                val+=1
    return val

def new_node(matrix,depth,current,next):
    new_matrix=deepcopy(matrix)
    x1=current[0]
    y1=current[1]
    x2=next[0]
    y2=next[1]
    new_matrix[x1][y1],new_matrix[x2][y2]=new_matrix[x2][y2],new_matrix[x1][y1]
    nn=node(new_matrix,depth+1,next)
    return nn
    
    
    
def solve():
    current=node(initial,0,(1,1))
    states=[]
    states.append(current)
    while True:
        sleep(1)
        least=states[0]
        for i in states:
            if i.heuristic<least.heuristic:
                least=i
        current=least   
        current.print_mat()
        states.remove(current)
        if current.matrix==goal:
            print("Goal Found")
            break
        
        for i in moves:
            move=(i[0]+current.whitespace[0],i[1]+current.whitespace[1])
            if isvalid(move[0],move[1]):
                nn=new_node(current.matrix,current.depth,current.whitespace,move)
                states.append(nn)
                
solve()