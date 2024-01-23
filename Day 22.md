## Day 22

Link: https://x.com/kom_senapati/status/1749606970003521689?s=20

### Approach:

- Calculated the total by adding the number of possible squares towards top-right, top-left, bottom-right, bottom-left
- Returned total

### Code:

```python
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        total=min(8-B,A-1)+min(A-1,B-1)+min(B-1,8-A)+min(8-A,8-B);
        return total;
```
