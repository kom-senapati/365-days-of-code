## Day 88

Link: https://x.com/kom_senapati/status/1773557886355968291?s=20

### Approach:

- Found out the mean, and then variance 
- Returned the variance rounded upto 2 decimal places

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        mean = sum(A) / len(A)
        variance = sum((x-mean)**2 for x in A) / len(A)
        return round(variance, 2)
```