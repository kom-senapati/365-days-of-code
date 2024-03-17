## Day 76

Link: https://x.com/kom_senapati/status/1769194507017273501?s=20

### Approach:

- Created indices dict to store the element with their indices
- Also result and min_index to store the first repeating element
- Iterated through the arr to check if the element was in dict and its index is smaller than min_index and updated else put into the dict
- Atlast returned the result

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        indices = {}
        min_index = float('inf')
        result = -1
        for i, n in enumerate(A):
            if n in indices:
                if indices[n] < min_index:
                    min_index = indices[n]
                    result = n
            else:
                indices[n] = i
        return result
```
