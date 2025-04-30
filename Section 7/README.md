# Sheet 7

1. Make sure that numpy is installed on your device by importing numpy module, then print its version.

<details>
    <summary>Answer</summary>

```python
import numpy as np
print(np.__version__)
```
</details>

## Creating array

2. Create an `1D` array which contains numbers `1,2,3`

<details>
    <summary>Answer</summary>

```python
import numpy as np
arr = np.array([1, 2, 3])
```
</details>

3. Create `1D` array which contains numbers from `1` up to `100` using `list` and `range` function.

<details>
    <summary>Answer</summary>

```python
arr = np.array(list(range(1,100)))
```
</details>

4. Create `1D` array whcih contains numbers from `1` up to `100` using `arange` function from numpy.

<details>
    <summary>Answer</summary>

```python
my_array = np.arange(1,100)
```
</details>


5. Create `2D` array which contains numbers from `1` up to `9`, with `3` rows and `3` columns.

<details>
    <summary>Answer</summary>

```python
k = np.array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
])
```
</details>

## Shape and Reshape

6. Create the same `2D` array from last question array by creating `1D` array using `arange` then `reshape` it.

<details>
    <summary>Answer</summary>

```python
arr = np.arange(1,10).reshape(3,3)
```
</details>

7. Convert the `2D` array from last question back to `1D`.

<details>
    <summary>Answer</summary>

```python
arr = np.arange(1,10).reshape(3,3)
arr = arr.flatten()
```

or

```python
arr = np.arange(1,10).reshape(3,3)
arr = arr.reshape(-1)
```
</details>

8. Given array with shape `(100,)` reshape it into `2D` array with `4` rows. **Don't explicitly write number of columns**

<details>
    <summary>Answer</summary>

```python
arr = np.arange(100) # array with shape (100)
arr = arr.reshape(4,-1) # reshape with size 4 and size/4
```
</details>

## Indexing and Slicing

9. Given array `a = np.arange(100).reshape(-1, 10)` what is the value stored at `[9][2]`

<details>
    <summary>Answer</summary>
Array has values from 0 to 100,

It is reshaped into (-1, 10) which is equal to (100/10, 10) = (10, 10), 

The value at row 9 and column 2 is 92
</details>

10. Print the third row of the array `a = np.arange(100).reshape(-1, 10)`

<details>
    <summary>Answer</summary>

```python
a = np.arange(100).reshape(-1, 10)
print(a[3, :]) # print row 3 and column all
```
</details>

11. Print the fourth column of the array `a = np.arange(100).reshape(-1, 10)`

<details>
    <summary>Answer</summary>

```python
a = np.arange(100).reshape(-1, 10)
print(a[:, 4])
```

</details>

## Join and Split

12. Given arrays `a = np.arange(10).reshape(-1,2)` and `b = np.arange(10,20).reshape(-1,2)` join them together to create an array with shape `(5, 4)` and `(10, 2)`

<details>
    <summary>Answer</summary>

```python
a = np.arange(10).reshape(-1,2)
b = np.arange(10,20).reshape(-1,2)
arr_10_2 = np.concatenate([a,b], axis=0) # axis = 0, row
arr_5_4 = np.concatenate([a,b], axis=1) # axis = 1, col
```
</details>

13. Give array `a = np.arange(20)` split it into 4 arrays of the same size.

<details>
    <summary>Answer</summary>

```python
a = np.arange(20)
arrays = np.split(a, 4)
```
</details>

14. Give array `a = np.arange(20)` split it into 4 arrays of size 3, 4, 5 and 8.

<details>
    <summary>Answer</summary>

```python
a = np.arange(20)
arrays = np.split(a, [3, 7, 12])
```
</details>

## Casting

14. Create an array of floating nubmers from `0` up to `1` with step `0.1`

<details>
    <summary>Answer</summary>

```python
f = np.arange(11) / 10
```
</details>

15. Cast the following array into array of double `a = np.arange(100).reshape(-1, 10)`

<details>
    <summary>Answer</summary>

```python
a = np.arange(100).reshape(-1, 10)
a = a.astype(np.double)
```
</details>


## Mathimatical Operations

16. Given array `a = np.arange(100).reshape(-1, 10)` perform the following operations:
    - `a + 1`
    - `a - 1`
    - `a * 2`
    - `a / 2`
    - `a ** 2`

<details>
    <summary>Answer</summary>
try it yourself and see the result.
</details>

17. Given array `a = np.arange(100).reshape(-1, 10)` perform the following operations:
    - `a > 50`
    - `a < 50`
    - `a >= 50`

<details>
    <summary>Answer</summary>
try it yourself and see the result.
</details>

18. Given array `a = np.array([1,2,3])` and `b = np.array([4,5,6])` perform the following operations:
    - `a + b`
    - `a - b`
    - `a * b`
    - `a / b`

<details>
    <summary>Answer</summary>
try it yourself and see the result.
</details>

19. Given array `a = np.array([1,2,3])` and `b = np.array([4,5,6])` perform the following operations:
    - `a > b`
    - `a < b`
    - `a >= b`

<details>
    <summary>Answer</summary>
try it yourself and see the result.
</details>

## Broadcasting

20. What is the output of the following code:

```python
a = np.array([1,2,3]).reshape(3,1)
b = np.array([4,5,6]).reshape(1,3)

print(a + b)
```

<details>
    <summary>Answer</summary>

array `a` and `b` are reshaped to match each other,
`a` will be `3x3` by repeating first column,
`b` will be `3x3` by repeating first row.
</details>
