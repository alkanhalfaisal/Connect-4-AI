import random   # for randomAI
import time     # for delay between AI turn and Human turn
import numpy as np

boardTest1 = [
    ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  "]
   ]

boardTest1 = np.array(
  [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
  ]
)
board= boardTest1
def isWinner(player, board):
    """Return true if the player has win. False otherwise"""
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            # left to right
            if j <= (len(board[i]) - 4):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                    return True

            # Up to down
            if i <= (len(board) - 4):
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                    return True

            # Diag
            if i <= (len(board) - 4) and j <= (len(board[i]) - 4):
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                    return True

            if i <= (len(board) - 4) and j <= (len(board[i]) - 4):
                if board[i][j+3] == board[i+1][j+2] == board[i+2][j+1] == board[i+3][j] == player:
                    return True 
    return False
    
def printBoard(board):
    """Print the board row by row"""
    print("  1    2    3    4    5    6    7")
    for row in board:
        print("------------------------------------\n|", end="")
        for cell in row:
            cell = "🟡" if cell == 1 else "🔴" if cell == 2 else "  "
            print(f" {cell} |", end="")
        print()
    print("------------------------------------")

def isBoardFull(board):
    """Return True if board is full. False otherwise"""
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True
    
def findValidMove(column, board): # 5 , board
    """Check if the move is valid or not starting from the last row. If it's valid will return [True,<the row should play in it>]. If not will return [False, None]"""

    rows = [5,4,3,2,1,0] 

    for row in rows:
        
        if board[row][column] == 0:
            return True, row
    return False, None
    
def getEmptyBoard():
    """Return an empty board"""

    return np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    )

def putMove(player, column, board): # .. , 5 , board
    """Try to make the move and return True if the move success. False otherwise"""
    
    isValid, row = findValidMove(column,board)
    if isValid:
        board[row][column] = player
        return row, column
    else:
        return -1, None

def getAllPossibleMoves(board):
    """Return all possible moves that could play on the current board"""
    columns = 7
    return [col for col in range(columns) if findValidMove(col, board)[0]]

def delay():
    """Delay between human turn (🔴) and AI turn (🟡)"""
    
    print("Computer is thinking", end="")
    for _ in range(3):
        print(".", flush=True, end="")
        time.sleep(0.5)
    print()

def isValidAnswer(answer):
    """Return true if the answer yes or no. False otherwise"""
    return answer == "y" or answer == "yes" or answer == "n" or answer == "no"

def intro(board):
    """Print the intro for the Game"""

    print("Welcome to Connect 4 Game. By FTC")
    print("\nExplain the Rules:")
    print("To Choose Where to Play. Choose the Column As Following:")
    printBoard(board)
    print()

def chooseDifficulty():
    """Ask the user to enter a valid difficulty and return his/her choice"""
    
    print("Choose AI difficulty. Options: \n-Easy \n-Medium \n-Hard \n-Impossible")
    while(True):
        difficulty = input("Enter your choice: ").lower()
        if (difficulty == "easy" or difficulty == "medium" or difficulty == "hard" or difficulty == "impossible"):
            return difficulty
        else:
            print("ERROR: Invalid option. Please try again")

def chooseHowStart():
    """Ask the user to enter a valid choice. Return true if the user want to play first. False otherwise"""
    
    while(True):
        answer = input("Do you want to go first? (Yes/No): ").lower()
        if isValidAnswer(answer):
            if answer == "y" or answer == "yes":
                return True
            else:
                return False
        else:
            print("ERROR: Invalid option. Please try again")

def chooseToContinue():
    """Ask the user to enter a valid choice. Return true if the user want to play again. False otherwise"""
    
    while(True):
        answer = input("Do you want to play again? (Yes/No): ").lower()
        if isValidAnswer(answer):
            if answer == "y" or answer == "yes":
                return True
            else:
                return False
        else:
            print("ERROR: Invalid option. Please try again")

# Methods Not Finish Yet is Below... 
def playPotatoMode(player, board):
    """Potato mode"""
    possibleMoves = getAllPossibleMoves(board)
    randomMove = random.choice(possibleMoves) 
    putMove(player, randomMove, board)

def playEasyMode(player, board):
    easyMove = calculateBestMove(board, 5, True, 5, float('-inf'), float('inf'))
    putMove(player, easyMove, board)

def playMediumMode(player, board):
    mediumMove = calculateBestMove(board, 6, True, 6, float('-inf'), float('inf'))
    putMove(player, mediumMove, board)

def playHardMode(player, board):
    # Should be playing by some smart logic.. with out using minimax algorthim 
    smartMove = calculateBestMove(board, 7, True, 7, float('-inf'), float('inf'))
    putMove(player, smartMove, board)

def playImpossibleMode(player, board):
    # Should receive a best move ever from a minimax function
    bestMove = calculateBestMove(board, 9, True, 9, float('-inf'), float('inf'))
    putMove(player, bestMove, board)
    

def isConnect(player, board, piece):
    pass
    
    
def isWinner(player, board):
    """Return true if the player has win. False otherwise"""
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            # left to right
            if j <= (len(board[i]) - 4):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                    return True

            # Up to down
            if i <= (len(board) - 4):
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                    return True

            # Diag
            if i <= (len(board) - 4) and j <= (len(board[i]) - 4):
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                    return True

            if i <= (len(board) - 4) and j <= (len(board[i]) - 4):
                if board[i][j+3] == board[i+1][j+2] == board[i+2][j+1] == board[i+3][j] == player:
                    return True 
            
    return False
    
    
def calculateBestMove(board, depth, isMax, difficulty , alpha, beta):
    """This method will calculate the best move ever for the AI on the current board. Using minimax algorithm"""
    
    if isWinner(1, board):
        return 1000
    elif isWinner(2, board):
        return -1000
    elif isBoardFull(board) or depth == 0:
        return 0
    
    if isMax:
        maxScore = [float('-inf'), -1]
        
        for possibleMove in getAllPossibleMoves(board):
            row, col = putMove(1, possibleMove, board)
            if row != -1:
                score = calculateBestMove(board, depth-1, False, difficulty, alpha, beta) - 1
                
              
                
                
                
                # printBoard(board)
                board[row][col] = 0
                # print(f"Debug: [max(maxScore[0], score), col] => [max({maxScore[0]}, {score}), {col}]")
                
                if maxScore[0] < score:
                    maxScore = [score, col]
                
                # maxScore = [max(maxScore[0], score), col]
                alpha = max(alpha, score)
                
                if beta <= alpha:
                    break
                
        if depth == difficulty:
            return maxScore[1]
        return maxScore[0]
    
    else:
        minScore = [float('inf'), -1]
        
        for possibleMove in getAllPossibleMoves(board):
            row, col = putMove(2, possibleMove, board)
            if row != -1:
                score = calculateBestMove(board, depth-1, True, difficulty, alpha, beta) + 1
                board[row][col] = 0

                if minScore[0] > score:
                    minScore = [score, col]
                # minScore = [min(minScore[0], score), col]
                beta = min(beta, score)
                
                if beta <= alpha:
                    break
                
        if depth == difficulty:
            return minScore[1]
        return minScore[0]
    
            
    
# def calculateBestMove1(board, depth, isMaximizing, difficulty): # 100% winning depth = 42
#     """This method will calculate the best move ever for the AI on the current board. Using minimax algorithm"""
    
#     if isWinner(1, board):
#         return 1000
#     elif isWinner(2, board):
#         return -1000
#     elif isBoardFull(board) or depth==0:
#         return 0

#     if(isMaximizing): # Bot turn 🟡
#         bestScore = [float('-inf'), -1]
        
#         scoreList =[]
#         for possibleMove in getAllPossibleMoves(board):
#             row , column = putMove(1, possibleMove, board) # pos = [row, col] = [0, 4] 
#             if row != -1:
#                 scoreList.append([calculateBestMove(board, depth-1, False, difficulty) - 1, possibleMove])
#                 board[row][column] = 0

#         if depth == difficulty: #  42
#             for score in scoreList:
#                 if score[0] >= bestScore[0]:
#                     bestScore = score
#             return bestScore[1]

#         return max([score[0] for score in scoreList])

#     else:
#         bestScore = [float('inf'), 1]

#         scoreList =[]
#         for possibleMove in getAllPossibleMoves(board):
#             row , column = putMove(2, possibleMove, board) # pos = [row, col] = [ ,  ]
#             if row != -1:
#                 scoreList.append([calculateBestMove(board, depth-1, True, difficulty) + 1, possibleMove])
#                 board[row][column] = 0
                
#         if depth == difficulty: #  42
#             for score in scoreList:
#                 if score[0] <= bestScore[0]:
#                     bestScore = score
#             return bestScore[1]
        
#         return min([score[0] for score in scoreList])

def playAI(player, board, difficulty):
    if difficulty == "easy":
        playEasyMode(player, board)
    elif difficulty == "medium":
        playMediumMode(player, board)
    elif difficulty == "hard":
        playHardMode(player, board)
    elif difficulty == "impossible":
        playImpossibleMode(player, board)

# Main Method.. Omar working on it
def startGame():
        
    humanPlayer = 2
    botPlayer = 1
    # board = getEmptyBoard()
    board = boardTest1
    isContinuingPlaying = True
    
    intro(board)

    while(isContinuingPlaying):

        isHumanTurn = chooseHowStart()
        difficulty = chooseDifficulty()

        print("\nGame Started:\n")
        printBoard(board)
        while(True):
            if(isHumanTurn):
                try:
                    column = int(input("Your move (1-7): ")) - 1
                    if(column > 6 or column < 0):
                        raise Exception()
                    if putMove(humanPlayer, column, board)[0] == -1:
                        raise Exception()
                except:
                    print("ERROR: Invalid column. Please try again")
                    continue

                printBoard(board)

                if isWinner(humanPlayer, board):
                    print("Your the Winner. Good job!!")
                    break 
                elif isBoardFull(board):
                    print("sorry.. no one wins")
                    break

            else:
                playAI(botPlayer, board, difficulty)
                #delay()
                printBoard(board)

                if isWinner(botPlayer, board):
                    print("ohh.. LOSER")
                    break 
                elif isBoardFull(board):
                    print("sorry.. no one wins")
                    break

            isHumanTurn = not isHumanTurn

        isContinuingPlaying = chooseToContinue()
        if isContinuingPlaying:
            board = getEmptyBoard()
        else:
            print("\nGood bye <3")