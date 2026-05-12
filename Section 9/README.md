# Section 9 [Video](https://aunedu-my.sharepoint.com/:v:/g/personal/ahmed_abdelaziz_aun_edu_eg/IQBUqQtuSZIATI4SJtGXSA42AcWDqWdSubaur5-GHFnUX4g?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=euike1)

## Pandas Series

1. Create Series with values from 0 to 100, and display it.

<details>
    <summary>Answer</summary>

```python
import pandas as pd

lst = list(range(101))

s = pd.Series(lst)
print(s)
```
</details>

2. Print the rows with index 2, 20, 40 from Q1.

<details>
    <summary>Answer</summary>

```python
import pandas as pd

lst = list(range(101))

s = pd.Series(lst)
print(s[[2,20,40]])
```
</details>

3. Create Series with values 15, 20, 18 and index 'a', 'b', 'c'.

<details>
    <summary>Answer</summary>

```python
import pandas as pd

lst = [15, 20, 18]
pd.Series(lst, index=['a','b','c'])
```
</details>

## Pandas Dataframe

4. Create the following Dataframe and name it `df`:

  Age   |   Height
--------|---------
   10   |  120
   19   |  180
   8    |  90
   12   |  130
   15   |  170

<details>
    <summary>Answer</summary>

```python
import pandas as pd

data = {
    'Age' : [10, 19, 8, 12, 15],
    'Height' : [120, 180, 90, 130, 170]
    }

df = pd.DataFrame(data)
print(df)
```
</details>

5. Print the column 'Height' only for the DataFrame `df`.

<details>
    <summary>Answer</summary>

```python
# using same df as Q4
print(df['Height'])
```
</details>

6. Print the second row only of the DataFrame `df`.
   
<details>
    <summary>Answer</summary>

```python
# using same df as Q4
print(df.iloc[1])
```
</details>

7. Print the second, third and forth rows only of the DataFrame `df`.
   
<details>
    <summary>Answer</summary>

```python
# using same df as Q4
print(df.iloc[[1,2,3]])
```
Another solution
```python
print(df.iloc[1:3])
```
> Note: 3 inclusive!

</details>

8. What is the difference between `loc` and `iloc`?

## Working larger dataset.

9. Load `CSV` File named `data.csv`, name it `dataset`.


<details>
    <summary>Answer</summary>

```python
import pandas as pd

dataset = pd.read_csv('data.csv')
```
</details>

10. Print the first `10` rows of the `dataset`.

<details>
    <summary>Answer</summary>

```python
print(dataset.head(n=10))
```
</details>

11. Print the last `5` rows of the `dataset`.

<details>
    <summary>Answer</summary>

```python
print(dataset.tail(n=5))
```
</details>

12. Print a sample of `15` rows the `dataset`.

<details>
    <summary>Answer</summary>

```python
print(dataset.sample(n=15))
```
</details>

13. Show the `dataset` description and info.

<details>
    <summary>Answer</summary>

```python
print(dataset.describe())

print(dataset.info())
```
</details>

## Data Cleaning

14. How many `NaN` Values are in the dataset?

<details>
    <summary>Answer</summary>

Read the result of info in the previous answer.
</details>

15. Drop any record with `NaN` value then reset index.

<details>
    <summary>Answer</summary>

```python
dataset.dropna(inplace=True) # What does inplace do?
print(dataset) # note the number of rows and the number at last row

dataset.reset_index(inplace=True, drop=True)
print(dataset)
```
</details>

16. Drop duplicated values of `dataset`.

<details>
    <summary>Answer</summary>

```python
dataset = dataset.drop_duplicates()
```
</details>

## Visualization

17. Show the box plot of the `dataset`, does it contain outliers?

<details>
    <summary>Answer</summary>

```python
dataset.boxplot()
```
</details>

18. Normalize and show the box plot again.

<details>
    <summary>Answer</summary>

```python
dataset = (dataset - dataset.mean()) / dataset.std() # see PDF for other normalization methods
dataset.boxplot()
```
</details>

19. Show the histogram of the `dataset`.

<details>
    <summary>Answer</summary>

```python
dataset.hist()
```
</details>

20. Print the correlation between dataset columns.

<details>
    <summary>Answer</summary>

```python
print(dataset.corr())
```
</details>