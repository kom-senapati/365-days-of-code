## Day 62

Link: https://x.com/kom_senapati/status/1764119229521961261?s=20

### Approach:

- Converted both binary strings to int and then added them and converted to binary string and returned

### Code:

```py
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
		return bin(int(A, 2)+int(B, 2))[2:]
```
