## Day 96

Link: https://x.com/kom_senapati/status/1776497994113974315

### Approach

- Checked for sum of all subarrays, if it didnt exceed counted them in else broke the inner loop and restarted

### Code

```py
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def numRange(self, A, B, C):
		res = 0
		for i in range(len(A)):
			sum_ = 0
			for j in range(i, len(A)):
				sum_ += A[j]
				if B <= sum_ <= C:
					res += 1
				if sum_ > C:
					break
		return res
```
