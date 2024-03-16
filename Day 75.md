## Day 75

Link: https://x.com/kom_senapati/status/1768857229208256782?s=20

### Approach:

- Created a hash to store elements and their indices
- Iterated throught the given tuple and found the target
- If target was in hash returned them and added n to hash if it was not there
- If not returned earlier returned empty list

### Code:

```py
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
		hash = {}
		for i,n in enumerate(A, start=1):
			target = B - n
			if target in hash:
				return [hash[target], i]
			if n not in hash:
				hash[n] = i
		return []
```
