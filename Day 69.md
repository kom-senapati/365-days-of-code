## Day 69

Link: https://x.com/kom_senapati/status/1766664908018434264?s=20

### Approach:

- Traverse through the array and push the index or create new arraylist in it
- Iterate again in arraylist and check for valid pairs and increment count with modulo
- return count at last

### Code:

```java
public class Solution {
    public int solve(ArrayList<Integer> A, int B) {
        final int MOD = 1000000007;
        int count = 0;

        Map<Integer, List<Integer>> hashMap = new HashMap<>();
        for (int i = 0; i < A.size(); i++) {
            if (!hashMap.containsKey(A.get(i))) {
                hashMap.put(A.get(i), new ArrayList<>());
            }
            hashMap.get(A.get(i)).add(i);
        }

        for (int i = 0; i < A.size(); i++) {
            List<Integer> indices = hashMap.get(A.get(i));
            for (int j = 0; j < indices.size(); j++) {
                if (indices.get(j) > i && indices.get(j) - i <= B) {
                    count = (count + 1) % MOD;
                }
            }
        }

        return count;
    }
}
```
