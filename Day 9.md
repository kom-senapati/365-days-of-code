## Day 9

Link: https://x.com/kom_senapati/status/1744920621904212224?s=20

### Approach:

- Created a StringBuffer to store the substring which has to reversed
- Reversed the above StringBuffer
- Created another StringBuffer to create the result
- Replaced the specified substr with the reversed one
- Then returned the result

### Code:

```java
public static String solve(String s, int L, int R)
{
    StringBuffer stringBuffer = new StringBuffer(s.substring(L, R + 1));
    stringBuffer.reverse();

    StringBuffer resultBuffer = new StringBuffer(s);
    resultBuffer.replace(L, R + 1, stringBuffer.toString());

    return resultBuffer.toString();
}
```
