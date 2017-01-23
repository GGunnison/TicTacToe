def welcomeMessage():
	example_board = [['|','1','|','2','|','3','|'],['|','4','|','5','|','6','|'],['|','7','|','8','|','9','|'],];
	print "Welcome to Tic Tac Toe!"
	player1 = raw_input("Player 1, would you like to use X's or O's? ").upper();
	if player1[0] == 'X':
		print "Player 2, you will be O's."
		player2 = 'O';
	else:
		print "Player 2, you will be X's."
		player2 = 'X';
	print "To make a move enter the number of the square you'd like to place your symbol as seen in the board below"
	printBoard(example_board)
	return player1, player2

def printBoard(board):
	for line in board:
		printline = ''
		for element in line:
			printline += element;
		print printline

def updateBoard(board, move, player):
	position = 1;
	new_board = [];
	for line in board:
		new_line = []
		for element in line:
			if move == position and element == '_':
				element = symbol(player);
			if element in ['_', 'X', 'O']:
				position += 1
			new_line.append(element);
		new_board.append(new_line);
	board = new_board
	return board

def symbol(player):
	if player == "Player1":
		symbol = player1;
	else:
		symbol = player2;
	return symbol

def play(board, player):
	move = raw_input(player + ':');
	board = updateBoard(board, int(move), player);
	if player == "Player1":
		player = "Player2";
	else: 
		player = "Player1";
	return board, player

def check(board):
	if (board[0][1] == board[0][3] == board[0][5] != '_') or \
		(board[1][1] == board[1][3] == board[1][5] != '_') or \
		(board[2][1] == board[2][3] == board[2][5] != '_') or \
		(board[0][1] == board[1][1] == board[2][1] != '_') or \
		(board[0][3] == board[1][3] == board[2][3] != '_') or \
		(board[0][5] == board[1][5] == board[2][5] != '_') or \
		(board[0][1] == board[1][3] == board[2][5] != '_') or \
		(board[0][5] == board[1][3] == board[2][1] != '_') :
		finished = True;
	elif '_' not in [board[0][1],board[0][3],board[0][5],board[1][1],board[1][3],board[1][5],board[2][1],board[2][3],board[2][5]]:
		finished = 'Stalemate';
	else:
		finished = False;
	return finished

def newBoard():
	board = [['|','_','|','_','|','_','|'],['|','_','|','_','|','_','|'],['|','_','|','_','|','_','|']];
	return board

def main(board):
	finished = False;
	player = "Player1";
	while finished == False:
		board, player = play(board, player);
		printBoard(board); 
		finished = check(board);

	if finished != 'Stalemate':
		if player == 'Player1':
			print "Player2 you've won!"
		else:
			print "Player1 you've won!"
	else: 
		print 'Stalemate'

	again = raw_input("Would you like to play again? (Y/N)").upper();
	if again == 'Y':
		board = newBoard();
		printBoard(board);
		main(board);
	else:
		print "Thank you for playing!"

if __name__ == "__main__":
	finished = False;
	player1, player2 = welcomeMessage();
	board = [['|','_','|','_','|','_','|'],['|','_','|','_','|','_','|'],['|','_','|','_','|','_','|']];
	main(board);