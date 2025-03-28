# Sheet 5

1. Generate the following lists using the `range` function:
   - `[0, 1, 2, 3, 4, 5]`
   - `[4, 6, 8, 10]`
   - `[10, 9, 8, 7, 6]`
   - `[10, 5, 0, -5, -10]`

2. What is the output of the following code, and explain the rule of the `zip` function?
   ```python
   x_coor = [1, 2, 3, 4, 5]
   y_coor = [2, 4, 6, 8, 10]
   z_coor = [0, -1, -2, -3, -4]

   points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
   ```

3. What is the output of the following code? Use `map` function to get the same output.
   ```python
   def apply(lst, fn):
       result = []
       for elem in lst:
           result.append(fn(elem))
       return result

   def add_1(num):
       return num + 1

   r = apply([1, 2, 3], add_1)
   print(r)
   ```

4. Modify the code in question 3 to use a lambda function.  
   *Hint:*
   ```python
   lambda <input param> : return value
   ```

5. What is the output of the following code?
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

6. Using shorthand if-else and list comprehension, generate a list indicating whether the corresponding number in the other list is even.
   ```python
   x = [1, 2, 10, 13, 1]
   # output = [False, True, True, False, False]
   ```

7. Explain the rule of each line in the following class, then modify the class
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
