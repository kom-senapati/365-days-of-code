## Day 58

Link: https://x.com/kom_senapati/status/1762827774455091239?s=20

### Approach:

- Squared the numbers given in A
- Sorted the array and then returned it

### Code:

```java
public class Solution {
    public ArrayList<Integer> solve(ArrayList<Integer> A) {
        for (int i=0;i<A.size();++i) {
            A.set(i, A.get(i) * A.get(i));
        }
        Collections.sort(A);
        return A;
    }
}
```
