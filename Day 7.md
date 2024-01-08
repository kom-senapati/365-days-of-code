## Day 7

Link: https://x.com/kom_senapati/status/1744194062209646725?s=20

### Approach:

- Created a Scanner
- Took 2 Strings as input
- Then used string methods to do the stated tasks

### Code:

```java
public static void main(String[] args) {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // DO NOT USE ARGUMENTS FOR INPUTS
    // E.g. 'Scanner' for input & 'System.out' for output
    Scanner sc = new Scanner(System.in);
    String A = sc.nextLine();
    String B = sc.nextLine();
    System.out.println(A.length() + B.length());
    System.out.println((A.compareTo(B) > 0) ? "Yes" : "No");
    System.out.println(A.toUpperCase()+ " " +B.toUpperCase());
    sc.close();
}
```
