## Day 80

Link: https://x.com/kom_senapati/status/1770808707799994404?s=20

### Approach:

- Created a dict and iterated throught the given arr and put their marks and counts in a list inside dict
- Then iterated through the items of d and found max_avg and returned

### Code:

```py
class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, A):
        d = {}
    
        for name, mark in A:
            if name not in d:
                d[name] = [0, 0]
            d[name][0] += int(mark)
            d[name][1] += 1
        
        max_avg = 0
        for name, (marks, count) in d.items():
            avg = marks // count
            max_avg = max(max_avg, avg)
        
        return max_avg
```