# Sheet 4

## range, zip and map

1. Generate the following lists using the `range` function:
   - `[0, 1, 2, 3, 4, 5]`
   - `[4, 6, 8, 10]`
   - `[10, 9, 8, 7, 6]`
   - `[10, 5, 0, -5, -10]`

<details>
<summary>Answer</summary>

```python
list(range(6))
list(range(4, 11, 2))
list(range(10, 5, -1))
list(range(10, -11, -5))
```

</details>

2. What is the output of the following code, and explain the rule of the `zip` function?
   ```python
   x_coor = [1, 2, 3, 4, 5]
   y_coor = [2, 4, 6, 8, 10]
   z_coor = [0, -1, -2, -3, -4]

   points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
   ```

<details>
<summary>Answer</summary>

```
zip function is used to create an iterator that combines elements from two or more iterables.
it will create a tuple of elements from each of the iterables.
```

</details>


3. Write a single line using `map` that convert a list of floating point numbers to int
    ```python
    nums = [1.1, 2.8, 3.9, 4.4414, 85.134, -14.143]
    ```
<details>
<summary>Answer</symmary>
    ```python
    nums = [1.1, 2.8, 3.9, 4.4414, 85.134, -14.143]
    nums = list(map(int, nums))
    ```

</details>

---

## shorthand if-else, comprehension

1. Using shorthand if-else and list comprehension, generate a list indicating whether the corresponding number in the other list is even.
   ```python
   x = [1, 2, 10, 13, 1]
   # output = [False, True, True, False, False]
   ```

<details>
<summary>Answer</summary>
    ```python
    x = [1, 2, 10, 13, 1]

    print([True if num % 2 == 0 else False for num in x])
    ```

</details>


2. Given a list of float numbers, combine them into a single string with comma
   sperating between them, each number should be 2 digit at maximum after
   decimal point.
   ```python
    nums = [134.1414, 12.412, 1, 415.3, -134.111]
    # output: [134.14, 12.41, 1.00, 415.30, -134.11]
   ```

<details>
<summary>Answer</summary>
    ```python
    nums = [134.1414, 12.412, 1, 415.3, -134.111]
    s = ", ".join(f"{i:.2f}" for i in nums)
    ```

</details>


3. Create a list whose elements are strings, the names of people in your family.
Now use a set comprehension (and, better yet, a nested set comprehension) to
find which letters are used in your family members’ names.

<details>
<summary>Answer</summary>
    ```python
    names = ["ahmed", "ali", "mohamed"]

    s = set ( c for name in names for c in name )
    ```

<bold>We can write nested comprehension as follows:</bold>

1. first write the normal loop

```python
for name in names:
    for c in name:
        print(c)
```

2. then write the nested comprehension by putting the outer loop beside the inner loop

```python
for name in names for c in name
```

3. now we have nested loop and we have `c` that hold all characters.

4. then write the set comperehension

```python
s = set ( c for name in names for c in name )
```

</details>

---

## Functions

1. Write a function `norm` that takes a list and return a normalized list,
   normaliztion include subtract the mean (average) from all the values and
   devide by standard deviation.
    ```python
    # return the average of the list, average = sum of list / number of elements
    def average(numbers):
        pass
    
    # return the standard deviation of the list:
    # sum( (x_i - average(x))^2 ) / length(x)
    # std = sqrt( sum( (x_i - average(x))^2 ) / length(x) )
    def get_std(numbers):
        pass


    # nums = (nums - average) / std
    def norm(numbers):
        pass

    nums = [1,2,3,4,5]
    normalized_nums = norm(nums)

    print(normalized_nums)
    ```
<details>
<summary>Answer</summary>
    ```python
    # return the average of the list, average = sum of list / number of elements
    def average(numbers):
        return sum(numbers) / len(numbers)

    # return the standard deviation of the list:
    # sum( (x_i - average(x))^2 ) / length(x)
    # std = sqrt( sum( (x_i - average(x))^2 ) / length(x) )
    def get_std(numbers):
        mean = average(numbers)
        #s = 0
        #for x in numbers:
        #    s += (x - mean) ** 2
        s = sum([(x - mean) ** 2 for x in numbers])
        
        s /= len(numbers)
        return s ** 0.5

    # nums = (nums - average) / std
    def norm(numbers):
        mean = average(numbers)
        std = get_std(numbers)

        return [(num - mean) / std for num in numbers]

    nums = [1,2,3,4,5]
    normalized_nums = norm(nums)

    print(normalized_nums)
    ```

</details>


2. What is the output of the following code?

   ```python
   def modlist(lst):
       for i in range(len(lst)):
           lst[i] = 10 * lst[i]

   def modvar(num):
       num += 10

   lst = [1, 2, 3]
   modlist(lst)
   print(lst)

   x = 0
   modvar(x)
   print(x)
   ```

<details>
<summary>Answer</summary>
```
[10, 20, 30]
0
```
</details>


3. Write a function that finds the average of a list of numbers passed as arguments.

```python
def average(*numbers):
    pass
```

<details>
<summary>Answer</summary>

```python
def average(*numbers):
    return sum(numbers) / len(numbers)

avg = average(1, 2, 3)
print(avg)
```

</details>

4. Write a function that substitutes variables into a mathematical equation
   written as a string.
    ```python
    def substitute(equation, **kwargs):
        pass
    ```

<details>
<summary>Answer</summary>
    ```python
    def substitute(equation, **kwargs):
        for k, v in kwargs.items():
            equation = equation.replace(k, str(v))
        return equation

    equation = "2 * x + y"
    e = substitute(equation, x=3, y=4)
    print(e)
    ```

</details>
