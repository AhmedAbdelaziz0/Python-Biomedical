# Sheet 3

## Exercise 1: Running Time Calculator
Write a program that:
- Repeatedly asks the user for numeric input representing 10 km run times
- Stops when the user enters 0 or presses Enter without input
- Calculates and prints the average time and number of runs
- Use variables `number_of_runs` and `total_time` to track the data

Example output might look like:
```
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 0
Average of 17.5, over 2 runs
```

```python
# Your code here
number_of_runs = 0
total_time = 0
```

<details>
<summary>Answer</summary>

```python
total = 0
count = 0

while True:
    number = input("Enter ")
    if number in ['0', '']:
        break

    if number.isdigit():
        print("Enter valid number")
        continue

    number = int(number)

    total = total + number
    count += 1
    print(f"total {total}, count: {count}")

print(total / count)
```

</details>

---

## Exercise 2: Number Cropping
Write a program that:
- Starts with a float `fl_num = 1234.5678`
- Uses two integers `bef_int_num = 2` and `aft_int_num = 3`
- Creates a new float with 'bef_int_num' digits before the decimal point and 'aft_int_num' digits after it
- Prints the result (should be 34.567)

```python
# Your code here
fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3
```

<details>
<summary>Answer</summary>

```python
fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

num = str(fl_num)
left, right = num.split('.')
left = left[bef_int_num:]
right = right[:aft_int_num]
num = left + '.' + right
fl_num = float(num)
```

</details>

---

## Exercise 3: String Sorting
Write a program that:
- Starts with the string `s = "Tom Jerry Harry"`
- Breaks it into individual words
- Sorts the words alphabetically
- Joins them back with commas between names
- Prints the result (should be "Harry, Jerry, Tom")

```python
# Your code here
s = "Tom Jerry Harry"
```

<details>

<summary>Answer</summary>

```python
s = "Tom Jerry Harry"

names = s.split()

combined = sorted(names)

combined = ", ".join(combined)

print(combined)
```

</details>

---

## Exercise 4: Even/Odd Index Sums
Write a program that:
- Starts with a list `sequence = [10, 20, 30, 40, 50, 60]`
- Calculates the sum of numbers at even indexes (0, 2, 4, etc.) in `even_sum`
- Calculates the sum of numbers at odd indexes (1, 3, 5, etc.) in `odd_sum`
- Prints both sums (should be 90 and 120)

```python
# Your code here
sequence = [10, 20, 30, 40, 50, 60]
even_sum = 0
odd_sum = 0
```

<details>
<summary>Answer</summary>

```python
sequence = [10, 20, 30, 40, 50, 60]
even_sum = 0
odd_sum = 0


even_sum = sum(sequence[0::2]) # start:end:step
odd_sum = sum(sequence[1::2])

print(even_sum, odd_sum)
```

</details>

---

## Exercise 5: Simple Login System
Write a program that:
- Uses a dictionary `USERS = {'user1': 'password1', 'user2': 'password2'}`
- Asks user for a username and stores it in `name_input`
- Asks user for a password and stores it in `pass_input`
- Checks if credentials match
- Prints success message if they match, error message if they don't
- Note: In real systems, never store unencrypted passwords!

```python
# Your code here
USERS = {'user1': 'password1', 'user2': 'password2'}
```

<details>
<summary>Answer</summary>

```python
USERS = {'user1': 'password1', 'user2': 'password2'}

name = input("Username: ")
passwd = input("Password: ")

if name in USERS and passwd == USERS[name]:
    print("Login successful")
else:
    print("Invalid username or password")

```

</details>

---

## Exercise 6: Dictionary Merger
Write a program that:
- given list of dictionaries:
- Combines all dictionaries from the list into `fin_di`
- Keeps the most recently merged value for duplicate keys
- Prints the result (should be {'a': 2, 'b': 3})

```python
# Your code here
d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}
all_dicts = [d1, d2, d3]
fin_di = {}
```

<details>
<summary>Answer</summary>
    
```python
d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}
all_dicts = [d1, d2, d3]
fin_di = {}

for d in all_dicts:
    fin_di.update(d)

print(fin_di)
```

</details>

---

## Exercise 7: Unique Number Counter
Write a program that:
- Tests two lists:
  - `numbers1 = [10, 20, 30]`
  - `numbers2 = [10, 20, 30, 10, 20, 30]`
- For each list, counts how many unique numbers it contains
- Prints the results (should be 3 and 3)

```python
# Your code here
numbers1 = [10, 20, 30]
numbers2 = [10, 20, 30, 10, 20, 30]
```

<details>
<summary>Answer</summary>

```python
numbers1 = [10, 20, 30]
numbers2 = [10, 20, 30, 10, 20, 30]

num1 = set(numbers1)
num2 = set(numbers1)

print(num1, num2)
```

</details>
