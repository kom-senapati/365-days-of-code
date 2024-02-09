## Day 39

Link: https://x.com/kom_senapati/status/1755873096119034039?s=20

### Approach:

- found the log2 of the given number
- checked if it was greater than 0 and is integer and returned 1,0 appropriately

### Code:

```py
class Solution:
	# @param A : string
	# @return an integer
	def power(self, A):
        import math
        i = math.log2(int(A))
        return int(i>=1 and i.is_integer())
```
