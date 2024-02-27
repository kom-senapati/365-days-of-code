## Day 57

Link: https://x.com/kom_senapati/status/1762325672695922714?s=20

### Approach:

- sorted the array A
- Iterated through the arr and got the supposed count of elements greater than p and removed count of duplicates
- Then checked if they were equal returned 1
- If iteration over returned -1

### Code:

```py
class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n):
            count_greater = n - i - 1
            j = i+1
            while(j<n and A[i] == A[j]):
                count_greater-= 1
                j+=1

            if count_greater == A[i]:
                    return 1
        return -1
```
