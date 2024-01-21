## Day 20

Link: https://x.com/kom_senapati/status/1748918465967370474?s=20

### Approach:

- Solved the indentation error
- Then added an if statement for edge cases

### Code:

```python
class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A<2:return 0
        upperLimit = int(A**0.5)
        for i in xrange(2, upperLimit + 1):
            if i < A and A % i == 0:
                return 0
        return 1
```
