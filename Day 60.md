## Day 60

Link: https://x.com/kom_senapati/status/1763533515813961732?s=20

### Approach:

- Created two arrays mx (prefix max array) and mn (suffix min array) and filled them using 2 separate loops.
- Iterated through the array A from index 1 to n-1, checking if A[i] was greater than elements to left and lesser than elements to right and if it was not equal to suffix min.
- If an element is found that meets the criteria, returned 1. Otherwise, returned 0 after iterating through the entire array.

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)
        mx,mn = [0]*n, [0]*n
        
        mx[0] = A[0]
        mn[n-1] = A[n-1]
        
        for i in range(1,n):
            mx[i] = max(mx[i-1], A[i])
        
        for i in range(n-2,-1,-1):
            mn[i] = min(mn[i+1], A[i])
        
        for i in range(1,n-1):
            if mx[i-1] < A[i] and mn[i+1] > A[i] and A[i] != mn[i+1]:
                return 1
        
        return 0
```
