## Day 1
Link: https://x.com/KomSenapati/status/1742021807790764499?s=20
### Approach:
- Split the string
- Reverse the array of words
- join them

### Code:
```python
class Solution:
    def solve(self,A):
        return " ".join(A.split()[::-1])
```