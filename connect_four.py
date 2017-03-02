#A game of connect four in python :D
#so idk what is happening
#connect k by n by m board:

# if i use
#
#
#
#
#
#


def print_board():
	for i in range(0, no_rows):
		print(board[i])
	print("\n")
		
def place_marker():
	place_col = int(input("Enter the the index of the coloumn you want to place your marker in: "))
	place_row = int(input("Enter the the index of the row you want to place your marker in: "))
	
	marker = "A"
	digit = ([int(str(board[place_col])) //10**(no_cols-place_col)]%10)
	
	if digit == "A" or digit =="B":
		turn_no = turn_no-1
		print("There is already a marker there. Please place it somewhere else....")
	
	board[place_col] = board[place_col][:(place_row-1)] + marker + board[place_col][place_row:]
	
def real_check_for_win():
	checker = possible_win[0]
	check_count = 0
	for i in range(0, no_k+1):
		if possible_win[i] == checker:
			check_count = check_count+1
	if check_count == no_k:
		winner=1
	else:
		winner=0
	
def check_win():
	possible_win = []*no_k
	for i in range(0, no_k+1):
		possible_win[i] = [int(board[place_col]) //10**((no_cols-place_col)+i)]%10
	real_check_for_win()
	for i in range(0, no_k):
		possible_win[i] = [int(board[place_col+i]) //10**(no_cols-place_col)]%10
	real_check_for_win()
	
no_rows = int(input("Enter the number of rows you want for your board: "))
no_cols = int(input("Enter the number of coloumns you want for your board: "))
no_k = int(input("Enter the number for K you want for your board: "))

board=["0"*no_cols]*no_rows

print_board()

winner = 0

while (winner == 0):

	place_marker()
	print_board()
	check_win()




