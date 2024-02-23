## Day 53

Link: https://x.com/kom_senapati/status/1761002269946831204?s=20

### Approach:

- Created hashMap hash
- Iterated through the array and updated the number's count and also returned it if its appearance was above N/3
- If the loop ended returned -1

### Code:

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        hash = {}
        N = len(A)
        for n in A:
            hash[n] = hash.get(n, 0) + 1
            if hash[n] > N//3:
                return n
        return -1
```
