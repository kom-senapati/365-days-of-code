## Day 32

Link: https://x.com/kom_senapati/status/1753264185457459698?s=20

### Approach:

- Checked the sign of integer and appropriately reversed it
- Checked if it was in range of 32-bit integer else returned 0

### Code:

```py
class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
        if A < 0:
            reversed_num = -int(str(-A)[::-1])
        else:
            reversed_num = int(str(A)[::-1])

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        else:
            return reversed_num
```
