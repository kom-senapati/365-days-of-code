## Day 26

Link: https://x.com/kom_senapati/status/1751078637292659010?s=20

### Approach:

- Created a list out of given sides
- Sorted them and checked if they satisfied rectangle conditions

### Code:

```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        sides = [A,B,C,D]
        sides.sort()
        return 1 if sides[0] == sides[1] and sides[2] == sides[3] else 0
```
