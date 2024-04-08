## Day 98

Link: https://x.com/kom_senapati/status/1777230273610203303

### Approach

- Transposed the matrix
- Then reversed the rows of matrix

### Code

```py
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(len(A)):
            A[i] = A[i][::-1]
        return A
```
