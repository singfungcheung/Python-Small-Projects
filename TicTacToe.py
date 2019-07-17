"""
This is a game of Tic Tac Toe.
My first milestone project.
"""

# This function is to print the boards side by side onto the screen
def print_board(board1,board2):
	print(board1[6] + " | " + board1[7] + " | " + board1[8], end = "		"), print(board2[6] + " | " + board2[7] + " | " + board2[8])
	print(board1[3] + " | " + board1[4] + " | " + board1[5], end = "		"), print(board2[3] + " | " + board2[4] + " | " + board2[5])
	print(board1[0] + " | " + board1[1] + " | " + board1[2], end = "		"), print(board2[0] + " | " + board2[1] + " | " + board2[2])

# This is to ask the first player whether they want to be 'X' or 'O', 
# or whatever they want.
def select_player1():
	playerInput = input("Hi first player. What symbol would you use to start things off?\n")

	# This is to check whether the symbol is more than a charcter. If it is, ask the player to try again. 
	while len(playerInput) > 1:
		print("Hey! That's not a symbol. It should be a character only. Try again.")
		playerInput = input("What symbol would you like to use to start things off?\n")
		
	print(f"Okay, you selected {playerInput.upper()} as your symbol")
	return playerInput.upper()

# This is to ask the second player whether they want to be 'X' or 'O', 
# or whatever they want.
def select_player2():
	playerInput = input("Hi second player. What symbol would you use to start things off?\n")

	# This is to check whether the symbol is more than a charcter. If it is, ask the player to try again. 
	while len(playerInput) > 1 or (playerInput == player1):
		print("Hey! That's not a symbol. It should be a character only. Try again.")
		playerInput = input("What symbol would you like to use to start things off?\n")
		
	print(f"Okay, you selected {playerInput.upper()} as your symbol")
	return playerInput.upper()

# This is to place the marker in a specific position on the board
def place_marker(board1,board2,marker,position):
	board1[position-1] = " "
	board2[position-1] = marker

# This is to ask the player where they want to put their symbol
def ask_player_for_placement(player):
	position = input(f"{player}! Where would you like to go? ")
	while True:
		if int(position) not in range(1,10):
			position = input("Hey! Select one of the numbers on the board! Try again: ")
			continue
		else:
			return int(position)

# This is to check whether anyone has won in a given position. If not, game continues
def check_win(playerSymbol):
	if (board2[0] == playerSymbol and board2[1] == playerSymbol and board2[2] == playerSymbol) or\
	(board2[3] == playerSymbol and board2[4] == playerSymbol and board2[5] == playerSymbol) or\
	(board2[6] == playerSymbol and board2[7] == playerSymbol and board2[8] == playerSymbol) or\
	(board2[0] == playerSymbol and board2[3] == playerSymbol and board2[6] == playerSymbol) or\
	(board2[1] == playerSymbol and board2[4] == playerSymbol and board2[7] == playerSymbol) or\
	(board2[2] == playerSymbol and board2[5] == playerSymbol and board2[8] == playerSymbol) or\
	(board2[0] == playerSymbol and board2[4] == playerSymbol and board2[8] == playerSymbol) or\
	(board2[2] == playerSymbol and board2[4] == playerSymbol and board2[6] == playerSymbol):
		return True

# This is to ask the players if they want to play again
def play_again():
	while True:
		response = input("Would you like to play again? Y/N ")
		if response == "": #if player enters the 'enter' or 'return' key
			response = 'y'
		response = response.upper()
		if response != 'Y' and response!='N':
			print("Error! Pick Y or N")
			continue
		else:
			return response == 'Y'

while True: #This while loop keeps the possibility of playing the game again without rerunning the code
	numberOfTurns = 0
	print("Welcome to the game of Tic Tac Toe!")
	player1 = select_player1() #symbol of player 1
	player2 = select_player2() #symbol of player 2
	while player1 == player2:
		print("You can't be the same as player 1! Try again!")
		player2 = select_player2()
	print("Okay! Let's go!")
	#board1 is for the player to visually see where they want to place their mark
	board1 = [str(num) for num in list(range(1,10))]
	#board2 is for the player to fill in
	board2 = [" "]*9
	print_board(board1,board2)
	print("\n") #print a new line for readibility

	while True: #This while loop keeps the game going until a result (win,draw) is achieved
		place_marker(board1,board2,player1,ask_player_for_placement(player1))
		print_board(board1,board2)
		numberOfTurns += 1
		if check_win(player1):
			print("player 1 wins!")
			break
		if numberOfTurns == 9:
			print("Draw! point splits 1/2 - 1/2")
			break
		place_marker(board1,board2,player2,ask_player_for_placement(player2))
		print_board(board1,board2)
		if check_win(player2):
			print("player 2 wins!")
			break
		numberOfTurns += 1
		if numberOfTurns == 9:
			print("Draw! point splits 1/2 - 1/2")
			break

	if play_again():
		continue
	else:
		print("Thanks for playing!")
		break