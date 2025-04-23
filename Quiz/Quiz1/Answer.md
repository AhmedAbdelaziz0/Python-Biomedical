# Quiz 1 Answer

## Question 1

steps:
1. Get input from user in a while loop.
2. Convert input to integer.
3. If input is less than 0, break the loop.
4. If input is not in the list, add it to the list (unique).
5. Get unique pairs from the list by using nested for loop or list comprehension.

```python
lst = []

while True:
    n = input()
    n = int(n)
    if n < 0:
        break
    if n not in lst:
        lst.append(n)

# pairs = [tuple(sorted((i, j))) for i in unique for j in unique]
# unique_pirs = set(pairs)
unique_pairs = []

for i in range(len(lst)):
    for j in range(i, len(lst)):
        unique_pairs.append((lst[i], lst[j]))


print(unique_pairs)
```

## Question 2

**Q**

```python
text = "         You must get at least {:.1f} in that course.       ".format(3.25)
print(text)
```

**A**

substitute 3.25 in the place holder.
in place holder, .1f means 1 decimal place.

Spaces must be visible.
```python
         You must get at least 3.2 in that course. 
```

**Q**

```python
text = text.strip()
print(text)
```

**A**

Strip removes leading and trailing characters

```
You must get at least 3.2 in that course. 
```

**Q**
```python
text = text.replace("must", "should")
print(text)
```

**A**

```
You should get at least 3.2 in that course.
```

**Q**
```python
text = text.title()
print(text)
```

**A**

Upper and lower case must be visible.

```
You Should Get At Least 3.2 In That Course.
```

**Q**
```python
print (text[15:5:-1])
```

**A**

```
A teG dluo
```
