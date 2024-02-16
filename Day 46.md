## Day 46

Link: https://x.com/kom_senapati/status/1758421044002513162?s=20

### Approach:

- Initialised the sum of first B ints
- Then iterated the array using i (B-1 to 0) and j (from end to start) pointers
- Adjusted the sum and checked if it was greater
- Returned the ans

### Code:

```py
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        sum_val = sum(A[:B])
        i = B - 1
        ans = sum_val
        
        for j in range(n - 1, n - 1 - B, -1):
            sum_val = sum_val - A[i] + A[j]
            ans = max(ans, sum_val)
            i -= 1
        
        return ans
```
