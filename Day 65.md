## Day 65

Link: https://x.com/kom_senapati/status/1765343355003621787?s=20

### Approach:

- Incremented A by 1 until B was 0 and returned A

### Code:

```java
public class Solution {
    public int addNumbers(int A, int B) {
        while (B>0) {
            A++;
            B--;
        }
        return A;
    }
}
```
