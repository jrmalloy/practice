def p1(A, i):
	# swap pivot to end of array
	pivot = A[i]

	A[-1], A[i] = A[i], A[-1]

	# iterate through whole array, swapping smaller values to the front
	low = -1
	for i, val in enumerate(A[:-1]):
		if A[i] < pivot:
			low += 1
			A[low], A[i] = A[i], A[low]

	# move pivot to be right after end of low partition
	low = low + 1
	A[low], A[-1]  = A[-1], A[low]


	# iterate from pivot to end of array, moving equal vals to the "front"
	for i in range(low + 1, len(A)):
		if A[i] == pivot:
			low += 1
			A[low], A[i] = A[i], A[low]

	return A


def test_p1():
	print(p1([5,9,8,2,6,4,2,7,3,5,1], 0))
	print(p1([1,2,3,1,2,3], 0))
	print(p1([1,2,3,1,2,3], 1))
	print(p1([1,2,3,1,2,3], 2))
	print(p1([1], 0))
	print(p1([3,2], 0))
	print(p1([2,1], 1))
	print(p1([2,2], 1))



def p2(A):

	for i in reversed(range(len(A))):
		A[i] += 1
		if A[i] < 10:
			break

		A[i] = 0

	if A[0] == 0:
		A[0] = 1
		A.append(0)


	return A

def test_p2():
	print(p2([2,1]))
	print(p2([2,1,9]))
	print(p2([2,1,9,9,9,9]))
	print(p2([9,9,9]))



def p17(arr):

	def hasDuplicate(subarr):
		return any((x>1 for x in subarr))



	for i in range(9):
		nfr = [0]*10
		nfc = [0]*10
		nfs = [0]*10

		# check row
		for j in range(len(arr[i])):
			nfr[arr[i][j]] += 1
			nfc[arr[j][i]] += 1

		sqi = (i//3)*3
		sqj = (i%3)*3

		for m in range(3):
			for n in range(3):
				nfs[arr[sqi+m][sqj+n]] += 1


		if any([hasDuplicate(nfs[1:]), hasDuplicate(nfc[1:]), hasDuplicate(nfr[1:])]):
			return False

	return True


def test_p17():
	arr = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]]

	print(p17(arr))

	arr = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,5,0,0,0,5,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]]

	print(p17(arr))

	arr = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,5,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,5,0,0],
	[0,0,0,0,0,0,0,0,0]]

	print(p17(arr))

	arr = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,5,0,0],
	[0,0,0,0,0,0,0,5,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]]

	print(p17(arr))

	arr = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,5,4,6],
	[0,0,0,0,0,0,1,8,7],
	[0,0,0,0,0,0,3,2,9],
	[0,0,0,0,0,0,0,0,0],
	[8,7,5,4,3,2,6,9,1],
	[0,0,0,0,0,0,0,0,0]]

	print(p17(arr))

	arr = [[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,5,4,6],
	[0,0,5,0,0,0,1,8,7],
	[0,0,0,0,0,0,3,2,9],
	[0,0,0,0,0,0,0,0,0],
	[8,7,5,4,3,2,6,9,1],
	[0,0,0,0,0,0,0,0,0]]

	print(p17(arr))






def p20(rows):
	def compute_row(prev):
		r = [1,]
		for i in range(len(prev) - 1):
			s = prev[i] + prev[i + 1]
			r.append(s)

		r.append(1)

		return r

	triangle = []
	triangle.append([1])

	for i in range(rows):
		nr = compute_row(triangle[i])
		triangle.append(nr)


	return triangle


# Main Function
if __name__ == '__main__': 
	#test_p2()
	test_p1()















