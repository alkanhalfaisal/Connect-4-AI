import pygame
import connectBoard
import spritesheet
from M import * 
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

width_of_a_col = 55
hight_of_a_row = 55

# set the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Connect 4')
#sprite
sprite_sheet_image = pygame.image.load('board.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
#connect 4
#red_circle = pygame.image.load('red.png')
#red = spritesheet.SpriteSheet(red_circle)

#white_circle = pygame.image.load('white.png')
#white = spritesheet.SpriteSheet(white_circle)

BG = (50, 50, 50)
BLACK = (0, 0, 0)
COLUMN_COUNT = 7
ROW_COUNT = 6
BG = (50, 50, 50)
RED = (102, 102, 255)
YELLOW = (255, 51, 153)
RADIUS = 30
xies = []
# for after the game is implemeted


def get_axis():
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			xies.append(c*width_of_a_col+90)


get_axis()
xies = list(set(xies))
xies.sort()

def draw_board(board,s):
		#update background
	s.fill(BG)

	#show frame image



	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(s, RED, (c*width_of_a_col+90, r*hight_of_a_row+70), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(s, YELLOW, (c*width_of_a_col+90, r*hight_of_a_row+70), RADIUS)
	
	s.blit(frame_0, (0, 0))
	pygame.display.update()



def add_the_circle( xLoc, yLoc):
	
		pygame.draw.circle(screen, RED, (xLoc, yLoc), RADIUS)


#sprite frames
frame_0 = sprite_sheet.get_image(0, 500, 500, 1, BLACK)
#rr = red.get_image(0,100,100,1.5,BLACK)
#ww = white.get_image(0,100,100,1.5,BLACK)
imgX, imgY = 0,0
run = True

humanPlayer = 2

def get_col(x,y):
	margin = 30 
	
	if(y>40 and y<440):
		for i in range(0,len(xies)): 
			
			if(x <= xies[i]+margin and x>xies[i]-margin):
				""
				print (x,x+1)
				return i 
		
		return -1 	
	else: 
		return -1 
		
	
isHumanTurn = chooseHowStart()
difficulty = chooseDifficulty()
isContinuingPlaying = True

while isContinuingPlaying:

	draw_board(board,screen)
	humanPlayer = 2
	botPlayer = 1
	column = None
	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			imgX, imgY = pygame.mouse.get_pos()
			column = get_col(imgX, imgY)
			print(column)
			if column == None:
				pass
	pygame.display.update()
    
	print ("m,")

	if(isHumanTurn):
		if column == None : continue 
		try:
			
			if(column > 6 or column < 0):
				raise Exception()
			if putMove(humanPlayer, column, board)[0] == -1:
				raise Exception()
		except:
			print("ERROR: Invalid column. Please try again")
			continue

		

		if isWinner(humanPlayer, board):
			print("Your the Winner. Good job!!")
			break
		elif isBoardFull(board):
			print("sorry.. no one wins")
			break

	else:
		playAI(botPlayer, board, difficulty)
		#delay()
		

		if isWinner(botPlayer, board):
			print("ohh.. LOSER")
			break
		elif isBoardFull(board):
			print("sorry.. no one wins")
			break

	isHumanTurn = not isHumanTurn


	
	
pygame.quit()

# print (imgX)
# print (imgY)
