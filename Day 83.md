## Day 83

Link: https://x.com/kom_senapati/status/1771719931152719921?s=20

### Approach:

- If array contains atleast one even elements then the product of array is guaranteed to be even.
- So number of operations will be NC1 + NC2 +…..+ NCN = 2^N - 1.
- So used a for loop to calculate 2^len(A) with mod and converted to int and returned 2^N - 1

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        x = 1
        for i in range(len(A)):
            x = int((x*2) % (1e9+7))
        return x-1
```