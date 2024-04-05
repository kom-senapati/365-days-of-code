## Day 95

Link: https://x.com/kom_senapati/status/1776140776428179813?s=20

### Approach

- Recursively check that if node's value falls in the range defined by its ancestors

### Code

```py
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
		
		def isBSTUtil(A, mini, maxi):
			if not A:
				return 1
			if A.val < mini or A.val > maxi:
				return 0
			
			return isBSTUtil(A.left, mini, A.val - 1) \
				and isBSTUtil(A.right, A.val+1, maxi)
		
		return isBSTUtil(A, float("-inf"), float("inf"))
```
