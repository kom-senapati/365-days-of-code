## Day 94

Link: https://x.com/kom_senapati/status/1775769588866957738?s=20

### Approach

- Initialised x var with first value of A
- Did xor of all the elements of A via x
- Returned x

### Code

```py
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
        x = A[0]
        for n in A[1:]:
            x ^= n
        return x
```
