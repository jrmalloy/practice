
def binarySearch(num, arr):
	start = 0
	end = len(arr)-1
	check = (start + end)/2
	
	print "start = ", start
	print "end = ", end
	print "check = ", check, "\n"

	while arr[check] != num:
		if arr[check] < num:
			start = check + 1
		else:
			end = check - 1

		if end < start:
			return -1

		check = (start + end)/2
		print "start = ", start
		print "end = ", end
		print "check = ", check, "\n"

	return check



def mergeSort(arr):

	# base case
	if len(arr) > 1:
		midpt = len(arr)/2
		arr = merge(mergeSort(arr[:midpt]), mergeSort(arr[midpt:]))
		
	return arr


# merging two sorted lists
def merge(arr1, arr2):
	merged = []
	while arr1 and arr2:
		if arr1[0] > arr2[0]:
			merged.append(arr2[0])
			arr2 = arr2[1:]
		elif arr1[0] < arr2[0]:
			merged.append(arr1[0])
			arr1 = arr1[1:]
		else:
			merged.append(arr1[0])
			merged.append(arr2[0])
			arr1 = arr1[1:]
			arr2 = arr2[1:]

	merged.extend(arr1)
	merged.extend(arr2)

	return merged



def quickSort(arr,lo,hi):
	if lo < hi:
		p = partition(arr,lo,hi)
		quickSort(arr,lo,p-1)
		quickSort(arr,p+1,hi)
	
	return arr

def partition(arr,lo,hi):

	def swap(arr, a, b):
		temp = arr[a]
		arr[a] = arr[b]
		arr[b] = temp
		return arr

	pivot = arr[hi]
	print "pivot=",pivot
	i = lo - 1
	for j in range(lo,hi):
		if arr[j] < pivot:
			i+= 1
			arr = swap(arr,i,j)

	arr = swap(arr,i+1,hi)
	print arr

	return i+1










if __name__ == '__main__':
	ans = binarySearch(-5,[1,2,3,4,5,8,9,11,12,13,15,16,17,19,21])
	print "ans=", ans

