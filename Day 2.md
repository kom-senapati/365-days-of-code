## Day 2

Link: https://x.com/KomSenapati/status/1742385408892428455?s=20

### Approach:

- Took the inputs and created queue.
- Used if else ladder to perform the stated tasks

### Code:

```java
public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        int Q;
        Scanner sc = new Scanner(System.in);
        Q = sc.nextInt();
        Queue<Integer> q = new ArrayDeque<>();
        for (int i=0;i<Q;i++){
            int x,y;
            x = sc.nextInt();
            y = sc.nextInt();
            if (x==1){
                q.add(y);
            } else if (x==2){
                if (q.size() != 0){
                    System.out.println(q.peek());
                } else System.out.println(-1);
            } else if (x==3){
                if (q.size() != 0){
                    q.remove();
                }
            }
        }
    }
```
