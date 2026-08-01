# Exercise 1 : Create a tuple of five colors.

Print:
- First color
- Last color

## Sample Code

```python

colors = ("Red","Blue","Green","Black","Yellow")
print(colors[0])
print(colors[4])

```

## Sample Output

```
Red
Yellow

```

# Exercise 2 : Create a tuple of five numbers.

Print:
- Second number
- Fourth number

## Sample Code

```python

numbers = (1,2,3,4,5,6)
print(numbers[1])
print(numbers[3])

```

## Sample Output

```
2
4

```

# Exercise 3 : Use negative indexing to print:
- Last element
- Second last element

## Sample Code

```python

numbers = (1,2,3,4,5,6)
print(numbers[-1])
print(numbers[-2])

```

## Sample Output

```
6
5

```

# Exercise 4 : Print the first three elements using slicing.

## Sample Code

```python

numbers = (1,2,3,4,5,6)
print(numbers[:3])


```

## Sample Output

```
(1, 2, 3)

```

# Exercise 5 : Print every second element.

## Sample Code

```python

numbers = (1,2,3,4,5,6,7,8)
print(numbers[::2])


```

## Sample Output

```
(1, 3, 5, 7)

```

# Exercise 6 : Create a single element tuple.

## Sample Code

```python

number = (100,)
print(number)


```

## Sample Output

```
100

```

# Exercise 7 : Predict the output.

```python

x = (100)

print(type(x))

```

## Sample Output

```
<class 'int'>

```

# Exercise 8 : Predict th output .

```python

x = ("Python",)

print(type(x))


```

## Sample Output

```
<class 'tuple'>

```

# Exercise 9 : Find the index of "Python".

languages = ("C","C++","Python","Java")

## Sample Code

```python

languages = ("C","C++","Python","Java")
print(languages.index("Python"))

```

## Sample Output

```
2

```

# Exercise 10 : Predict the output.

```python

numbers = (10,20,30,40,50)

print(numbers[1:4])

```

## Sample Output

```
(20, 30, 40)

```

# Exercise 11 : Predict the output.

```python

letters = ("A","B","C","D","E","F")

print(letters[::-1])

```

## Sample Output

```
('F', 'E', 'D', 'C', 'B', 'A')

```

# Exercise 12 : Tuple Packing.
Store:

Name
Age
City

Print the tuple.

## Sample Code

```python

student_data = ("Ali",18,"Gilgit")
print(student_data)


```

## Sample Output

```
('Ali', 18, 'Gilgit')

```

# Exercise 13 : Tuple Unpacking.

student = ("Ali",18,"Gilgit")

## Sample Code

```python
student_data = ("Ali",18,"Gilgit")
name , age , city = student_data
print(name)
print(age)
print(city)

```

## Sample Output

```
Ali
18
Gilgit

```

# Exercise 14 : Predict the output.

```python

student = ("Ali",18)

name,age,city = student

```

## Sample Output

```
ValueError: not enough values to unpack (expected 3, got 2)

```

# Exercise 15 : Predict the output.

```python

student = ("Ali",18,"Gilgit")

name,age = student

```

## Sample Output

```
ValueError: too many values to unpack (expected 2, got 3)

```

# Exercise 16 : Predict the output.

```python

numbers = (10,20,30)

print(numbers.count(100))

```

## Sample Output

```
0

```
# Exercise 17 : Predict the output.

```python

numbers = (10,20,30)

print(numbers.index(30))

```

## Sample Output

```
2

```
# Exercise 18 : Predict the output.

```python

numbers = (10,20,30)

numbers[1] = 50

```

## Sample Output

```
TypeError: 'tuple' object does not support item assignment

```
# Exercise 19 : Predict the output.

```python

numbers = (1,2,4,3,2,4,5,2,3,4)
print(numbers.count(2))

```

## Sample Output

```
3

```
# Exercise 20 : Predict the output.

```python

student = ("Sunaina",17,"Gilgit","A+")

name, age, city, grade = student

print(name)
print(student[2])
print(student[-1])
print(student[:2])
print(student.count("Gilgit"))

```

## Sample Output

```
Sunaina
Gilgit
A+
('Sunaina', 17)
1

```