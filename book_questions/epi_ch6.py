
def p1_str2int(string):

	if len(string) == 0:
		print('Empty string')
		return

	digits = '0123456789'

	# check if string is negative
	if len(string) > 1 and string[0] == '-':
		is_neg = True
		string = string[1:]
	else:
		is_neg = False


	num = 0

	for ch in string:
		idx = digits.find(ch)
		if idx < 0:
			print('Illegal digit')
			return

		num *= 10
		num += idx

	if is_neg:
		return -num
	else:
		return num


def	test_p1_str2int():
	assert p1_str2int('1234') == 1234
	assert p1_str2int('-987') == -987
	assert p1_str2int('0') == 0
	assert p1_str2int('') == None
	assert p1_str2int('1234a') == None


def p1_int2str(num):

	digits = '0123456789'
	string = []

	# check if negative
	if num < 0:
		is_neg = True
		num = -num
	else:
		is_neg = False

	if not num:
		return '0'


	while num > 0:
		d = num % 10
		string.append(digits[d])
		num = num // 10


	if is_neg:
		string.append('-')

	string.reverse()

	return ''.join(string)


def test_p1_int2str():
	assert p1_int2str(1234) == '1234', p1_int2str(1234)
	assert p1_int2str(-987) == '-987', p1_int2str(-987)
	assert p1_int2str(0) == '0', p1_int2str(0)


def p3(column):

	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def get_mapping(ch):
		return alphabet.index(ch) + 1

	num = 0
	for ch in column:
		num *= len(alphabet)
		num += get_mapping(ch)

	return num


def test_p3():
	assert p3('A') == 1, p3('A')
	assert p3('AA') == 27, p3('AA')
	assert p3('ZZ') == 702, p3('ZZ')






if __name__ == '__main__': 
	test_p1_str2int()
	test_p1_int2str()
	test_p3()

