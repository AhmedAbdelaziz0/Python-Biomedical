# Sheet 4

1. Write a function that generate a random password, you can use `random`
   package with `random.choice` function

   Your function should take the length of the password and the characters needed
   in the password as arguments.

```python
def generate_password(length, chars):
    pass

generate_password(8, "abcde")
```

<details>
<summary>Answer</summary>

```python
import random

def generate_password(length, chars):
    return "".join(random.choice(chars) for _ in range(length))

passwd = generate_password(8, "abcde")
print(passwd)
```

</details>

2. Use comperehension to generate a string of characters that contains, all
   characters (upper and lower), digits.

   you can use: `ord`, `chr` and `join` functions.
   see `help(ord)`

<details>
<summary>Answer</summary>

```python
s = "".join(
    chr(c)
    for c in list(range(ord("a"), ord("z") + 1))
    + list(range(ord("A"), ord("Z") + 1))
    + list(range(ord("0"), ord("9") + 1))
)
```

```python
# another way
s = "".join( chr(ord('a') + i) for i in range(26) )
s += s.upper()
s += "".join( chr(ord('0') + i) for i in range(10) )
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

4. Write a function that finds the average of a list of numbers passed as arguments.

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

5. Write a function that substitutes variables into a mathematical equation
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
