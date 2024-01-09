## Day 8

Link: https://x.com/kom_senapati/status/1744535102254883048?s=20

### Approach:

- Created a Scanner
- Took 1 String and 2 Integers as input
- Then used string substring method to do the stated task

### Code:

```java
public static void main(String[] args) {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // DO NOT USE ARGUMENTS FOR INPUTS
    // E.g. 'Scanner' for input & 'System.out' for output
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    int i = sc.nextInt();
    int j = sc.nextInt();
    System.out.println(s.substring(i,j+1));
    sc.close();
}
```
