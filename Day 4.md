## Day 4

Link: https://x.com/KomSenapati/status/1743089013094039937?s=20

### Approach:

- Took the inputs and created a deque
- Used swith case statements to perform the stated tasks

### Code:

```java
public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
        Deque<Integer> deq = new ArrayDeque<>();
        int Q = sc.nextInt();
        for (int i=0;i<Q;i++) {
            int x,y;
            x = sc.nextInt();
            y = sc.nextInt();
            switch (x) {
                case 1:
                    deq.addLast(y);
                    break;
                case 2:
                    deq.addFirst(y);
                    break;
                case 3:
                    System.out.println((deq.size() == 0) ? -1 : deq.peekFirst());
                    break;
                case 4:
                    System.out.println((deq.size() == 0) ? -1 : deq.peekLast());
                    break;
                case 5:
                    if (deq.size() != 0) deq.removeFirst();
                    break;
                case 6:
                    if (deq.size() != 0) deq.removeLast();
            }
        }
    }
```
