# Sheet 1

The target of this sheet is to get familiar with your IDE (such as spyder or vs code) and python.

- Input/Output
- Variables, types, casting
- Operators
- Strings

## Indentation

In any programming language there is a way to define the start and end of a
coding block, for example in C++ it was curly brackets `{}`.
In python it is the indentation, line that are aligned are togather.

Lets see an example of finding if a number is even or odd:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = input("Enter a number")
if is_even(num):
    print("The number you entered is even")
else:
    print("The number you entered is odd")
```

> Note that a single space will give you indentation error so copy and pasting is not adviced.
> also spaces ` ` are not the same as tabs, when you want to make indentation use tab button on your keyboard.

---


1. Write python code that asks the user for his name and print `Hello <name>`

<details>
<summary>Answer</summary>

```python
name = input("Enter your name: ")
print(f"Hello {name}")
```

</details>

2. Write python code that asks the user for two floating points numbers and print their sum


<details>
<summary>Answer</summary>

```python
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
print(x + y)
```

</details>

3. What is the ouput of the following code (run the code to see the output)?:

```python
x = 10
y = 20

z = x ** 2 * y
print(z)
```

<details>
<summary>Answer</summary>

```
2000
```

</details>

4. What is the output of the following code (run the code to see the output)?:

```python
x = "10"
y = 20

print(type(x), type(y))
```

<details>
<summary>Answer</summary>

```
<class 'str'> <class 'int'>
```

</details>

5. In `print` function what does 'sep' and 'end' do?

```python
x = 1
y = 2
print(x, y, sep=" + ", end=" = ")
print(3)
```

<details>
<summary>Answer</summary>

```
1 + 2 = 3

sep: separator between elements
end: is printed at the end of the line
```

</details>

6. What is the output of this code?

```python
x = "10"
y = 'abc'
print(x.isdigit(), y.isdigit())
```

<details>
<summary>Answer</summary>

```
True False
```

</details>

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

<details>
<summary>Answer</summary>

```python
remainder = x % y
quotient = x // y

print("remainder is {} and quotient is {}".format(remainder, quotient))
print("remainder is {0} and quotient is {1}".format(remainder, quotient))
print(f"remainder is {remainder} and quotient is {quotient}")
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

<details>
<summary>Answer</summary>

```
This code converts between celsius and fahrenheit.
It uses choice to determine the conversion.
Instead of using if statements,
    it multipy the result by 1 - choice and the other by choice,
    that way one choice will be suppressed
```

</details>
