## Day 5

Link: https://x.com/kom_senapati/status/1743483443835781353?s=20

### Approach:

- Created a custom Comparator
- Used it to change order of priority queue
- Then took the inputs and used switch to carry out the stated tasks

### Code:

```java
class pqcomp implements Comparator<Integer> {
    @Override
    public int compare(Integer a, Integer b) {
        return b - a;
    }
}
public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        Comparator<Integer> comp = new pqcomp();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Q,comp);
        for (int i=0;i<Q;i++) {
            int x,y;
            x = sc.nextInt();
            y = sc.nextInt();
            switch (x) {
                case 1:
                    pq.offer(y);
                    break;
                case 2:
                    System.out.println((pq.size() != 0) ? pq.peek() : -1);
                    break;
                case 3:
                    if (pq.size() != 0) pq.poll();
                    break;
            }
        }
    }
}
```
