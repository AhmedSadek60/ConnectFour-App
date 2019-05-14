import math
class ConnectFour:
    #board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    def __init__(self):
        self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        #Placing a Move on the board
    def placeMove(self,column,player):
        if self.board[0][column]!=0:
            return False
        for i in range(5,0):
            if self.board[i][column] == 0:
                self.board[i][column] = player
                return True
        return False
    
    
    def undoMove(self, column):
        for i in range(0,6): 
            if self.board[i][column] != 0 :
                self.board[i][column] = 0
                break      

    #Printing the board
    def displayConnectFour(self):
        for i in range(0,6):
            for j in range(0,7):
                print(str(self.board[i][j])+" ", end =" ")
            print()


class Connect4AI:
    
    #b=ConnectFour()
    def __init__(self, b):
        self.b = b
        self.nextMoveLocation=-1
        self.maxDepth = 9

    def letOpponentMove(self):
        move=int(input("Enter your move (1-7)"))
        while(move<1 or move > 7 or self.b.board[0][move-1]!=0):
            print("Invalid move.\n\nYour move (1-7): ")
        #Assume 2 is the opponent
        self.b.placeMove(move-1,2)
    
    
    ############## 
    #Game Result
    def gameResult(self, b):
        aiScore = 0 
        humanScore = 0
        for i in range(6,0):
            for j in range(0,7):
                if(self.b.board[i][j]==0): 
                    continue
                
                #Checking cells to the right
                if(j<=3):
                    for k in range(0,4):
                            if(self.b.board[i][j+k]==1):
                                aiScore=aiScore+1
                            elif(self.b.board[i][j+k]==2):
                                humanScore=humanScore+1
                            else:
                                break
                    if (aiScore==4):
                        return 1 
                    elif (humanScore==4):
                        return 2
                    aiScore = 0 
                    humanScore = 0
                
                #Checking cells up
                if(i>=3):
                    for k in range(0,4):
                            if(self.b.board[i-k][j]==1): 
                                aiScore=aiScore+1
                            elif(self.b.board[i-k][j]==2):
                                humanScore=humanScore+1
                            else:
                                break
                    if (aiScore==4):
                        return 1
                    elif (humanScore==4):
                        return 2
                    aiScore = 0
                    humanScore = 0
                
                #Checking diagonal up-right
                if(j<=3 and i>= 3):
                    for k in range(0,4):
                        if(self.b.board[i-k][j+k]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i-k][j+k]==2):
                            humanScore=humanScore+1
                        else:
                            break
                    
                    if(aiScore==4):
                        return 1
                    elif (humanScore==4):
                        return 2
                    aiScore = 0
                    humanScore = 0
                
                #Checking diagonal up-left
                if(j>=3 and i>=3):
                    for k in range(0,4):
                        if(self.b.board[i-k][j-k]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i-k][j-k]==2):
                            humanScore=humanScore+1
                        else:
                            break
                    if(aiScore==4):
                        return 1
                    elif (humanScore==4):
                        return 2
                    aiScore = 0
                    humanScore = 0
                 
            
        
        
        for j in range(0,7):
            #Game has not ended yet
            if(self.b.board[0][j]==0):
                return -1
        
        #Game draw!
        return 0
    
    
    def calculateScore(self,aiScore,moreMoves):  
        moveScore = 4 - moreMoves
        if(aiScore==0):
            return 0
        elif(aiScore==1):
            return 1*moveScore
        elif(aiScore==2):
            return 10*moveScore
        elif(aiScore==3):
            return 100*moveScore
        else:
            return 1000
    
    #Evaluate board favorableness for AI
    def evaluateConnectFour(self):
      
        aiScore=1
        score=0
        blanks = 0
        k=0
        moreMoves=0
        for i in range(6,0):
            for j in range(0,7):
                
                if(self.b.board[i][j]==0 or self.b.board[i][j]==2):
                    continue 
                #from left to right chances 
                #checks in the left half of the board if there is successive coins for the same player 
                #if there is successive coins it increases aiscore by 1
                #if the next coin is for the opposite player it makes aiscore=0 #No chance to win in this direction
                #else: there is blank spaces #blanks++
                if(j<=3):
                    for k in range(0,4):
                        if(self.b.board[i][j+k]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i][j+k]==2):
                            aiScore=0
                            blanks = 0
                            break
                        else:
                            blanks=blanks+1
                    
                    #checks the empty square for the next coloumns
                    #example
                    '''
                    000////
                    101////
                    111////
                    222////
                    121////
                    112////
                    '''
                    # "/" is the empty cells that represent an empty square
                    moreMoves = 0 
                    if(blanks>0): 
                        for c in range(0,4):
                            column = j+c
                            for m in range(i,6):
                                if(self.b.board[m][column]==0):
                                    moreMoves=moreMoves+1
                                else:
                                    break
                            
                    if(moreMoves!=0):
                        score += self.calculateScore(aiScore, moreMoves)
                    aiScore=1   
                    blanks = 0

                #from bottom to up chance
                if(i>=3):
                    for k in range(0,4):
                        if(self.b.board[i-k][j]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i-k][j]==2):
                            aiScore=0
                            break

                    moreMoves = 0 
                    if(aiScore>0):
                        column = j
                        #for(int m=i-k+1 m<=i-1m++):
                        for m in range(i-k+1,i):
                            if(self.b.board[m][column]==0):
                                moreMoves=moreMoves+1
                            else:
                                break
                        
                    if(moreMoves!=0):
                        score += self.calculateScore(aiScore, moreMoves)
                    aiScore=1  
                    blanks = 0

                #from right to left chance
                if(j>=3):
                    for k in range(0,4):
                        if(self.b.board[i][j-k]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i][j-k]==2):
                            aiScore=0
                            blanks=0
                            break
                        else:
                            blanks=blanks+1

                    moreMoves=0
                    if(blanks>0):
                        for c in range(0,4):
                            column = j- c
                            for m in range(i,6):
                                if(self.b.board[m][column]==0):
                                    moreMoves=moreMoves+1
                                else:
                                    break

                    
                    if(moreMoves!=0):
                        score += self.calculateScore(aiScore, moreMoves)
                    aiScore=1 
                    blanks = 0
                 
                #for diagonal chances right up
                if(j<=3 and i>=3):
                    for k in range(0,4):
                        if(self.b.board[i-k][j+k]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i-k][j+k]==2):
                            aiScore=0
                            blanks=0
                            break
                        else:
                            blanks=blanks+1

                    moreMoves=0
                    if(blanks>0):
                        for c in range(0,4):
                            column = j+c
                            row = i-c
                            for m in range(row,6):
                                if(self.b.board[m][column]==0):
                                    moreMoves=moreMoves+1
                                elif(self.b.board[m][column]==1):
                                    continue
                                else:
                                    break

                        if(moreMoves!=0):
                            score += self.calculateScore(aiScore, moreMoves)
                        aiScore=1
                        blanks = 0
                    
                
                # for diagonal chance left up
                if(i>=3 and j>=3):
                    for k in range(0,4):
                        if(self.b.board[i-k][j-k]==1):
                            aiScore=aiScore+1
                        elif(self.b.board[i-k][j-k]==2):
                            aiScore=0
                            blanks=0
                            break
                        else:
                            blanks=blanks+1                        
                    
                    moreMoves=0
                    if(blanks>0):
                        for c in range(0,4):
                            column = j-c
                            row = i-c
                            for m in range(row,6):
                                if(self.b.board[m][column]==0):
                                    moreMoves=moreMoves+1
                                elif(self.b.board[m][column]==1):
                                    continue
                                else:
                                    break
                        
                        if(moreMoves!=0):
                            score += self.calculateScore(aiScore, moreMoves)
                        aiScore=1
                        blanks = 0
        return score

    
    def minimax(self,depth,turn,alpha,beta):
        
        if(beta<=alpha):
            if(turn == 1):
                return math.inf
            else:
                return -math.inf

        gameresult = self.gameResult(self.b)
        
        if(gameresult==1):
            return math.inf/2
        elif(gameresult==2):
            return -math.inf/2
        elif(gameresult==0):
            return 0 
        
        if(depth==self.maxDepth):
            return self.evaluateConnectFour()
        
        maxScore = -math.inf
        minScore = math.inf
                
        for j in range(0,7):
            
            currentScore = 0
            
            if(self.b.board[0][j]!=0):
                continue 
            
            if(turn==1):
                self.b.placeMove(j, 1)
                currentScore = self.minimax(depth+1, 2, alpha, beta)
                
                if(depth==0):
                    print("Score for location "+str(j)+" = "+str(currentScore)+"\n")
                    if(currentScore > maxScore):
                        nextMoveLocation = j 
                    if(currentScore == math.inf/2):
                        self.b.undoMove(j)
                        break
                
                maxScore = max(currentScore, maxScore)
                alpha = max(currentScore, alpha)  
            
            elif(turn==2):
                self.b.placeMove(j, 2)
                currentScore = self.minimax(depth+1, 1, alpha, beta)
                minScore = min(currentScore, minScore)
                beta = min(currentScore, beta) 
             
            self.b.undoMove(j) 
            if(currentScore == math.inf or currentScore == -math.inf):
                break 
        if turn==1:
            return maxScore
        else:
            return minScore
    
    def getAIMove(self):
        self.nextMoveLocation = -1
        self.minimax(0, 1, -math.inf, math.inf)
        return self.nextMoveLocation
    
    def playAgainstAIConsole(self):
        humanMove=-1
        #TODO
        #Scanner scan = new Scanner(System.in)
        print("Would you like to play first? (yes/no) ")
        #TODO
        answer=input()
        
        if(answer=="yes"):
            #connect= Connect4AI()
            self.letOpponentMove()
        self.b.displayConnectFour()
        self.b.placeMove(3, 1)
        self.b.displayConnectFour()
        
        while(1):
            self.letOpponentMove()
            self.b.displayConnectFour()
            gameresult = self.gameResult(self.b)
            if(gameresult==1):
                print("AI Wins!\n")
                break
            elif(gameresult==2):
                print("You Win!\n")
                break
            elif(gameresult==0):
                print("Draw!\n")
                break
            
            self.b.placeMove(self.getAIMove(), 1)
            self.b.displayConnectFour()
            gameresult = self.gameResult(self.b)
            if(gameresult==1):
                print("AI Wins!\n")
                break
            elif(gameresult==2):
                print("You Win!\n")
                break
            elif(gameresult==0):
                print("Draw!\n")
                break
    
    def main():
        b = ConnectFour()
        ai = Connect4AI(b)  
        ai.playAgainstAIConsole()
#TODO  
Connect4AI.main()