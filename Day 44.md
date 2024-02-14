## Day 44

Link: https://x.com/kom_senapati/status/1757610805388779950?s=20

### Approach:

- Created the frequency dict
- converted that into list of tuples and sorted them on basis of array
- got those counts in result and returned

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        f = {}
        for n in A:
            f[n] = f.get(n, 0) + 1

        result = [count for n, count in sorted(f.items(), key=lambda x: x[0])]

        return result
```
