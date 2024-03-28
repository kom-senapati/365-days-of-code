## Day 87

Link: https://x.com/kom_senapati/status/1773177328123642072?s=20

### Approach:

- At least we can select maximum frequency of an element subarrays to delete
- So created a freq dict and returned max value of frequencies in the dict

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        f = {}
        for n in A:
            f[n] = f.get(n, 0) + 1
        return max(f.values())
```