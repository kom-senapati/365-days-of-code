## Day 6

Link: https://x.com/kom_senapati/status/1743833793595887681?s=20

### Approach:

- Created a Scanner
- Took 2 BigIntegers as input
- Then computed the sum and shown the output.

### Code:

```java
public static void main(String[] args) {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // DO NOT USE ARGUMENTS FOR INPUTS
    // E.g. 'Scanner' for input & 'System.out' for output
    BigInteger x,y;
    Scanner sc = new Scanner(System.in);
    x = new BigInteger(sc.nextLine());
    y = new BigInteger(sc.nextLine());
    System.out.print(x.add(y));
}
```
