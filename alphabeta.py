from __future__ import print_function  # Only needed for Python 2
import copy
import timeit
from sys import maxsize
from operator import itemgetter
depth = 2
scoreCard = []
scoreCard.append([99,-8,8,6,6,8,-8,99])
scoreCard.append([-8,-24,-4,-3,-3,-4,-24,-8])
scoreCard.append([8,-4,7,4,4,7,-4,8])
scoreCard.append([6,-3,4,0,0,4,-3,6])
scoreCard.append([6,-3,4,0,0,4,-3,6])
scoreCard.append([8,-4,7,4,4,7,-4,8])
scoreCard.append([-8,-24,-4,-3,-3,-4,-24,-8])
scoreCard.append([99,-8,8,6,6,8,-8,99])
arr = []
arr.append(['8','.','.','.','.','.','.','.','.'])
arr.append(['7','.','.','.','.','.','.','.','.'])
arr.append(['6','.','.','.','.','.','.','.','.'])
arr.append(['5','.','.','.','.','.','.','.','.'])
arr.append(['4','.','.','O','X','.','.','.','.'])
arr.append(['3','.','.','.','.','.','.','.','.'])
arr.append(['2','.','.','.','.','.','.','.','.'])
arr.append(['1','.','.','.','.','.','.','.','.'])
arr.append([' ','A','B','C','D','E','F','G','H'])
            
iDict ={ 0 : "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1" }
jDict ={1: "A", 2:"B", 3:"C", 4:"D", 5:"E",6:"F",7:"G",8:"H",
        }


def getDiagTopLeft(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i-1
        q = j-1
        while p>=0 and q>= 1 and arr[p][q] == ch :
            myList.append([p,q])    
            p=p-1
            q=q-1
        if p>=0 and q>=1 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        else:
            return -1
        

def getDiagBotRight(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i+1
        q = j+1
        while p<=7 and q<=8 and arr[p][q] == ch:
            myList.append([p,q]) 
            p=p+1
            q=q+1
        if p<=7 and q<=8 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList    
        return -1

def getDiagBotLeft(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i+1
        q = j-1
        while p<=7 and q>=1 and arr[p][q] == ch :
            myList.append([p,q])
            p=p+1
            q=q-1
        if p<=7 and q>=1 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        return -1

def getDiagTopRight(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i-1
        q = j+1
        while p>=0 and q<=8 and arr[p][q] == ch:
            myList.append([p,q])
            p=p-1
            q=q+1
        if p>=0 and q<=8 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        return -1
        
def getRight(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i
        q = j+1
        while q<= 8 and arr[p][q] == ch :
            myList.append([p,q])
            q=q+1
        if q<=8 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        return -1

def getLeft(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i
        q = j-1
        while q>=1 and arr[p][q] == ch :
            myList.append([p,q])
            q=q-1
        if q>=1 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        return -1

def getBot(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i+1
        q = j;
        while p<= 7 and arr[p][q] == ch:
            myList.append([p,q])
            p=p+1
        if p<=7 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        return -1

def getTop(i,j,player,arr):
        if player == -1:
            ch = 'O'
        else:
            ch = 'X'
        myList = []
        p =i-1
        #print "P is ",p;
        q = j;
        #print "Q is ",q;
        while p>=0 and arr[p][q] == ch:
            myList.append([p,q])
            p=p-1
        if p>=0 and arr[p][q]=='.':
            myList.append([p,q])
            myList = myList[::-1]
            return myList
        return -1


def getAll(player,arr):
    if player == -1:
            ch = 'O'
            var = 'X'
    else:
            ch = 'X'
            var = 'O'
    retList=[]
   
    k=0
    index = {}
    for i in range(0, 8):
        for j in range(1, 9):
            if arr[i][j] == var:
                #print("checking for",i,j)
                if i>1 and j>2 and arr[i-1][j-1] == ch:
                    #print("diagtopleft entered by",i,j)
                    newList = getDiagTopLeft(i,j,player,arr)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)
                if i>0 and arr[i-1][j] == ch:
                    #print("top entered by",i,j)
                    newList = getTop(i,j,player,arr)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)

                if i>0 and j<8 and arr[i-1][j+1] == ch:
                    #print("diagtoprigth entered by",i,j)
                    newList = getDiagTopRight(i,j,player,arr)
                    #print (newList)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)

                if j>1 and arr[i][j-1]== ch:
                    #print("left entered by",i,j)
                    newList = getLeft(i,j,player,arr)
                    #print(newList,"for",i,j)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)

                if j<8 and arr[i][j+1] == ch:
                    #print("right entered by",i,j)
                    newList = getRight(i,j,player,arr)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)

                if i<7 and j>1 and arr[i+1][j-1] == ch:
                    #print("diagbotleft entered by",i,j)
                    newList = getDiagBotLeft(i,j,player,arr)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)

                if i<7 and arr[i+1][j] == ch:
                    #print("bot entered by",i,j)
                    newList = getBot(i,j,player,arr)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)

                if i<7 and j<8 and arr[i+1][j+1] == ch:
                    #print("diagbotright entered by",i,j)
                    newList = getDiagBotRight(i,j,player,arr)
                    if newList != -1:
                        first = newList[0][0],newList[0][1]
                        if first in index:
                            t = index[first]
                            for s in range(1,len(newList)):
                                retList[t].append(newList[s])
                        else:
                            index[first] = k
                            k=k+1
                            retList.append(newList)
                
    if not retList:
        return -1
    else:
        return sorted(retList, key=itemgetter(0))
          
 
def evaluate(arr):
    evalFin = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'O':
                evalFin += scoreCard[i][j]

            elif arr[i][j] == 'X':
                evalFin-= scoreCard[i][j]
    return evalFin
    
    



class Game(object):

    def __init__(self,depth,board,player,editList,name,pname):
        self.editList = editList
        self.size = 8
        self.pname = pname
        self.name = name
        self.board = [[elem for elem in line] for line in board]
        self.depth = depth
        self.player = player
        self.children = []
        self.value = 0;
        
        if player == -1:
            self.ch = 'O'
        else:
            self.ch = 'X'
        
        self.modifyBoard()
    def modifyBoard(self):
        if self.editList:
            for i in self.editList:
                self.board[i[0]][i[1]] = self.ch 

    def printName(self):
        print (self.name)

    def printBoard(self):
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
          for row in self.board]))
        

    def evalBoard(self):
        evaluation = evaluate(self.board)
        return evaluation
    def count(self):
            black = 0
            white= 0
            for i in range(0,8):
                    for j in range(1,9):
                            if self.board[i][j] == 'X':
                                    black+=1
                            elif self.board[i][j] == 'O':
                                    white+=1
            print ("You :" , black)
            print ("Computer :" , white)
         
                            
    def createChildren(self):
        if self.depth >=0:
            self.xList = getAll(self.player,self.board);
            if self.xList == -1:
                if self.name == self.pname :
                     return -1
                else:
                        #print ("Computer: Pass")
                        name = "pass"
                        self.xList = []
                        self.children.append(Game(self.depth-1,self.board,-self.player,self.xList,name,self.name))
                        
                              
            else:
                for i in self.xList:
                    name = i[0][0],i[0][1]
                    self.children.append(Game(self.depth-1,self.board,-self.player,i,name,self.name))
                return 0

def alphaBeta(arr):
    editList =[]
    name = "root"
    pname = []
    global depth
    node = Game(depth,arr,1,editList,name,pname)
    v = Max_Value(node,-maxsize,maxsize)
    #print (v)
    if node.children:
            for child in node.children:
                if child.editList:
                        if child.value == v:
                                #child.printBoard()
                                print ("Computer played :",jDict[child.editList[0][1]]+""+iDict[child.editList[0][0]])
                                return child.board
                else:
                      print("Computer- PASS")
                      return -1
    
    

def Max_Value(node, alpha, beta):
    global depth;    
    if node.depth == 0:
        v = node.evalBoard()
        return v
    v = -maxsize
    myVal = node.createChildren()
    if myVal == -1:
        v = node.evalBoard()
        return v
    for child in node.children:
        v = max(v, Min_Value(child,alpha,beta))
        if v >= beta:
            return v     #pruning
        alpha = max(alpha, v)
        
    node.value = v
    return v
        
def Min_Value(node, alpha, beta):
    global depth    
    if node.depth == 0:
        v = node.evalBoard()
        return v
    v = maxsize
    myVal = node.createChildren()
    if myVal == -1:
        v = node.evalBoard()
        return v
    for child in node.children:
        v = min(v, Max_Value(child,alpha,beta))
        if v<= alpha:
            return v #pruning
        beta = min(beta,v)
    node.value = v
    return v
    
