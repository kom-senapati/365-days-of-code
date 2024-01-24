## Day 23

Link: https://x.com/kom_senapati/status/1749997593176973459?s=20

### Approach:

- First solved all the edge cases and even number case.
- Then checked only the odd numbers till the sqrt of A.
- If not found any divisor, returned 1

### Code:

```java
public class Solution {
    public int isPrime(int A) {
        if (A<2) return 0;
        if (A==2) return 1;
        if (A%2==0) return 0;
        for (int i=3;i<Math.sqrt(A)+1;i+=2){
            if (A%i==0) return 0;
        }
        return 1;
    }
}
```
