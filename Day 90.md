## Day 90

Link: https://x.com/kom_senapati/status/1774254803604078862?s=20

### Approach:

- Initialised a stack and pushed all the chars of A onto it
- While stack was not empty added the char popped from stack to reversedString var
- Atlast returned it

### Code:

```py
class Solution:
	# @param A : string
	# @return a strings
	def reverseString(self, A):
		stack = []
		for c in A:
			stack.append(c)
		reversedString = ""
		while stack:
			reversedString += stack.pop()
		return reversedString
```