# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:23:08 2017

@author: Chetan
"""
import numpy as np
import hello as h
import alphabeta as ab
import os

def modifyBoard(editList,ch):
        if editList:
            for i in editList:
                arr[i[0]][i[1]] = ch 
def count(arr):
        black = 0
        white= 0
        for i in range(0,8):
                for j in range(1,9):
                        if arr[i][j] == 'X':
                                black+=1
                        elif arr[i][j] == 'O':
                                white+=1
        print "You :" , black
        print "Computer :" , white
        return white -black
arr = [];
arr.append(['1','.','.','.','.','.','.','.','.'])
arr.append(['2','.','.','.','.','.','.','.','.'])
arr.append(['3','.','.','.','.','.','.','.','.'])
arr.append(['4','.','.','.','O','X','.','.','.'])
arr.append(['5','.','.','.','X','O','.','.','.'])
arr.append(['6','.','.','.','.','.','.','.','.'])
arr.append(['7','.','.','.','.','.','.','.','.'])
arr.append(['8','.','.','.','.','.','.','.','.'])
arr.append([' ','A','B','C','D','E','F','G','H'])
            
iDict ={ 0 : "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8" }
jDict ={1: "A", 2:"B", 3:"C", 4:"D", 5:"E",6:"F",7:"G",8:"H",
        }
def printBoard():
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
          for row in arr]))
player = 1
print "***** LET'S PLAY REVERSI *****"
print "You - X"
print "Computer - O"
printBoard()
flag = 0
while True:
    player = -player
    if player< 0:
        var = 'X'
    else:
        var = 'O'
    moveList = ab.getAll(player,arr)
    print "Your turn!!"
    
    k=0;
    if moveList== -1:
            if prev == 1:
                    print "Game over!"
                    score = count(arr)
                    if score < 0:
                            print "You Win!"
                    else:
                            print "Computer Wins!"
                    break
            else:
                    print "Whoops! No moves for you!\n Computer plays again!"
                    prev = 1
    else:
        print "Available moves :",
        for i in moveList:
                print str(k)+")"+" "+jDict[i[0][1]]+""+iDict[i[0][0]],
                k=k+1
                
        t = int(raw_input("\nEnter Choice:\n"))
        modifyBoard(moveList[t],var)
        prev = 0
        printBoard()
    print "Computer's turn:"
    player = -player
    res = ab.alphaBeta(arr)
    if res == -1:
            if prev == 1:
                    break
            else:
                    prev = 1
    else:
            arr =res
            printBoard()
            count(arr)
            prev=1
