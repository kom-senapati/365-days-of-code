## Day 54

Link: https://x.com/kom_senapati/status/1761239110084112792?s=20

### Approach:

- Counted how many times 1 occur in array
- Then made an array with that much 1s in right side and other 0s and returned it

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ones = A.count(1)
        return [0] * (len(A) - ones) + [1] * ones
```
