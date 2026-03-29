# Midterm 2024

## Question 1
Trace the following segment of code and show the outputs. **(2 points each)**

```python
A = [-5, 7, -9, 0]
B = [abs(x) for x in A]
print(B)
```


```python
L = [2, 3, 5, 7]
for i in L:
    for j in range(i):
        print(j, end=' ')
    print('')
```


```python
def fun(**kwargs):
    for key, item in kwargs.items():
        if '_' in key:
            print(item)

fun(A_1=5, A2=3, B1="h_w", B_2=False)
```

---

## Question 2

Write a single statement that do the following: **(2 points each)**

1. Make a `list` of even number between `0` and `100`.

2. Shorthand `if else` that print the smaller of two values `A` and `B`.

3. Sort `list1` in descending order.

4. Define a `lambda` function that take variable `x` and return range from `0` to less than `x`.

---

## Question 3

a) Write a program that ask user to input a number and calculate the factorial of that number and print it, the program should first check if the entered number is positive integer. **(4 points)**

b) Write a functoin that takes a `list of integers` as input and returns `True` if the list is sorted in ascending order, `False` otherwise. **(4 points)**

