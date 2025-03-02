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

2. Complete the following code:

```python
count = int(input("Enter count: "))
char = input("Enter character to repeat: ")

print() # print the character repeated <count> times
```

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

4. Comment on the result of the following code:

```python
my_str = "    hello           world          "

my_str = my_str.strip()
my_str = my_str.title()
sub_strs = my_str.split(' ')
my_str = sub_strs[0].upper() + ', ' + "python".title() + '!'
print(my_str)
```

5. Write python code that replaces the word "world" with your name in single
   line.

```python
s = "Hello world"

# Your code goes here

print(s)
```

6. Write python code that find the index of the second occurrence of the letter "o" in the string "Hello world"

7. Write python code that count the number of occurrences of the letter "o" in the string "Hello world"


8. What is the output of the following code:

```python
a = 1 / 3
b = 2 / 3

# Note the rounding
print(f"{a:.4f} + {b:.4f} = {a + b:.4f}")

print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(chr(72) + chr(111) + chr(119) + chr(33))
```

9. What is the output of the following code:

```python
s = "Hello world"

print(s[-5:] + ' ' + s[0:5])
```

---

Lists

**Notes:**
1. Lists are mutable.
2. Lists are heterogeneous.

**Questions:**

1. Start with empty list, and append three different numbers to it `(1, 2, 3)`

2. extend the list from the previous code with new list `[5, 6, 7]`

3. insert at index `3` the value `4` 

4. remove the last element.

5. remove the element with value `6`.

6. what is the index of the value 3

7. reverse the list

8. new list = the first 3 elements of the current list.

9. What is the difference between `list.sort` and `sorted`

```python
lst = [2, 4, 1, 5, -1]
print(sorted(lst))

lst.sort()
print(lst)
```

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
