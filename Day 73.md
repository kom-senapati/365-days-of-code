## Day 73

Link: https://x.com/kom_senapati/status/1768259905566220369?s=20

### Approach:

- Created rtoi dict and res var
- Iterated through the given string and checked if current char is smaller than next char and subtracted its value else added its value
- Atlast returned res

### Code:

```py
class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(self, A):
		rtoi = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        for i,c in enumerate(A):
            if (i+1) < len(A) and rtoi[c] < rtoi[A[i+1]]:
                res -= rtoi[c]
            else:
                res += rtoi[c]
        return res
```
