# Sheet 2

## Strings

**Note:** 
1. String is a class, which means it has methods and attributes.
2. String is immutable (which means you can't change it).
3. String has some overloaded operator such as `+` and `*`

**Questions:**

1. Complete the following code, using operators instead of string format:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print() # <name> <age>
```


<details>
<summary>Answer</summary>

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name + ' ' + age)
```

</details>

2. Complete the following code:

```python
count = int(input("Enter count: "))
char = input("Enter character to repeat: ")

print() # print the character repeated <count> times
```

<details>
<summary>Answer</summary>

```python
count = int(input("Enter count: "))
char = input("Enter character to repeat: ")

print(char * count)
```

</details>

3. Write python code that retrieve the name of the file, also print the file
   type

```python
file_name = "/home/user/projects/my_project/file.txt"

# Your code goes here
```

<details>
<summary>Hint</summary>

You may use split method to split the file name from the path
and use indexing to get the last element.

</details>


<details>
<summary>Answer</summary>

```python
file_name = "/home/user/projects/my_project/file.txt"

file_split = file_name.split('/')[-1]
file_name, file_type = file_split.split('.')

print(file_name, file_type)
```

</details>

4. Comment on the result of the following code:

```python
my_str = "    hello           world          "

my_str = my_str.strip()
my_str = my_str.title()
sub_strs = my_str.split(' ')
my_str = sub_strs[0].upper() + ', ' + "python".title() + '!'
print(my_str)
```

<details>
<summary>Answer</summary>

```
1. Strips the leading and trailing spaces.
2. Converts the string to title case. (first letter of each word is uppercase)
3. Splits the string into a list of substrings.
4. Converts the first substring to uppercase and concatenates it with "python".

hello           world
Hello           World
['Hello', '', '', '', '', '', '', '', '', '', '', 'World']
Hello, Python!
```

</details>

5. Write python code that replaces the word "world" with your name in single
   line.

```python
s = "Hello world"

# Your code goes here

print(s)
```

<details>
<summary>Answer</summary>

```python
s = "Hello world"

s = s.replace('world', 'Ahmed')

print(s)
```

</details>

6. Write python code that find the index of the second occurrence of the letter "o" in the string "Hello world"

<details>
<summary>Answer</summary>

```python
s = "Hello world"

print(s.find('o', s.find('o') + 1))
```

</details>

7. Write python code that count the number of occurrences of the letter "o" in the string "Hello world"

<details>
<summary>Answer</summary>

```python
s = "Hello world"

print(s.count('o'))
```

</details>

8. What is the output of the following code:

```python
a = 1 / 3
b = 2 / 3

# Note the rounding
print(f"{a:.4f} + {b:.4f} = {a + b:.4f}")

print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(chr(72) + chr(111) + chr(119) + chr(33))
```

<details>
<summary>Answer</summary>

```
0.3333 + 0.6667 = 1.0000

# this is an issue with floating point number representation in the cpu
0.1 + 0.2 = 0.30000000000000004 

# casting to char using chr (you don't need to the memorize corresponding to it)
How!
```

</details>

---

Lists

**Notes:**
1. Lists are mutable.
2. Lists are heterogeneous.

**Questions:**

1. Start with empty list, and append three different numbers to it `(1, 2, 3)`

<details>
<summary>Answer</summary>

```python
lst = []

lst.append(1)
lst.append(2)
lst.append(3)
# lst = [1, 2, 3]
```

</details>

2. extend the list from the previous code with new list `[5, 6, 7]`

<details>
<summary>Answer</summary>

```python
lst.extend([5, 6, 7])
# lst = [1, 2, 3, 5, 6, 7]
```

</details>

3. insert at index `3` the value `4` 

<details>
<summary>Answer</summary>

```python
lst.insert(3, 4)
# lst = [1, 2, 3, 4, 5, 6, 7]
```

</details>

4. remove the last element.

<details>
<summary>Answer</summary>

```python
lst.pop()
# lst = [1, 2, 3, 4, 5, 6]
```

</details>

5. remove the element with value `6`.

<details>
<summary>Answer</summary>

```python
lst.remove(6)
# lst = [1, 2, 3, 4, 5]
```

</details>

6. what is the index of the value 3

<details>
<summary>Answer</summary>

```python
print(lst.index(3))
# 2
```

</details>

7. reverse the list

<details>
<summary>Answer</summary>

```python
lst.reverse()
# lst = [5, 4, 3, 2, 1]
```

</details>

8. new list = the first 3 elements of the current list.

<details>
<summary>Answer</summary>

```python
new_list = lst[:3]
# new_list = [1, 2, 3]
```

</details>

9. What is the difference between `list.sort` and `sorted`

```python
lst = [2, 4, 1, 5, -1]
print(sorted(lst))

lst.sort()
print(lst)
```

<details>
<summary>Answer</summary>

```
lst.sort() will change the list in place,
    while sorted will return a new list.
```

</details>

10. The following code aims to create a list that have three different lists:
what is wrong with that code, fix it

```python
lst1 = []
lst2 = [1,2,3]

lst1.append(lst2)
lst1.append(lst2)
lst1.append(lst2)

lst1[0][0] = 10

print(lst1)
```

<details>
<summary>Answer</summary>

```python
lst1 = []
lst2 = [1,2,3]

lst1.append(lst2.copy())
lst1.append(lst2.copy())
lst1.append(lst2[:])

lst1[0][0] = 10

print(lst1)
```

</details>
