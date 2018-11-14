

def birthdayProb(n, d):
	"""
	n: number of people/data points
	d: number of unique values

	Computes probability of a collision given
	n people and d values. For classic birthday
	problem, d=365 days and probability is 50%
	when n=23.
	"""

	if n > d: return 1

	p = 1.0
	for i in range(n):
		m = 1.0 - (float(i)/float(d))
		p *= m

	return 1.0-p



