# Telegram Buddy

This will help in various task while messaging on telegram like you can compile a python or c code and can fetch git profile or repo data/details using telegram buddy. More features will be introduced soon...

# Commands
 - `/pylang` helps you to compile python code while messaging.
    
    ```python3
    For Example:
    
    /pylang
    l = [int(i) for i in input().split()]
    
    py_input_vars:  # input here
    1 2 3 4 5
    ```
 - `/clang` can be used to compile python code while messaging.
    ```c
    For Example:
    
    /clang
    #include <stdio.h>
    
    void main(){
      int arr[10],i,n;
      scanf("%d",&n);
      while(i<n){
        scanf("%d",&arr[i]);
        i++;
      }
      i = 0;
      while(i<n){
        printf("%d",arr[i]);
        i++;
      }
    }
    // input here
    c_input_vars:
    5
    1 2 3 4 5
    ```
