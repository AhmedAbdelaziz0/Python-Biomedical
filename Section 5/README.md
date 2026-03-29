# Sheet 5

1. Explain the rule of each line in the following class, then modify the class
   to be Point3d, and add subtract method.

```python
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add(self, p):
        self.x += p.x
        self.y += p.y

    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y

        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5
        return dist


p1 = Point2D(1, 2)
p2 = Point2D(4, -2)

p2.add(p1)

print(p2)
print(p1.distance(p2))
```

<details>
<summary>Answer</summary>

```python
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add(self, p):
        self.x += p.x
        self.y += p.y
        self.z += p.z

    def subtract(self, p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z

    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        delta_z = self.y - p.z

        dist = (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5
        return dist
```

</details>

2. Modify the code in question 3 to use a lambda function.  
   *Hint:*
   ```python
   lambda <input param> : return value
   ```

<details>
<summary>Answer</summary>

```python
r = list(map(lambda x: x + 1, [1, 2, 3]))
print(r)
```

</details>

3. Using short hand if: write single statement that print whether a string `A`
   contain numeric value.

<details>
<summary>Answer</summary>

```python
if A.isnumeric(): print(f"{A} is a number")
```

</details>

4. What is the output of the following code:
```python
lst = [i ** 2 for i in range(10)]
for idx, value in enumerate(lst):
    print(f"{idx} - {value}")
```

<details>
<summary>Answer</summary>

```
0 - 0
1 - 1
2 - 4
3 - 9
4 - 16
5 - 25
6 - 36
7 - 49
8 - 64
9 - 81
```

</details>

5. Convert the Library system into single class.
