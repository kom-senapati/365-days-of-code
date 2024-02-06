## Day 36

Link: https://x.com/kom_senapati/status/1754851883636719798?s=20

### Approach:

- Removed spaces, special characters using regex
- Changed the string to lowercase
- checked if it was palindrome using string slicing

### Code:

```py
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        import re
        A = re.sub(r'[^a-zA-Z0-9]', '', A).lower()
        return int(A == A[::-1])
```
