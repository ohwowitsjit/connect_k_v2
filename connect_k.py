def print_board():
	for i in range(0, no_rows):
		print(board[i])
	
def place_marker(turn_no):
	place_col = int(input("Enter the the index of the coloumn you want to place your marker in: "))
	freq_called[place_col] = freq_called[place_col] +1

	marker = "C"
	if ((turn_no)%2)==0:
		marker = "A"
	elif ((turn_no)%2)==1:
		marker = "B"
	
	if freq_called[place_col] >= no_cols:
		print("The coloumn is full. Please retry:")
		place_marker(turn_no)
	
	board[no_rows-freq_called[place_col]] = board[no_rows-freq_called[place_col]][:(place_col-1)] + marker + board[no_rows-freq_called[place_col]][place_col:]
	
def check_win():
	checker = board[no_rows-(freq_called[place_col]-1)][place_col]
	no_checks=0
	for i in range(0, no_k):
		if board[no_rows-(freq_called[place_col]-1)][place_col+i]==checker:
			no_checks = no_checks+1


	
	
no_rows = int(input("Enter the number of rows you want for your board: "))
no_cols = int(input("Enter the number of coloumns you want for your board: "))
no_k = int(input("Enter the number for K you want for your board: "))

board=["0"*no_cols]*no_rows
freq_called = [0]*no_cols

print_board()

winner = 0
turn_no=1
while (winner == 0):
	place_marker(turn_no)
	print_board()
	turn_no = turn_no+1
	