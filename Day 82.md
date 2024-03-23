## Day 82

Link: https://x.com/kom_senapati/status/1771364476836610240?s=20

### Approach:

- Initialised two pointers l and r
- Performed binary search , calculated the middle index and checked if element at that pos is less/equal to B, if it was set l = mid+1 else r = mid-1
- Atlast returned l

### Code:

```py
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] <= B:
                l = mid + 1
            else:
                r = mid - 1
        return l
```