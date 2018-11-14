

def circular_array(arr):
  # best algo is probably O(n) - checking if it's complete means checking if every element is included, so we can't avoid that

  # We can probably just jump through the array checking each element

  # keep track of which idxs were visited with a hashset
  visited = set([])
  idx = 0


  while idx not in visited:
    visited.add(idx)
    #compute new idx
    offset = arr[idx]
    idx += offset
    idx = idx % len(arr)

  return len(visited) == len(arr)



def reverseDigits(N):

  if N < 0:
    neg = True
    N = abs(N)
  else:
    neg = False

  num = 0
  while N > 0:
    num *= 10
    num += N%10
    N /= 10


  if neg:
    return -num
  else:
    return num


# Main Function
if __name__ == '__main__': 

	print reverseDigits(75)
	print reverseDigits(-75)
	print reverseDigits(12345)
	print reverseDigits(-54321)







