import random
import time

def isEmpty(board,symbols,i,j):
	if board[i][j] not in symbols:
		return True
	return False

def checkFull(board,symbols):
	for i in range(3):
		for j in range(3):
			if board[i][j] not in symbols:
				return False
	return True

def displayBoard(board):
	print("\n\n")
	for i in range(3):
		print(" \t\t| {}\t| {}\t| {}\t|".format(board[i][0],board[i][1],board[i][2]))
		print("\t\t_________________________",end="\n\n")
	print("\n\n")

def checkWin(board,symbol):
	flag3,flag4=1,1
	for i in range(3):
		flag1,flag2=1,1
		for j in range(3):
			if board[i][j]!=symbol:
				flag1=0
			if board[j][i]!=symbol:
				flag2=0
			if i==j and board[i][j]!=symbol:
				flag3=0
			elif abs(i-j) in [0,2] and board[i][j]!=symbol:
				flag4=0
		if flag1==1 or flag2==1:
			return True
	if flag3==1 or flag4==1:
		return True
	return False

def getMove(board,symbols,player):
	cboard=[[board[i][j] for j in range(3)] for i in range(3)]
	for i in range(3):
		for j in range(3):
			if isEmpty(board,symbols,i,j):
				cboard[i][j]=symbols[player]
				if checkWin(cboard,symbols[player]):
					return 3*i+j+1
				else:
					cboard[i][j]=symbols[1-player]
					if checkWin(cboard,symbols[1-player]):
						return 3*i+j+1
					else:
						cboard[i][j]=board[i][j]
	while True:
		move=random.randint(0,8)
		if isEmpty(board,symbols,move//3,move%3):
			return move+1

def playMulti(board,symbols,names,first):
	player=first
	while True:
		try:
			print(names[player]+"'s Move ...",end="\n\n")
			move=int(input("Enter the Position : "))
			i,j=(move-1)//3,(move-1)%3
			if isEmpty(board,symbols,i,j):
				board[i][j]=symbols[player]
				time.sleep(2)
				displayBoard(board)
				if checkWin(board,symbols[player]):
					print(names[player],"Has Won The Game ...",end="\n\n")
					print("Better Luck Next Time",names[abs(1-player)],"....",end="\n\n")
					return
				elif checkFull(board,symbols):
					print("Match Draw between",names[player],"and",names[abs(1-player)],"...",end="\n\n")
					return
				else:
					player=abs(1-player)
			else:
				print("This Position is Already Filled",end="\n\n")
				time.sleep(2)
				displayBoard(board)
		except:
			print("Enter a Valid Input ...",end="\n\n")
			time.sleep(2)
			displayBoard(board)

def playWithComputer(board,symbols,names,first):
	player=first
	while True:
		try:
			if player==1:
				print(names[player]+"'s Move ...",end="\n\n")
				move=int(input("Enter the Position : "))
			elif player==0:
				print(names[player]+"'s Move ...",end="\n\n")
				move=getMove(board,symbols,player)
			i,j=(move-1)//3,(move-1)%3
			if isEmpty(board,symbols,i,j):
				board[i][j]=symbols[player]
				time.sleep(2)
				displayBoard(board)
				if checkWin(board,symbols[player]):
					print(names[player],"Has Won The Game ...",end="\n\n")
					print("Better Luck Next Time",names[abs(1-player)],"....",end="\n\n")
					return
				elif checkFull(board,symbols):
					print("Match Draw between",names[player],"and",names[abs(1-player)],"...",end="\n\n")
					return
				else:
					player=abs(1-player)
			else:
				print("This Position is Already Filled",end="\n\n")
				time.sleep(2)
				displayBoard(board)
		except:
			print("Enter a Valid Input ...",end="\n\n")
			time.sleep(2)
			displayBoard(board)

def withComputer(board,symbols):
	names=["Computer"]
	names.append(input("Enter tha name of the Player : "))
	if random.randint(1,10)%2==0:
		first=0
	else:
		first=1
	time.sleep(2)
	displayBoard(board)
	playWithComputer(board,symbols,names,first)

def withPlayer(board,symbols):
	names=[]
	names.append(input("Enter the name of Player - 1 : "))
	names.append(input("Enter the name of Player - 2 : "))
	if random.randint(1,10)%2==0:
		first=1
	else:
		first=0
	time.sleep(2)
	displayBoard(board)
	playMulti(board,symbols,names,first)

if __name__=='__main__':
	try:
		print("Enter: \n1: Play a Multiplayer Game \n2: Play Game with Computer",end="\n\n")
		option=int(input("Enter your Option : "))
		board=[[str(3*j+i+1) for i in range(3)] for j in range(3)]
		symbols=["$","*"]
		if option==2:
			withComputer(board,symbols)
		elif option==1:
			withPlayer(board,symbols)
		else:
			print("Enter a Valid Option ...",end="\n\n")
	except:
		print("Enter a Valid Input ...",end="\n\n")