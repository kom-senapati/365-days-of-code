## Day 33

Link: https://x.com/kom_senapati/status/1753621026834165935?s=20

### Approach:

- `(A + C - 1)` calculates the position of the Ath item starting from position C.
- `% B` ensures that the position is within the circle of size B.

### Code:

```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return (A+C-1) % B
```
