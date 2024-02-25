## Day 55

Link: https://x.com/kom_senapati/status/1761590193994231949?s=20

### Approach:

- If A was 0 returned empty array
- Created res array with 1 as first entry
- Iterated A-1 times to create the other rows
- Added 0s at both ends and then created the new row as sum of consecutive values of old row
- appended the row to res and atlast returned res

### Code:

```py
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0: return []
        res = [[1]]
        for i in range(A-1):
            t = [0] + res[-1] + [0]
            row = []
            for j in range(len(t)-1):
                row.append(t[j+1] + t[j])
            res.append(row)
        return res
```
