
class Cipher:
	def __init__(self, alphabet):
	"""
	alphabet: tuple, list, or string
	"""
	self.alphabet = alphabet


class ShiftCipher(Cipher):

	def decrypt(cipherText):

		for shift in range(len(alphabet)):
			ans = ''
			for i in range(len(teststr)):
				j = (alphabet.find(teststr[i]) + shift) % len(alphabet)
				ans += alphabet[j]

			print 'String with shift=',shift, ':',ans
			issolved = raw_input('Is this broken? (y/n)')
			if issolved=='y': break


class AffineCipher(Cipher):

	def decrypt(cipherText,alpha):
		for shift in range(len(alphabet)):
			ans = ''
			for i in range(len(teststr)):
				j = (alpha*(alphabet.find(teststr[i]) - shift)) % len(alphabet)
				ans += alphabet[j]

			print 'String with b=',shift, ':',ans
			issolved = raw_input('Is this broken? (y/n)')
			if issolved=='y': break


class PermutationCipher(Cipher):

	def __init__(self,key=()):
		self.key = key


	def decrypt(cipherText,keyLen):
		from itertools import permutations

		keylist = list(permutations(range(keyLen)))
		trykeys = keylist

		# filter based on guesses
		#trykeys = [l for l in trykeys if l == (3,0,5,1,6,2,7,4)]
		
		finalkey = -1
		for key in trykeys:
			print 'Key:',key
			ans = ''
			for j in range(len(cipherText)/keyLen):
				for i in range(keyLen):
					ans += cipherText[j*keyLen + key[i]]

			issolved = raw_input(ans)
			if issolved=='y':
				finalkey = key
				break

		if finalkey: print 'Key found:', finalkey




