## Day 31

Link: https://x.com/kom_senapati/status/1752892222914331108?s=20

### Approach:

- Returned 0  if A was greater than or equal to 0
- Then checked for palindrome by str tricks
- converted the boolean to int by int function

### Code:

```py
class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        return int( A>=0 and str(A) == str(A)[::-1] )
```
