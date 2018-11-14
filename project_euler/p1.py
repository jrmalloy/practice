


def sumMultiples(n):

  multiples = set([])

  x = 1

  while x*3 < n:
    multiples.add(x*3)
    x+=1

  x = 1

  while x*5 < n:
    multiples.add(x*5)
    x+=1

  return sum(multiples)


def fibonacci(limit, x=0, y=1, evensum=0):
	"""
	Given two integers x and y, returns the next number in the fibonacci sequence, up until limit value
	"""
	z = y+x

	if z >= limit:
		return evensum

	elif z%2 == 0:
		evensum += z

	return fibonacci(limit, y, z, evensum)


def largestPrimeFactor(n):

	"""
	finds the largest prime factor of n
	"""
	import math

	maxPrime = 1
	i = 2
	x = math.sqrt(n)

	while i <= x:
		# while i divides n, divide by i
		while not n%i:
			n /= i
			maxPrime = max(maxPrime,i)
			print i

		i += 1

	return max(maxPrime,n)


def numPalindrome(x):

	numlist = []

	# separate into digits
	while x > 0:
		numlist.append(x%10)
		x /=10

	# check if palindrome
	for i in range(len(numlist)/2):
		if numlist[i] != numlist[-(i+1)]:
			return False

	return True








