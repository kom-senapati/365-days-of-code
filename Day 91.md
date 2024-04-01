## Day 91

Link: https://x.com/kom_senapati/status/1774630102380523748?s=20

### Approach:

- Initialised a count variable
- Incremented it if bit was set and right shifted A
- Returned count at last

### Code:

```py
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A:
            if (A&1):
                count += 1
            A >>= 1
        return count
```