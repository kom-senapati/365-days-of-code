## Day 21

Link: https://x.com/kom_senapati/status/1749225402869191008?s=20

### Approach:

- Checked all the conditions and found out a<=b was not implemented
- Then changed `b = 0` to `b = a`

### Code:

```python
class Solution:
	# @param A : integer
	# @return a list of list of integers
	def squareSum(self, A):
		ans = []
		a = 0
		while a * a < A:
			b = a
			while b * b < A:
				if a * a + b * b == A:
					newEntry = [a, b]
					ans.append(newEntry)
				b += 1
			a += 1
		return ans
```
