# Sheet 6

# File IO
1. Write a program that create a new file, then write `Hello from file` to the file.

<details>
    <summary>Answer</summary>

```python
f = open("file.txt", "w")
f.write("Hello from file\n")
f.close()
```
</details>

2. Write a program that append your name to the previous file.

<details>
    <summary>Answer</summary>

```python
with open("file.txt", "a") as f:
    f.write("Ahmed\n")
```
</details>

3. Write a program that write a list of numbers from 1 to 100 to the same file.

<details>
    <summary>Answer</summary>

```python
with open("file.txt", "a") as f:
    for i in range(1, 101):
        f.write(str(i) + '\n')
```
</details>
4. Read the lines from 50 to 60 and print it on the screen.

<details>
    <summary>Answer</summary>

```python
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(*list(map(str.strip, lines[50:60])), sep='\n')
```
</details>

*Note* you should close the file or ues the `with` keyword

# JSON

1. Create a JSON file that has username and password of multiple users.

<details>
    <summary>Answer</summary>

```python
import json

database = {
        "User1" : "password1",
        "User2" : "password2"
        }

with open("file.json", "w") as file:
    json.dump(database, file)
```
</details>

2. Write a program that read the JSON file and print the username and password of the first user.

<details>
    <summary>Answer</summary>

```python
import json

with open("file.json", "r") as file:
    database = dict(json.load(file))
    (user, passwd), *_ = database.items()
    # or any working way to get the first item
    print("USER: {}, PASSWD: {}".format(user, passwd))
```
</details>

3. Write a program that add a new user to the JSON file.

<details>
    <summary>Answer</summary>

```python
import json

with open("file.json", "r") as file:
    database = dict(json.load(file))

database.update({
    "New User" : "Good password"
    })

with open("file.json", "w") as file:
    json.dump(database, file)
```
</details>
4. Prompt the user to enter his username and password and check if the user can log in.

<details>
    <summary>Answer</summary>

```python
import json

with open("file.json", "r") as file:
    database = dict(json.load(file))

user = input("username: ")
passwd = input("password: ")

if user in database and database[user] == passwd:
    print("logging you in")
else:
    print("wrong username or password")
```
</details>

*Note* you should use `json.dump` and `json.load`

# Math Module

1. Write a program that calculate the area of a circle with radius 4.5

<details>
    <summary>Answer</summary>

```python
import math

r = 4.5
print("Area: ", math.pi * r * r)
```
</details>
