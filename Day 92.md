## Day 92

Link: https://x.com/kom_senapati/status/1775053905166209267?s=20

### Approach

- Created a var i and iterated through A
- If the element of i and j were not same incremented i and swapped them
- Atlast returned i+1

### Code

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 1:
            return 1
        i = 0
        for j in range(len(A)):
            if A[i] != A[j]:
                i+=1
                A[i] = A[j]
        return i+1
```
