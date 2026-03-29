# Midterm 2025

## Question 1
Trace the following segment of code and show the outputs. **(3 points each)**

```python
L = [10, 6, 5, 3]
for i, j in enumerate(L):
    print(pow(j, i), end='@')
```

```python
def fun(*arg):
    N=0
    for v in args:
        if v >= 0:
            N += v
        print(N)
    N /= len(args)
    return N

print(fun(5, 3, -7, 8))
```

## Question 2
Write a single statement that do the following: **(2 points each)**
1. Shorthand if that print "the number is even" if value of `A` is even.
2. Sort elements of list `A`
3. Build a dictionary from two lists `keys` and `values`

## Question 3
Write a function that takes a list of strings as input and returns a new list
with all the strings lower case **(4 points)**.

## Question 4
Create a Python class named `Book` with the following features: **(6 points)**
- A constructor `__init__` that initializes three attributes: title, author and
  year.
- A `__str__` method that returns a string representation of the book in the
  format: `"Title: <title>, Author: <author>, Year: <year>"`
- A method called `is_classic()` that returns `True` if the book was published
  more than 50 years ago and `False` otherwise.
