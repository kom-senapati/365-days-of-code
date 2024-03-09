## Day 68

Link: https://x.com/kom_senapati/status/1766335746414174620?s=20

### Approach:

- Created MOD and s vars to store the modulo and count of amazing substrings
- Traversed through the string and checked if the char was a vowel and added number of possible substrings from that index modulo MOD
- atlast returned s

### Code:

```java
public class Solution {
    public int solve(String A) {
        int MOD = 10003;
        int s = 0;
        int n = A.length() - 1;
        for (int i=0;i<=n;++i){
            char ch = A.charAt(i);
            if(ch == 'a' || ch == 'e' || ch == 'i' || ch=='o' || ch =='u' || ch == 'A' || ch == 'E' || ch == 'I' || ch=='O' || ch =='U'){
                s += (n-i+1) % MOD;
            }
        }
        return s % MOD;
    }
}
```
