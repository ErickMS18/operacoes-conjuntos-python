# Set Operations in Python

This project aims to develop a program that performs operations on data sets, such as **union**, **intersection**, **difference**, and **cartesian product**. The program is developed in **Python** and takes as input a text file (`.txt`) containing the data and operations to be performed.

## Project Requirements

- The program must read an input text file with the following format:
  1. The first line contains the number of operations to be performed.
  2. The following lines describe the operations and the sets involved:
     - **U**: Union
     - **I**: Intersection
     - **D**: Difference
     - **C**: Cartesian product
  3. Each operation is followed by two lines containing the elements of the sets, separated by commas.

### Sample Input File

```4```
```U```
```3, 5, 67, 7```
```1, 2, 3, 4```
```I```
```1, 2, 3, 4, 5```
```4, 5```
```D```
```1, A, C, 34```
```A, C, D, 23```
```C```
```3, 4, 5, 5, A, B, R```
```1, B, C, D, 1```

### Sample Output

For the union operation (U) between the sets `{3, 5, 67, 7}` and `{1, 2, 3, 4}`, the output will be:

Union: set 1 {3, 5, 67, 7}, set 2 {1, 2, 3, 4}. Result: {3, 5, 67, 7, 1, 2, 4}


### How to Run

- The code is available in the project folder, along with the test files.
- The program can be run in the terminal or output the results to a file.

**Note**: The output must be formatted correctly, as shown in the example above, to avoid losing points in the evaluation.
