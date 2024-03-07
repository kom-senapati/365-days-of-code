## Day 66

Link: https://x.com/kom_senapati/status/1765704588156444763?s=20

### Approach:

- Found the pivot (rightmost digit in the string that is smaller than the digit to its right). If not found returned -1.
- Searched from right to left to find the smallest digit larger than the pivot
- Swapped the pivot and the larger digit found.
- Reversed the substring to the right of the pivot and returned it

### Code:

```py
class Solution:
    def reverse(self, A, i, j):
        """
        Reverses A from i to j
        """
        A = list(A)
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return ''.join(A)

    def solve(self, A):
        i = len(A) - 2
        n = len(A)
        while i >= 0:
            if A[i] < A[i + 1]:
                break
            i -= 1

        if i == -1:
            return "-1"

        j = n - 1
        while j > i:
            if A[j] > A[i]:
                break
            j -= 1

        A = list(A)
        A[j], A[i] = A[i], A[j]

        return self.reverse(''.join(A), i + 1, n - 1)
```
