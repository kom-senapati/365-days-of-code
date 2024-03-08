## Day 67

Link: https://x.com/kom_senapati/status/1765945340018962739?s=20

### Approach:

- The `Mod` method calculates `(A^B) % C`.
- It converts negative `A` to its positive modular equivalent.
- If `A` is zero, it returns 0.
- If `B` is zero, it returns 1.
- It iteratively updates `result` and `base` using binary exponentiation technique.
- In each iteration, it multiplies `result` by `base` if the current bit of `B` is 1.
- Then, it updates `B` to be `B` divided by 2 and updates `base` to its square modulo `C`.
- Finally, it returns the calculated `result`.

### Code:

```py
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @return an integer
	def Mod(self, A, B, C):
        if A < 0:
            A = A % C
        elif A == 0:
            return 0
        elif B == 0:
            return 1
        result = 1
        base = A % C
        while B > 0:
            if B % 2 == 1:
                result = (result * base) % C
            B //= 2
            base = (base * base) % C
        return result
```
