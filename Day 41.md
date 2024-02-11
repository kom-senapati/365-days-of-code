## Day 41

Link: https://x.com/kom_senapati/status/1756502961503535134?s=20

### Approach:

- Constructed a frequency array to track the occurrences of each character.
- Assessed the number of characters with odd occurrences.
- For even-length strings, returned 1 only if there were no characters with odd occurrences.
- For odd-length strings, returned 1 only if there was exactly one character with an odd occurrence count.

### Code:

```py
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        f = {}
        for c in A:
            f[c] = f.get(c,0) + 1
        
        o = 0
        for count in f.values():
            if count % 2 != 0:
                o += 1
        
        if len(A) % 2 == 0:
            return 1 if o == 0 else 0
        else:
            return 1 if o == 1 else 0
```
