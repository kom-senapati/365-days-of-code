## Day 45

Link: https://x.com/kom_senapati/status/1758112038465782070?s=20

### Approach:

- Initialised carry and res vars, and i,j vars for indices of A,B
- Iterated through A,B in reverse and found the current digit and updated the carry as well as res array
- Appended the carry if it existed
- Returned the reversed res

### Code:

```py
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):
        carry = 0
        res = []
        i, j = len(A) - 1, len(B) - 1
        
        while i >= 0 or j >= 0:
            n = carry
            if i >= 0:
                n += A[i]
                i -= 1
            if j >= 0:
                n += B[j]
                j -= 1
            res.append(n % 10)
            carry = n // 10
        
        if carry:
            res.append(carry)
        
        return res[::-1]
```
