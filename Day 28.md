## Day 28

Link: https://x.com/kom_senapati/status/1751819697098805389?s=20

### Approach:

- Checked if it was a bit returned the bit in string
- Else returned the reversed string of remainders of A (recursively obtained)

### Code:

```java
public class Solution {
    public String findDigitsInBinary(int A) {
        if (A <= 1) return Integer.toString(A);
        return findDigitsInBinary(A / 2).concat(Integer.toString(A % 2));
    }
}
```
