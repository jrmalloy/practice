import random

class Selection:
	UNMARKED = 1
	CLEARED = 2
	FLAGGED = 3



class Board:
	def __init__(self, height = 9, width = 10, n_mines = 8):
		self.height = height
		self.width = width
		self.n_mines = n_mines
		self.board = [[]]
		self.create_board()

	def create_board(self):
		"""Creates board state for minesweeper game.

		Args:
			x (int): Number of rows in board. 
			y (int): Number of columns in board.
			n_mines (int): Number of mines in board

		"""

		def populate_mines():
			deck = list(range(self.width * self.height))
			random.shuffle(deck)

			mine_list = []

			for i in range(self.n_mines):
				loc = deck.pop()
				r, c = self.convert_to_xy(loc)
				mine_list.append((r,c))
				self.board[r][c] = -1

			surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
			while mine_list:
				mr, mc = mine_list.pop()
				# increment board around mine
				for loc in surrounding:
					nr = mr + loc[0]
					nc = mc + loc[1]
					if self.is_in_bounds(nr, nc) and not self.get_space(nr, nc) < 0:
						self.board[nr][nc] += 1



		self.board = [[0] * self.width for _ in range(self.height)]
		populate_mines()


	def convert_to_xy(self, i):
		"""Converts single index into (row, col)."""
		row = i // self.width
		col = i % self.width

		return (row, col)


	def get_board(self):
		return self.board

	def get_space(self, row, col):
		return self.board[row][col]

	def is_in_bounds(self, row, col):
		return row >= 0 and row < self.height \
					and col >= 0 and col < self.width

	def is_empty(self, row, col):
		return not self.board[row][col]


class Minesweeper:

	def __init__(self, height = 9, width = 10, n_mines = 8):
		self.mine_board = Board(height, width, n_mines)
		self.is_loss = False
		self.height = height 
		self.width = width
		self.mines = n_mines
		self.cleared = 0
		self.select_board = [[Selection.UNMARKED] * self.width for _ in range(self.height)]



	def play(self):

		def get_user_input():
			picked = input('Pick a square (row,col): ')
			picked.replace(' ', '')
			row, col = picked.split(',')
			if row.isdigit() and col.isdigit() \
			and self.mine_board.is_in_bounds(int(row), int(col)):
					return (int(row), int(col))
			else:
				print('Invalid input. Please enter input as follows: row,col')
				return get_user_input()


		self.display_board()

		while not self.is_win() and not self.is_loss:
			row, col = get_user_input()
			self.select(row, col)
			self.display_board()

		if self.is_win():
			print('You win! :D')
		else:
			print('You lose :(')




	def select(self, row, col):
		stat = self.select_board[row][col]

		if stat == Selection.FLAGGED: 
			self.select_board[row][col] = Selection.UNMARKED
		elif stat == Selection.UNMARKED:
			self.select_board[row][col] = Selection.CLEARED

		if self.mine_board.get_space(row, col) < 0:
			self.is_loss = True
		else:
			self.cleared += 1


	def is_win(self):
		board_size = self.height * self.width
		return not self.is_loss and self.cleared == (board_size - self.mines)


	def display_board(self):
		"""Prints the current board state to the console."""

		for r in range(self.height):
			line = ['|']
			for c in range(self.width):
				if self.select_board[r][c] == Selection.UNMARKED:
					line.append(' ')
				elif self.select_board[r][c] == Selection.CLEARED:
					space = self.mine_board.get_space(r,c)
					if space < 0:
						line.append('X')
					else:
						line.append(str(space))
				else:
					line.append('F')

				line.append('|')

			print(''.join(line))




if __name__ == "__main__":
    game = Minesweeper()
    game.play()



		
