
def pacman():
	"""Prints ASCII art for user.

	Inspired by https://www.reddit.com/r/Python/comments/9jnglb/im_really_bored_at_work/

	"""

	MAX_FOOD = 50
	MAX_LINE = 5

	# Ascii art
	FOOD = {'cherries': ['  ,', ' /|', 'O O'], \
	'bananas': ['   _      ', ' _ \\\'-_,# ', '_\\\'--\',\'`|', '\\`---`  / ', ' `----\'`  '], \
	'ghosts': [' .-. ', '| OO|', '|   |', '\'^^^\''], \
	'frightened ghosts': [' .-. ', '| ..|', '| ^^|', '\'^^^\''], \
	'pacman': [' .--. ', '/ _.-\'', '\\  \'-.', ' \'--\' '], \
	'ms. pacman': [' .M-. ', '/ _.-\'', '\\  \'-.', ' \'--\' '], \
	'pears': ['  (  ', ' / \\ ', '(   )', ' `"\' ']
	}


	def print_food(nfood, food):
		if nfood <= 0:
			input('I thought you said you were hungry? ')
		elif nfood > MAX_FOOD:
			input('That\'s way too much food ')
		else:
			while nfood > 0:
				if nfood > MAX_LINE:
					copies = MAX_LINE
				else:
					copies = nfood
				
				for i, line in enumerate(food):
					s = [line] * copies
					print('  '.join(s))
				
				nfood -= MAX_LINE



	hungry = True
	while hungry:
		uin = input('What food do you want? ')
		if uin in FOOD:
			food_ascii = FOOD[uin]
			uin = input(f'How many {uin} do you want? ')

			if not uin.isdigit():
				input('Give me a number next time >:( ')

			else:
				print_food(int(uin), food_ascii)

				valid = False
				while not valid:
					status = input('Are you still hungry? (y/n) ')
					if status == 'y':
						valid = True
					elif status == 'n':
						valid = True
						hungry = False
						print('Ok. Byeeeeeeee!')
					else:
						input('Seriously? This is a simple yes/no question :\\ ')

		elif uin == 'What do you have?':
			foods = list(FOOD.keys())
			foodstr = ', '.join(foods[:-1])
			foodstr = ''.join(['We have ', foodstr, ' and ', foods[-1], '.'])
			input(foodstr)

		else:
			input('I don\'t have that, try again.')


def main():
    pacman()

if __name__ == "__main__":
    main()







