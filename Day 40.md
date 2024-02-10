## Day 40

Link: https://x.com/kom_senapati/status/1756145451810672777?s=20

### Approach:

- Most recent index is maintained by d
- When the char is seen and its in dict, then we update the left pointer to char after the repeating char
- we also keep the track of longest substr with res
- at last its returned

### Code:

```py
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
        res = 0
        d = {}
        left = 0

        for i, c in enumerate(A):
            if c in d and d[c] >= left:
                left = d[c] + 1
            d[c] = i
            res = max(res, i - left + 1)

        return res
```
