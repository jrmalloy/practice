def mergek(*args):
	import heapq # outside the function

	mins = []
	heapq.heapify(mins)
	merged = []

	for i,l in enumerate(args):
		heapq.heappush(mins, (l[0], i))

	i = [0]*len(args)


	while len(mins) > 0:

		n,l = heapq.heappop(mins)
		merged.append(n)

		i[l] += 1
		if i[l] < len(args[l]):
			heapq.heappush(mins, (args[l][i[l]], l))


	return merged



def check(truth, expected):
	if truth != expected:
		print('Failure: {truth}, {expected}'.format(truth=truth, expected=expected))


check(mergek...)

assert mergek([], [], []) == []