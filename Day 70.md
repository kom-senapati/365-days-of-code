## Day 70

Link: https://x.com/kom_senapati/status/1767161618012488019?s=20

### Approach:

- Created res variable (StringBuilder for efficiency)
- Traversed through the string and got the count of a character
- If the count was not equal to B appended the characters to res
- Returned the res at end

### Code:

```java
public class Solution {
    public String solve(String A, int B) {
        int N = A.length();
        StringBuilder res = new StringBuilder();
        
        for (int i = 0; i < N; ++i) {
            int cnt = 1; 
            int j = i + 1;
            while (j < N && A.charAt(j) == A.charAt(i)) {
                j++;
                cnt++;
            }
            if (cnt != B) {
                while (i < j) {
                    res.append(A.charAt(i));
                    i++;
                }
            }
            i = j - 1;
        }
        return res.toString();
    }
}
```
