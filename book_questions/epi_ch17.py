import math

def p17(tasks):

	assignments = set([]) # set of tuples (task1, task2)
	largest_sum = (0,0)
	min_task = math.inf # min element in largest task


	for t in tasks:
		if t < min_task:
			assignments.discard(largest_sum)
			new_t = (sum(largest_sum) - min_task, t)
			




