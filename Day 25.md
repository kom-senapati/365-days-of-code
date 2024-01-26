## Day 25

Link: https://x.com/kom_senapati/status/1750723230183436587?s=20

### Approach:

- Created a new class pair as stated
- Created a compareTo method which is used to for sorting the arr

### Code:

```java
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        
        /****Don't alter the code below*****/
        Scanner in = new Scanner(System.in);
        ArrayList<pair> arr = new ArrayList<pair>();
        int n = in.nextInt();
        in.nextLine();
        for(int i = 0;i<n;i++)
        {
            int a = in.nextInt();
            int b = in.nextInt();
            arr.add(new pair(a,b));
            in.nextLine();
        }
        in.close();
        Collections.sort(arr);
        for(int i=0;i<n;i++)
        {
            System.out.println(arr.get(i).first + " " + arr.get(i).second);
        }
        /*********************************************************************/
        
    }

    public static class pair implements Comparable<pair> {
        int first;
        int second;
        
        public pair(int a, int b) {
            this.first = a;
            this.second = b;
        }

        @Override
        public int compareTo(pair other) {
            if (this.second != other.second) {
                return Integer.compare(other.second, this.second);
            } else {
                return Integer.compare(other.first, this.first);
            }
        }
    }
}
```
