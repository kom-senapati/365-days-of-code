## Day 86

Link: https://x.com/kom_senapati/status/1772816923371217191?s=20

### Approach:

- Checked if length of A was in range [8,15]
- Created flags for lower, upper, special, and numeric character
- Iterated through the A and updated if found any
- Returned the and result of all these flags

### Code:

```py
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) > 15 or len(A) < 8:
            return 0
        special = '@#%&!$*'
        l=u=s=d=0
        for c in A:
            if c.isupper():u=1
            if c.islower():l=1
            if c.isdigit():d=1
            if c in special:s=1
        return l and u and s and d
```