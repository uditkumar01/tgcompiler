# Telegram Buddy

This will help in various task while messaging on telegram like you can compile a python or c code and can fetch git profile or repo data/details using telegram buddy. More features will be introduced soon...

# Commands
 - `/pylang` helps you to compile python code while messaging.
    
    ```python3
    For Example:
    
    /pylang
    l = [int(i) for i in input().split()]
    print(l)
    
    py_input_vars:  # input here
    1 2 3 4 5
    ```
    ```
    OUTPUT:

    123 456 789 123 456 789 123 456 789
    ```
 - `/clang` can be used to compile python code while messaging.
    ```c
    For Example:
    
    /clang
    #include <stdio.h> 
    int main() 
    { 
      // array to store digits 
      int a[100000]; 
      int i, number_of_digits; 
      scanf("%d", &number_of_digits); 
      for (i = 0; i < number_of_digits; i++) { 

        // %1d reads a single digit 
        scanf("%3d", &a[i]); 
      } 

      for (i = 0; i < number_of_digits; i++) 
        printf("%d ", a[i]); 

      return 0; 
    } 
    c_input_vars:
    9
    123456789123456789123456789
    ```
    ```text
    OUTPUT:

    123 456 789 123 456 789 123 456 789
    ```
