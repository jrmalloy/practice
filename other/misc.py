
def reverse_str(s):
	"""Given a string, reverse in place.
	"""

	swap_i = len(s) - 1

	for i in range(len(s) // 2):
		s[i], s[swap_i] = s[swap_i], s[i]
		swap_i -= 1

	return s


def test_reverse_str():
	assert reverse_str('') == ''
	assert reverse_str('abc') == 'cba'
	assert reverse_str('abcd') == 'dcba'


if __name__ == '__main__': 
	test_reverse_str()