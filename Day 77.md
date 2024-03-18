## Day 77

Link: https://x.com/kom_senapati/status/1769696481454211168?s=20

### Approach:

- Created helper functions to check if given strings form a ipv4 address or not, create strings for indices, join the indices to form valid ipv4 address
- Then iterated through the given string to form all possible ipv4 address and checked if they are valid and made an array to store the indices
- Then added all the ip addresses into res array and returned

### Code:

```py
class Solution:
	# @param A : string
	# @return a list of strings
	def restoreIpAddresses(self, A):
        def ifValid(A):
            if len(A) != 4:
                return False
            
            for i in range(4):
                if A[i][0] == '0' and len(A[i]) != 1:
                    return False
                elif int(A[i]) > 255:
                    return False
            return True
        
        def makeArray(A, i1, i2, i3):
            arr = [""] * 4
            arr[0] = A[:i1]
            arr[1] = A[i1:i2]
            arr[2] = A[i2:i3]
            arr[3] = A[i3:]
            return arr
        
        def getIPAdd(A, iValues):
            res = A[:iValues[0]] + "." + A[iValues[0]:iValues[1]] + "." + A[iValues[1]:iValues[2]] + "." + A[iValues[2]:]
            return res

        lenA = len(A)
        
        if lenA < 4 or lenA > 12:
            return None
        
        Res = []
        iValuesArr = []

        for i1 in range(1, 4):
            for i2 in range(i1 + 1, i1 + 4):
                for i3 in range(i2 + 1, i2 + 4):
                    if i3 < lenA:
                        iValues = []
                        if ifValid(makeArray(A, i1, i2, i3)):
                            iValues.extend([i1, i2, i3])
                            iValuesArr.append(iValues)
        
        for i in range(len(iValuesArr)):
            Res.append(getIPAdd(A, iValuesArr[i]))

        return Res
```
