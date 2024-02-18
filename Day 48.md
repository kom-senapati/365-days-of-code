## Day 48

Link: https://x.com/kom_senapati/status/1759031461011661002?s=20

### Approach:

- Iterated through the array in reverse and updated all the digits till carry was there
- Even after iteration if carry is there inserted the carry at first pos
- Popped all the zeroes from the left side and returned the arr

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        for i in range(len(A) - 1, -1, -1): 
            carry += A[i]
            A[i] = carry % 10
            carry //= 10
            if carry == 0:
                break
        if carry:
            A.insert(0, carry)
        while len(A) > 1 and A[0] == 0:
            A.pop(0)
        return A
```
