## Day 61

Link: https://x.com/kom_senapati/status/1763756171079418076?s=20

### Approach:

- Created vars for maintaining current arr(t) and sum(currSum) and required array and maxSum.
- Iterated through the array and added all the non negetive ints into t and also their sum in currSum
- If a negetive number or end of A is reached checked the conditions and updated res and maxSum and then emptied t and currSum set to 0
- Returned res 

### Code:

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i = 0
        res = []
        t = []
        maxSum = 0
        currSum = 0
        
        for j in range(len(A)):
            if A[j] >= 0:
                t.append(A[j])
                currSum += A[j]
                
            if A[j] < 0 or j==len(A)-1:
                if currSum > maxSum or (currSum == maxSum and len(t) > len(res)):
                    res = t
                    maxSum = currSum
                t = []
                currSum = 0
                i = j+1
        
        return res
```
