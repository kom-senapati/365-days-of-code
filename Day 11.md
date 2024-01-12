## Day 11

Link: https://x.com/kom_senapati/status/1745706860316098802?s=20

### Approach:

- Created a scanner and took the numeric string as input
- Converted the string to BigInteger
- Used if else and isProbablePrime method to print prime or not


### Code:

```java
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    BigInteger bi = new BigInteger(s);
    if (bi.isProbablePrime(1))
        System.out.println("prime");
    else 
        System.out.println("not prime");
}
```
