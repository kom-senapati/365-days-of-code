## Day 35

Link: https://x.com/kom_senapati/status/1754493012791398544?s=20

### Approach:

- Using Euclidean algorithm
- if B is 0 then returning A else gcd(B,A%B) (using recursion)

### Code:

```py
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
        if B == 0: return A
        return self.gcd(B,A%B)
```
