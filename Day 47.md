## Day 47

Link: https://x.com/kom_senapati/status/1758680961695338767?s=20

### Approach:

- Marked the presence of ints in range [1,N]
- Iterated through the array and returned i+1 if found first positive int
- If all were present returned N+1

### Code:

```java
public class Solution {
    public int firstMissingPositive(ArrayList<Integer> A) {
        int N = A.size();
        for (int i = 0; i < N; i++) {
            int num = A.get(i);
            while (num > 0 && num <= N && A.get(num - 1) != num) {
                int temp = A.get(num - 1);
                A.set(num - 1, num);
                num = temp;
            }
        }
        for (int i = 0; i < N; i++) {
            if (A.get(i) != i + 1) {
                return i + 1;
            }
        }
        return N + 1;
    }
}
```
