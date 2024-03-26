## Day 85

Link: https://x.com/kom_senapati/status/1772456472720413028?s=20

### Approach:

- Made a result array to store answer of all the queries
- for each query, initialised res var and iterated through A and updated res if found any element greater than b, then appended it to result
- atlast returned result

### Code:

```py
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []
        
        for b in B:
            res = -1
            
            for j in range(len(A)):
                if A[j] >= b:
                    res = j
                    break
            
            result.append(res)
        
        return result
```