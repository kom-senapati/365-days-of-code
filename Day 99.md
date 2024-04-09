## Day 99

Link: https://x.com/kom_senapati/status/1777689888055562484

### Approach

- Created a flag to check if we need to zero the first col
- Traversed the matrix and set first element of row 0 if any 0 found in row and also with col and flag
- Then zeroed out matrix acc to rows and cols (not first)
- Then checked for first row and matrix and zeroed out if any left

### Code

```cpp
void Solution::setZeroes(vector<vector<int> > &a) {
    int m = a.size();
    int n = a[0].size();
   
    bool flag = false;
   
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(a[i][j] == 0){
                a[i][0] = 0;
                if(j != 0){
                    a[0][j] = 0;
                } else {
                    flag = true;
                }
            }
        }
    }
   
    for(int i = 1; i < m; i++){
        for(int j = 1; j < n; j++){
            if(a[i][0] == 0 || a[0][j] == 0)
                a[i][j] = 0;
        }
    }
   
    if(a[0][0] == 0){
        for(int i = 0; i < n; i++){
            a[0][i] = 0;
        }
    }
   
    if(flag){
        for(int i = 0; i < m; i++){
            a[i][0] = 0;
        }
    }
}
```
