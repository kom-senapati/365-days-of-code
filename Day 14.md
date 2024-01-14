## Day 14

Link: https://x.com/kom_senapati/status/1746670151616037272?s=20

### Approach:

- a[i+b] was used for accessing the num and appending to ret
- Changed it to a[(i+b)%len(a)] for rotating operation

### Code:

```python
class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        for i in xrange(len(a)):
            ret.append(a[(i + b)%len(a)])
        return ret
```