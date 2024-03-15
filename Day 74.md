## Day 74

Link: https://x.com/kom_senapati/status/1768643695262179655?s=20

### Approach:

- Checked if any sign is provided or not
- Iterated through the given string and added that char to number if it was a digit else broke loop
- If anytime the overflow or underflow occurs extremes are returned
- atlast returned number (if not returned earlier)

### Code:

```py
class Solution:
	# @param A : string
	# @return an integer
	def atoi(self, A):
		A = A.strip()
        if not A:
          return 0
    
        sign = -1 if A[0] == '-' else 1
        if A[0] in {'-', '+'}:
          A = A[1:]
    
        num = 0
    
        for c in A:
          if not c.isdigit():
            break
          num = num * 10 + ord(c) - ord('0')
          if sign * num <= -2**31:
            return -2**31
          if sign * num >= 2**31 - 1:
            return 2**31 - 1
    
        return sign * num
```
