## Day 71

Link: https://x.com/kom_senapati/status/1767541621506126038?s=20

### Approach:

- Created res variable
- And looped till A was 1 and created a var curr and iterated through the previous string
- and got the count of the each char and appended to curr var and after the after iteration changed res var
- returned res

### Code:

```java
public class Solution {
    public String countAndSay(int A) {
        if (A <= 0) return "";
        String res = "1";
        while (A > 1) {
            
            StringBuilder curr = new StringBuilder();
            for (int i=0;i<res.length();++i) {
                int c = 1;
                while (i+1 < res.length() && res.charAt(i) == res.charAt(i+1)){
                    c++;
                    i++;
                }
                curr.append(c).append(res.charAt(i));
            }
            res = curr.toString();
            A--;
        }
        
        return res;
    }
}
```
