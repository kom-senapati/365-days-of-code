## Day 12

Link: https://x.com/kom_senapati/status/1746003009719664935?s=20

### Approach:

- Created a scanner and hashset
- Stored the input integers in set
- Displayed size of set


### Code:

```java
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Set<Integer> nums = new HashSet<>();
    int A = sc.nextInt();
    for (int i=0;i<A;++i){
        nums.add(sc.nextInt());
    }
    System.out.println(nums.size());
    sc.close();
}
```
