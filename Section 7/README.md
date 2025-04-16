# Sheet 7

1. Make sure that numpy is installed on your device by importing numpy module, the print its version.

## Creating array

2. Create an `1D` array which contains numbers `1,2,3`

3. Create `1D` array whcih contains numbers from `1` up to `100` using `list` and `range` function.

4. Create `1D` array whcih contains numbers from `1` up to `100` using `arange` function from numpy.

5. Create `2D` array which contains numbers from `1` up to `9`, with `3` rows and `3` columns.

## Shape and Reshape

6. Create the same `2D` from last question array by creating `1D` array using `arange` then `reshape` it.

7. Convert the `2D` array from last question back to `1D`.

8. Given array with shape `(100,)` reshape it into `2D` array with `4` rows. **Don't explicitly write number of columns**

## Indexing and Slicing

9. Given array `a = np.arange(100).reshape(-1, 10)` what is the value stored at `[9][2]`

10. Print the third row of the array `a = np.arange(100).reshape(-1, 10)`

11. Print the fourth column of the array `a = np.arange(100).reshape(-1, 10)`

## Casting

12. Create an array of floating nubmers from `0` up to `1` with step `0.1`

13. Cast the following array into array of double `a = np.arange(100).reshape(-1, 10)`

## Mathimatical Operations

14. Given array `a = np.arange(100).reshape(-1, 10)` perform the following operations:
    - `a + 1`
    - `a - 1`
    - `a * 2`
    - `a / 2`
    - `a ** 2`

15. Given array `a = np.arange(100).reshape(-1, 10)` perform the following operations:
    - `a > 50`
    - `a < 50`
    - `a >= 50`

16. Given array `a = np.array([1,2,3])` and `b = np.array([4,5,6])` perform the following operations:
    - `a + b`
    - `a - b`
    - `a * b`
    - `a / b`

17. Given array `a = np.array([1,2,3])` and `b = np.array([4,5,6])` perform the following operations:
    - `a > b`
    - `a < b`
    - `a >= b`

## Broadcasting

18. What is the output of the following code:

```python
a = np.array([1,2,3]).reshape(3,1)
b = np.array([4,5,6]).reshape(1,3)

print(a + b)
```

