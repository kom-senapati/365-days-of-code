## Day 59

Link: https://x.com/kom_senapati/status/1763198678959833344?s=20

### Approach:

- Initialized a res array
- Traversed through the upper diagonal start and then moved down anti-diagonaly and appended the results respectively
- Traversed through the lower diagonal start and then moved down anti-diagonaly and appended the results respectively
- Returned res

### Code:

```py
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        res = []

        for x in range(n):
            curr = []
            i = 0
            j = x
            while j >= 0:
                curr.append(A[i][j])
                i += 1
                j -= 1
            res.append(curr)

        for x in range(1, n):
            curr = []
            i = x
            j = n - 1
            while i < n:
                curr.append(A[i][j])
                i += 1
                j -= 1
            res.append(curr)
        return res
```
