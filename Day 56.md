## Day 56

Link: https://x.com/kom_senapati/status/1761590193994231949?s=20

### Approach:

- Created a custom Compare class by overriding the default compare method
- Created a string array of given ints
- Sorted the array using Compare class
- Made the string result using StringBuilder
- Popped leading 0s

### Code:

```java
public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    static class Compare implements Comparator<String> {
        @Override
        public int compare(String a, String b) {
            if ((a + b).compareTo(b + a) > 0) {
                return -1;
            } else {
                return 1;
            }
        }
    }
    public String largestNumber(final int[] A) {
        String[] strArr = new String[A.length];
        for (int i = 0; i < A.length; i++) {
            strArr[i] = Integer.toString(A[i]);
        }
        
        Arrays.sort(strArr, new Compare());

        StringBuilder result = new StringBuilder();
        for (String s : strArr) {
            result.append(s);
        }
        
        String finalResult = result.toString();
        finalResult = finalResult.replaceFirst("^0+(?!$)", "");
        return finalResult.isEmpty() ? "0" : finalResult;
    }
}
```
