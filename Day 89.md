## Day 89

Link: https://x.com/kom_senapati/status/1773910100820034009?s=20

### Approach:

- Initialised res and iterated through the string A
- If it was a digit, extracted the full number and added it to res
- Returned res

### Code:

```py
class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        res = 0
        i = 0
        while i < len(A):
            if A[i].isdigit():
                j = i
                n = 0
                while j < len(A) and A[j].isdigit():
                    n = n * 10 + int(A[j])
                    j += 1
                res += n
                i = j
            else:
                i += 1
        return res
```