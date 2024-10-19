# README.md Assignment3

## Table of contents
* [Array.py](#Array.py)
* [test_Array.py](#test_Array.py)

## Array.py

### Prerequisites

- You need to have Python 3 installed.

### Functionality

- Works with 1D and 2D arrays.
- Checks if all arguments are implemented correctly.
- Returns the value of an item in the array.
- Returns a nicely printable string representation of the array.
- Element-wise adds Array with another Array or number.
- Element-wise subtracts an Array or number from another Array.
- Element-wise multiplies an Array or number with another array.
- Compares the shape of an Array with another Array.
- Compares an Array element-wise with another Array or number.
- Returns the smallest value of the array.

### Missing Functionality

- Does not work with *n*-dimentional arrays.

### Usage

- First you need to initialize your array. This Array class needs two arguments provided by the user:
  - **shape(tuple)**: shape *(n, m)* of the array as a tuple. E.g. an 1D array with *n* elements will have shape = *(n, 1)*. 
  - ***values**: The values in the array. These should all be the same data type. Either int, float or bool.
 
   E.g.: 
   ``` 
   1. my_array = Array((3 , 2) , 8, 3, 4, 1, 6, 1) 
   ```
- The ***__getitem__*** function returns value of item in array. It needs one argument provided by the user.
  - **item(int)**: Index of value to return.
  
  E.g.:
    ```
    1. my_array = Array((3 , 2) , 8, 3, 4, 1, 6, 1)
    2. my_array[1][0]
    ```
- Use `print()` to return a nicely printable string representation of the array.
- Use `+` to add an Array element-wise with another Array or number
- Use `-` to substract an Array element-wise with another Array or number
- Use `*` to multiply an Array element-wise with another Array or number
- Use `==` to compare the shape of an Array with another Array.
- The ***is_equal*** function comperes an Array element-wise with another Array or number. It need one argument provided by the user:
  - **other (Array, float, int)**: The array or number to compare with this array.
 
  E.g.
    ```
    1. my_array1 = Array((3 , 2) , 8, 3, 4, 1, 6, 1)
    2. my_array2 = Array((3 , 2) , 8, 3, 4, 1, 6, 2)
    3. my_array1.is_equal(my_array2)
    ```
- The **min_element** function returns the smalles value of the array. Does not work with booleans.
  E.g.
    ```
    1. my_array = Array((3 , 2) , 8, 3, 4, 1, 6, 1)
    2. my_array.min_element()
    ```

## test_Array.py

### Prerequisites

- You need to have Python 3 installed.
- You need to have pytest installed.

### Functionality

- Checks if every functionality of the Array.py works as it should. 

### Usage

- Run the test using the command `pytest` in the command line, e.g.:
```
$ pytest test_Array.py
```
