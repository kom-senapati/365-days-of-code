## Day 72

Link: https://x.com/kom_senapati/status/1767903550036746457?s=20

### Approach:

- Created itor list of entries of respective number and its roman conversion
- Created res var, iterated through itor
- If A was divisble by the number then updated res and A
- at last returned res

### Code:

```py
class Solution:
	# @param A : integer
	# @return a strings
	def intToRoman(self, A):
        itor = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), 
        (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), 
        (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        
        res = ""
        
        for i,r in reversed(itor):
            if A // i:
                res += r * (A//i)
                A = A % i
        
        return res
```
