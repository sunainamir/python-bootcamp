# What is a Tuple?

- A tuple is a data structure that stores groups of elements in sequential order.
- Tuples are immutable, which means their elements cannot be changed after creation.

## Syntax

```python

()

```

## Sample Code

```python

colors = ("Red","Green","Blue")

print(colors)

```

## Sample Output

```

('Red', 'Green', 'Blue')

```

## Key Points

- Tuples store multiple elements.
- Elements are separated by commas.
- Tuples use parentheses ().
- Elements are ordered.
- Tuples can store different data types.
- Tuples are immutable.

## AI Connection

AI uses tuples to store fixed information such as image dimensions, RGB values, coordinates, and model input shapes that should never change.

# Single Element Tuple

- A tuple with one element must contain a comma after the value.

## Syntax

```python

(value,)

```

## Sample Code

```python

number = (10,)

print(type(number))

```

## Sample Output

```

<class 'tuple'>

```

## Key Points

- A comma creates a tuple.
- Parentheses alone do not create a tuple.
- Without a comma, Python treats it as the original data type.

## AI Connection

AI sometimes stores one fixed value as a tuple to maintain consistency with other tuple-based data.

# Tuple Indexing

- Tuple indexing is used to access elements by their position.

## Syntax

```python

tuple_name[index]

```

## Sample Code

```python

fruits = ("Apple","Banana","Orange")

print(fruits[1])

```

## Sample Output

```

Banana

```

## Key Points

- Index starts from 0.
- Supports positive and negative indexing.
- Cannot modify elements using indexing.

## AI Connection

AI accesses specific values from tuples such as coordinates and fixed labels using indexing.

# Tuple Slicing

- Tuple slicing is used to access multiple elements from a tuple.

## Syntax

```python

tuple_name[start:end:step]

```

## Sample Code

```python

numbers = (10,20,30,40,50)

print(numbers[1:4])

```

## Sample Output

```

(20, 30, 40)

```

## Key Points

- Start index is included.
- End index is excluded.
- Supports step values.
- Returns a new tuple.

## AI Connection

AI slices tuples while selecting portions of fixed datasets or coordinates.

# count()

- count() returns how many times a value appears in a tuple.

## Syntax

```python

tuple_name.count(value)

```

## Sample Code

```python

numbers = (10,20,10,30,10)

print(numbers.count(10))

```

## Sample Output

```

3

```

## Key Points

- Counts occurrences of a value.
- Returns an integer.
- Does not modify the tuple.

## AI Connection

AI counts repeated labels or values inside fixed datasets.

# index()

- index() returns the index of the first occurrence of a value.

## Syntax

```python

tuple_name.index(value)

```

## Sample Code

```python

numbers = (10,20,30,20)

print(numbers.index(20))

```

## Sample Output

```

1

```

## Key Points

- Returns the first matching index.
- Raises ValueError if the value is not found.
- Does not modify the tuple.

## AI Connection

AI locates labels, classes, or coordinates stored inside tuples.

# Tuple Packing

- Tuple packing stores multiple values into one tuple automatically.

## Syntax

```python

tuple_name = value1, value2, value3

```

## Sample Code

```python

student = "Sunaina",18,"Gilgit"

print(student)

```

## Sample Output

```

('Sunaina', 18, 'Gilgit')

```

## Key Points

- Parentheses are optional.
- Multiple values are packed into one tuple.
- Packing makes code shorter.

## AI Connection

AI packs related values together such as coordinates, RGB values, and prediction results.

# Tuple Unpacking

- Tuple unpacking stores tuple elements into separate variables.

## Syntax

```python

variable1, variable2 = tuple_name

```

## Sample Code

```python

student = ("Sunaina",18)

name, age = student

print(name)
print(age)

```

## Sample Output

```

Sunaina
18

```

## Key Points

- Number of variables must equal the number of tuple elements.
- Too many or too few variables raise ValueError.
- Makes code cleaner and easier to read.

## AI Connection

AI unpacks coordinates, model outputs, and prediction values into separate variables for further processing.
