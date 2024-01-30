## Day 29

Link: https://x.com/kom_senapati/status/1752183692351746413?s=20

### Approach:

- Handled the edge cases (negetive int and zero)
- Else traversed from 2 to sqrt of A
- Took the log of A wrt M and if it was int returned 1
- At last returned 0

### Code:

```py
import math
class Solution:
	# @param A : integer
	# @return an integer
	def isPower(self, A):
        if A < 1 : return 0
        elif A == 1 : return 1
        for M in range(2, int(math.sqrt(A))+1):
            N = math.log(A,M)
            N = round(N,6)
            if math.ceil(N) == math.floor(N):return 1
        return 0
```
