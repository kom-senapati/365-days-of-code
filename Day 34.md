## Day 34

Link: https://x.com/kom_senapati/status/1754005399215440206?s=20

### Approach:

- Checked if A falls in range [0,26] if it fell returned corresponding char
- else used a while loop to calculate current letter and added to result and updated A

### Code:

```py
class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
        if A <= 26:
            return chr(ord('A') + A - 1)
        
        result = ''
        while A > 0:
            remainder = (A - 1) % 26
            result = chr(ord('A') + remainder) + result
            A = (A - 1) // 26
        
        return result
```
