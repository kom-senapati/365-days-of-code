## Day 42

Link: https://x.com/kom_senapati/status/1757070710080413955?s=20

### Approach:

- Sorted the array
- Then changed the length if it was odd
- Then iterated till that with skipping 1 value
- while iteration swapped those 2 values

### Code:

```py
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
        A.sort()
        n=len(A)
        if n%2:n-=1
        for i in range(0,n,2):
            A[i],A[i+1] = A[i+1],A[i]
        return A
```
