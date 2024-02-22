## Day 52

Link: https://x.com/kom_senapati/status/1760696848501575714?s=20

### Approach:

- Created empty row
- Appended the corresponding binomial coefficients
- returned the row

### Code:

```py
class Solution:
    # @param A : integer
    # @return a list of integers
    def coeff(self, n, k):
        import math
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    def getRow(self, A):
        row = []
        for i in range(A + 1):
            row.append(self.coeff(A, i))
        return row
```
