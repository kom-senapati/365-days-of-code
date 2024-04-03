## Day 93

Link: https://x.com/kom_senapati/status/1775411433024667851?s=20

### Approach

- Pushed the current node to stack and set current = current.left until current wass None
- Poped the top item from the stack if current was None and the stack was not empty
- Appended the popped item into res and set current = popped_item.right 
- Go to step 3.
- If current is NULL and the stack is empty then we are done.

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
	# @return a list of integers
	def inorderTraversal(self, A):
        res = []
        current = A
        stack = []
        while 1:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                res.append(current.val)
                current = current.right 
            else:
                break
        return res
```
