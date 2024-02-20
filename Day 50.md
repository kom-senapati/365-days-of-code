## Day 50

Link: https://x.com/kom_senapati/status/1759917796245307796?s=20

### Approach:

- Sorted the intervals according to start value
- Created res array and traversed through intervals
- If it was overlapping edited the end of last interval in res else appended the interval

### Code:

```py
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        res = []
        for i in intervals:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        
        return res
```
