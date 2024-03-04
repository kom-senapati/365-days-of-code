## Day 63

Link: https://x.com/kom_senapati/status/1764630191614443825?s=20

### Approach:

- Sorted the given array of strs
- Made two vars for shortest and longest string
- Iterated and found the largest common prefix between them

### Code:

```py
class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        if len(A) == 0:
            return ""
        A.sort()
        f,l = A[0], A[-1]
        c = 0
        while c < len(f) and f[c] == l[c]:
            c += 1
        return f[:c]
```
