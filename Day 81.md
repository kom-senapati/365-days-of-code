## Day 81

Link: https://x.com/kom_senapati/status/1771029795003895887?s=20

### Approach:

- Created two max and two min variables to store maximum and minimum values for A[i]+i and A[i]-i
- Iterated through the array and upated these
- At last returned max of (A[i]+i-A[j]-j, A[i]-i+A[j]+j)

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = max2 = float("-inf")
        min1 = min2 = float("inf")
        
        for i,n in enumerate(A):
            max1 = max(max1, n+i)
            max2 = max(max2, n-i)
            
            min1 = min(min1, n+i)
            min2 = min(min2, n-i)
        
        return max(max1-min1, max2-min2)
```