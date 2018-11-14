
import math

class BstNode:
	def __init__(self, data = None, left = None, right = None):
		self.data, self.left, self.right = data, left, right


def is_bst(tree):

	def helper(tree, lo, hi):

		if tree == None or tree.data == None:
			return True

		num = tree.data

		# check if in range
		if lo <= num <= hi:
			return False
		else:
			return helper(tree.left, lo, num) and helper(tree.right, num, hi)

	return helper(tree, -math.inf, math.inf)



