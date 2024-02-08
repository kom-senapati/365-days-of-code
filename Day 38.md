## Day 38

Link: https://x.com/kom_senapati/status/1755568946143477827?s=20

### Approach:

- Created a helper function to check str within specified indexes for being palindrome
- If given str was palindrome returned 1
- Else iterated the string from both sides and checked the end chars, if they were not equal checked if str was palindrom except it and returned 1 

### Code:

```py
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, string, low, high):
        while low < high:
            if string[low] != string[high]:
                return False
            low += 1
            high -= 1
        return True
    def solve(self, A):
        l = 0
        h = len(A) - 1
        if self.isPalindrome(A,l,h):return 1
        while l < h:
            if A[l] == A[h]:
                l += 1
                h -= 1
            else:
                if self.isPalindrome(A, l + 1, h) or self.isPalindrome(A, l, h - 1):
                    return 1
                return 0
        return 0
```
