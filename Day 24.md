## Day 24

Link: https://x.com/kom_senapati/status/1750429778178461771?s=20

### Approach:

- Created a new Arraylist
- Iterated through the range(0,A) and checked if the number is prime
- If it was found to be prime, added to arraylist
- Returned the arraylist

### Code:

```java
public class Solution {
    public static int isPrime(int A) {
        if (A<2) return 0;
        if (A==2) return 1;
        if (A%2==0) return 0;
        for (int i=3;i<Math.sqrt(A)+1;i+=2){
            if (A%i==0) return 0;
        }
        return 1;
    }
    public ArrayList<Integer> sieve(int A) {
        ArrayList<Integer> l = new ArrayList<>();
        for (int i=1;i<=A;++i){
            if (isPrime(i)==1) l.add(i);
        }
        return l;
    }
}
```
