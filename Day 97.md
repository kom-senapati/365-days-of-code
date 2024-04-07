## Day 97

Link: https://x.com/kom_senapati/status/1776808762722103600

### Approach

- A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.
- Did this logic with if else ladder

### Code

```py
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A % 400 == 0:
            return 1
        elif A % 100 == 0:
            return 0
        elif A % 4 == 0:
            return 1
        else:
            return 0
```
