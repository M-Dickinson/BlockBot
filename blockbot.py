from copy import deepcopy

def convertPiece(piece):
	root = (-1, -1)
	vectors = [(0, 0)]
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			if piece[i][j] != '.':
				if root != (-1, -1):
					vectors.append((j-root[1], root[0]-i))
				else:
					root = (i, j)
	return vectors

def checkLines(board):
	delRows = []
	for i in range(len(board)):
		delRow = True
		for j in board[i]:
			if j == '.':
				delRow = False
		if delRow:
			delRows.append(i)
	delCols = []
	for i in range(len(board[0])):
		delCol = True
		for j in range(len(board)):
			if board[j][i] == '.':
				delCol = False
		if delCol:
			delCols.append(i)

	for i in delRows:
		for j in range(len(board[i])):
			board[i][j] = 0
	for i in delCols:
		for j in board:
			j[i] = 0

def placePiece(board, piece, location):
	vectors = convertPiece(piece)
	placed = True
	try:
		for i in vectors:
			y = location[1] - i[1]
			x = location[0] + i[0]
			if board[y][x] != '.' or x < 0 or y < 0:
				placed = False
	except IndexError:
		placed = False
	if placed:
		for i in vectors:
			board[location[1] - i[1]][location[0] + i[0]] = '#'
		checkLines(board)
	return placed

def printBoard(board):
	for i in board:
		output = ''
		for j in i:
			output += j + ' '
		print(output.strip())

height = 8
width = 8
board = [['.' for i in range(height)] for j in range(width)]
numPieces = 3
"""
piece = [[1, 1, 1],
	 [1, 1, 1],
	 [1, 1, 1]]
placePiece(board, piece, (2, 2))

saveboard = deepcopy(board)

for i in range(height):
	for j in range(width):
		board = deepcopy(saveboard)
		placed = placePiece(board, piece, (i, j))
"""

while True:
	pieces = []
	while len(pieces) < numPieces:
		piece = []
		while True:
			piecerow = input("Enter peice " + str(len(pieces) + 1) + " data: ")
			if piecerow == 'x':
				break
			else:
				piece.append(piecerow.split())
		printBoard(piece)
		print()
		valid = input("Is this piece correct? (y/n): ")
		if valid == 'y':
			pieces.append(piece)
	for i in pieces:
		printBoard(i)
		print()

	restart = input("Continue? (y/n): ")
	if restart == 'n':
		break
