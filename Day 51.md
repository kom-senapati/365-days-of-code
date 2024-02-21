## Day 51

Link: https://x.com/kom_senapati/status/1760279210260603214?s=20

### Approach:

- Initialized arr with a single digit
- Multiplied digits with consecutive integers, handling carry if any
- Iterated through the arr to form the res
- Ensured the function directly returns 2 if A equals 2
- Correctly calculated the factorial by looping from 2 to A

### Code:

```py
class Solution:
    # @param A : integer
    # @return a strings
    def multiply(self, arr, i):
        carry = 0
        for x in range(len(arr)):
            product = arr[x] * i + carry
            arr[x] = product % 10
            carry = product // 10
        while carry:
            arr.append(carry % 10)
            carry //= 10

    def solve(self, A):
        if A == 2:
            return 2
        arr = [1]
        for i in range(2, A+1):
            self.multiply(arr, i)
        res = 0
        for d in reversed(arr):
            res = res * 10 + d
        return res
        
```
