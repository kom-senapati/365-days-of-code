## Day 37

Link: https://x.com/kom_senapati/status/1755230137447006344?s=20

### Approach:

- Stripped the string for removing spaces, if it was empty returned 0
- Splitted the string for obtaining words, if it was empty returned 0
- returned length of last word

### Code:

```py
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
        A = A.strip()
        if not A : return 0
        A = A.split()
        if not A : return 0
        return len(A[-1])
```
