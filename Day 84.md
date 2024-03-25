## Day 84

Link: https://x.com/kom_senapati/status/1772068036733702603?s=20

### Approach:

- Total items = B, Total items can be sold in a week = A*5
- So returned the ceil value of number of weeks

### Code:

```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        import math
        return math.ceil(B / (A*5))
```