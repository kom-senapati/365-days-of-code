## Day 79

Link: https://x.com/kom_senapati/status/1770474743818293754?s=20

### Approach:

- Created a frequency dict of A
- Iterated through the dict to find and return element having frequency more than floor(N/2)

### Code:

```py
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        N = len(A)
        
        d = {}
        for n in A:
            d[n] = d.get(n,0) + 1
            
        for n,f in d.items():
            if f > N//2:
                return n
```