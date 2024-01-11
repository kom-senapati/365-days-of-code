## Day 10

Link: https://x.com/kom_senapati/status/1745389580449411318?s=20

### Approach:

- Created a StringBuilder to store the substring which has to reversed
- Reversed the above StringBuilder
- Created another StringBuilder to create the result
- Replaced the specified substr with the reversed one
- Then returned the result

### Code:

```java
public static String solve(String s, int L, int R)
{
    StringBuilder sb = new StringBuilder(s.substring(L,R+1));
    sb.reverse();
    StringBuilder res = new StringBuilder(s);
    res.replace(L,R+1,sb.toString());
    return res.toString();
}
```
