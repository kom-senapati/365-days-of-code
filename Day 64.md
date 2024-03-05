## Day 64

Link: https://x.com/kom_senapati/status/1764859060266914292?s=20

### Approach:

- Created two arrays left and right to store minimum value from left to right and maximum value from right to left
- Using two pointer approach we find the maximum gap by maintaining ans var

### Code:

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        left = [A[0]] + [0] * (len(A)-1)
        right = [0] * (len(A)-1) + [A[-1]]
        for i in range(1, len(A)):
            left[i] = min(left[i-1], A[i])
        for j in range(len(A)-2, -1, -1):
            right[j] = max(right[j+1], A[j])
            
        l, r = 0, 0
        ans = 0
        while l < len(A) and r < len(A):
            if right[r] >= left[l]:
                ans = max(ans, r-l)
                r += 1
            else:
                l += 1
        return ans
```
