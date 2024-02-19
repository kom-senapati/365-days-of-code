## Day 49

Link: https://x.com/kom_senapati/status/1759538128220479959?s=20

### Approach:

- If new_interval was empty, returned intervals
- Created a res list
- Iterated over the intervals list and popped the last interval of res and checked for correct position or merge 
- Atlast returned res

### Code:

```py
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if not new_interval:
            return intervals
            
        res = [new_interval]
        for i in range(len(intervals)):
            a = res.pop()
            b = intervals[i]
            if a.start > b.end:
                res.extend([b,a])
            elif a.end < b.start:
                res.extend([a,b])
            else:
                start = min(a.start, b.start)
                end = max(a.end, b.end)
                res.append(Interval(start, end))
        
        return res
```
