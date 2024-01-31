## Day 30

Link: https://x.com/kom_senapati/status/1752536698175770949?s=20

### Approach:

- Defined a helper function to check if a number is prime or not
- Iterated over the numbers from 2 to A and checked if the i and A-i are prime
- If they were prime returned them

### Code:

```py
class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
        def is_prime(n):
            if n < 2: return False
            elif n==2: return True
            elif n%2==0:return False
            for i in range(3,int(n ** .5) + 1,2):
                if n%i==0:return False
            return True
            
        for i in range(2,A):
            if is_prime(i) and is_prime(A-i):
                return [i,A-i]
```
