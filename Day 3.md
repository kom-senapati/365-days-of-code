## Day 2

Link: https://x.com/KomSenapati/status/1742754506839069065?s=20

### Approach:

- Took the inputs and created a priority queue.
- Used if else ladder to perform the stated tasks

### Code:

```java
public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        PriorityQueue<Integer> pq = new PriorityQueue<>(); 
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        for (int i=0;i<Q;i++){
            int x,y;
            x = sc.nextInt();
            y = sc.nextInt();
            if (x == 1) {
                pq.offer(y);
            } else if (x == 2) {
                if (!pq.isEmpty()) {
                    System.out.println(pq.peek());
                } else {
                    System.out.println(-1);
                }
            } else if (x == 3) {
                if (!pq.isEmpty()) {
                    pq.poll();
                }
            }
        }
    }
```
