# Sheet 1

The target of this sheet is to get familiar with your IDE (such as spyder or vs
code) and python.

- Input/Output
- Variables, types, casting
- Operators
- Strings


1. Write python code that asks the user for his name and print `Hello <name>`

2. Write python code that asks the user for two floating points numbers and print their sum

3. What is the ouput of the following code (run the code to see the output)?:

```python
x = 10
y = 20

z = x ** 2 * y
print(z)
```

4. What is the output of the following code (run the code to see the output)?:

```python
x = "10"
y = 20

print(type(x), type(y))
```

5. In `print` function what does 'sep' and 'end' do?

```python
x = 1
y = 2
print(x, y, sep=" + ", end=" = ")
print(3)
```

6. What is the output of this code?

```python
x = "10"
y = 'abc'
print(x.isdigit(), y.isdigit())
```

7. Use 3 different ways of string format to print the following string:
`remainder is <remainder> and quotient is <quotient>` use the variables x, y

```python
x = 8
y = 12

remainder =  # TODO compute the remainder
quotient =  # TODO compute the quotient

print()  # TODO 1st way
print()  # TODO 2nd way
print()  # TODO 3rd way 
```

<details>
<summary>Hint</summary>

```python
print("{}, {}".format("Hello", "World")) # Hello, World
print("{0}, {0}".format("Hello", "World")) # Hello, Hello
h = "Hello"
w = "World"
print(f"{h}, {w}") # Hello, World
```

</details>

8. [challenge] What is the output of the following code, and what does it do?

```python
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter a Choice (1, 2)): ")
choice = int(choice) - 1

temperature = input("Enter a temperature: ")
temperature = float(temperature)

converted = (temperature * 9 / 5 + 32) * (1 - choice) + ((temperature - 32) * 5 / 9) * choice

print(f"Result: {converted}")
```
