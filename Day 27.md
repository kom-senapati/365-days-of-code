## Day 27

Link: https://x.com/kom_senapati/status/1751447930769400130?s=20

### Approach:

- First counted the factors of the number
- Then made factors array of that size and added to them
- At last sorted and returned the array
- For finding factors traversed till sqrt(A)

### Code:

```java
public class Solution {
    public int[] allFactors(int A) {
        int count = 0;

        for (int i = 1; i <= Math.sqrt(A); i++) {
            if (A % i == 0) {
                if (A/i == i) {
                    count++;
                } else {
                    count += 2;
                }
            }
        }

        int[] factors = new int[count];
        int index = 0;

        for (int i = 1; i <= Math.sqrt(A); i++) {
            if (A % i == 0) {
                factors[index++] = i;
                if (A/i != i) {
                    factors[index++] = A/i;
                }
            }
        }
        Arrays.sort(factors);
        return factors;
    }
}
```
