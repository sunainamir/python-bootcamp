# What is a List?

- A list is a data structure used to store multiple values in a single variable.

## Syntax

```python
list_name = [elements]
```

## Sample Code

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

## Sample Output

```
['Apple', 'Banana', 'Mango']
```

## Key Points

- Lists can store multiple values.
- Lists can store different data types.
- Elements are separated by commas.
- Lists are ordered.
- Lists are mutable (can be changed).

## AI Connection

- AI uses lists to store datasets, labels, predictions, and model outputs.
- Lists help organize large amounts of information in one variable.

---

# List Indexing

- Every element in a list has an index.
- Indexing starts from **0**.

## Syntax

```python
list_name[index]
```

## Sample Code

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[2])
```

## Sample Output

```
Apple
Mango
```

## Key Points

- First element has index 0.
- Indexing provides direct access to elements.
- Accessing an invalid index raises an IndexError.

## AI Connection

- AI programs use indexing to access specific images, labels, or data samples.

---

# Negative Indexing

- Negative indexing accesses elements from the end of the list.

## Syntax

```python
list_name[-index]
```

## Sample Code

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
print(fruits[-2])
```

## Sample Output

```
Mango
Banana
```

## Key Points

- -1 refers to the last element.
- -2 refers to the second last element.
- Negative indexing makes accessing end elements easy.

## AI Connection

- AI programs often use negative indexing to retrieve the latest prediction or recent result.

---

# List Slicing

- Slicing returns multiple elements from a list.

## Syntax

```python
list_name[start:stop]
```

## Sample Code

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

## Sample Output

```
[20, 30, 40]
```

## Key Points

- Start index is included.
- Stop index is excluded.
- Slicing returns a new list.
- If stop exceeds list length, Python does not raise an error.

## AI Connection

- AI uses slicing to divide datasets into training and testing sets.

---

# Slicing with Step

- Step controls how many positions Python moves after selecting an element.

## Syntax

```python
list_name[start:stop:step]
```

## Sample Code

```python
numbers = [10,20,30,40,50,60]

print(numbers[0:6:2])
```

## Sample Output

```
[10, 30, 50]
```

## Key Points

- Start is included.
- Stop is excluded.
- Step skips elements according to the given value.

## AI Connection

- AI uses step slicing when sampling data or selecting every nth element.

---

# append()

- append() adds one element at the end of the list.

## Syntax

```python
list_name.append(value)
```

## Sample Code

```python
numbers = [10,20]

numbers.append(30)

print(numbers)
```

## Sample Output

```
[10, 20, 30]
```

## Key Points

- Adds only one element.
- Increases list length by one.
- Can also append another list as a single nested element.

## AI Connection

- AI uses append() to store predictions, losses, or new data during processing.

---

# extend()

- extend() adds each element of another iterable individually.

## Syntax

```python
list_name.extend(iterable)
```

## Sample Code

```python
numbers = [10,20]

numbers.extend([30,40])

print(numbers)
```

## Sample Output

```
[10, 20, 30, 40]
```

## Key Points

- Adds multiple elements.
- Does not create a nested list.
- Increases list length according to the number of added elements.

## AI Connection

- AI combines multiple datasets or batches using extend().

---

# insert()

- insert() inserts an element before the specified index.

## Syntax

```python
list_name.insert(index, value)
```

## Sample Code

```python
numbers = [10,30]

numbers.insert(1,20)

print(numbers)
```

## Sample Output

```
[10, 20, 30]
```

## Key Points

- Takes two parameters: index and value.
- Existing elements shift to the right.
- If index is greater than the list length, Python inserts the element at the end.
- Negative indexes are also allowed.

## AI Connection

- AI uses insert() to place special tokens or values at specific positions.

---

# remove()

- remove() removes the first matching value from the list.

## Syntax

```python
list_name.remove(value)
```

## Sample Code

```python
numbers = [10,20,30,20]

numbers.remove(20)

print(numbers)
```

## Sample Output

```
[10, 30, 20]
```

## Key Points

- Removes the first matching value.
- Removes by value, not by index.
- Raises an error if the value does not exist.

## AI Connection

- AI removes unwanted labels or duplicate values from datasets.

---

# pop()

- pop() removes and returns an element.

## Syntax

```python
list_name.pop()
```

or

```python
list_name.pop(index)
```

## Sample Code

```python
numbers = [10,20,30]

last = numbers.pop()

print(last)
print(numbers)
```

## Sample Output

```
30
[10, 20]
```

## Key Points

- Removes the last element by default.
- Can remove an element using its index.
- Returns the removed value.

## AI Connection

- AI uses pop() while implementing stacks, backtracking, and search algorithms.

---

# clear()

- clear() removes all elements from the list.

## Syntax

```python
list_name.clear()
```

## Sample Code

```python
numbers = [10,20,30]

numbers.clear()

print(numbers)
```

## Sample Output

```
[]
```

## Key Points

- Empties the list completely.
- The list still exists after clearing.

## AI Connection

- AI clears temporary data after processing to save memory.

---

# del Statement

- del deletes elements or an entire list.

## Syntax

```python
del list_name[index]
```

## Sample Code

```python
numbers = [10,20,30]

del numbers[1]

print(numbers)
```

## Sample Output

```
[10, 30]
```

## Key Points

- Deletes by index.
- Can delete slices.
- Can delete the whole list.

## AI Connection

- AI removes unnecessary data structures to optimize memory usage.

# len()

- len() returns the total number of elements in a list.

## Syntax

```python

len(list_name)

```

## Sample Code

```python

fruits = ["Apple","Banana","Orange"]

print(len(fruits))

```

## Sample Output

```
3

```

## Key Points

- Returns the total number of elements.
- Returns an integer value.
- It does not count characters inside an element.
- Works with lists, strings, tuples and dictionaries.

## AI Connection

AI uses len() to count the number of samples in a dataset, predictions, or training batches.

# count()

- count() returns how many times a specific value appears in a list.

## Syntax

```python

list_name.count(value)

```

## Sample Code

```python

numbers = [2,5,2,8,2]

print(numbers.count(2))

```

## Sample Output

```
3

```

## Key Points

- Counts occurrences of a value.
- Returns 0 if the value is not found.
- Searches the complete list.
- Useful for repeated elements.

## AI Connection

AI uses count() to count labels, classes, or repeated values in datasets.

# index()

- index() returns the index of the first occurrence of a value.

## Syntax

```python

list_name.index(value)

```

## Sample Code

```python

fruits = ["Apple","Banana","Orange"]

print(fruits.index("Banana"))

```

## Sample Output

```
1

```

## Key Points

- Returns the first matching index.
- Index starts from 0.
- Gives ValueError if the value is not found.
- Useful for locating elements.

## AI Connection

AI uses index() to locate labels, classes, or words inside datasets.

# sort()

- sort() arranges list elements in ascending order by default.

## Syntax

```python

list_name.sort()

```

## Sample Code

```python

numbers = [8,4,1,6]

numbers.sort()

print(numbers)

```

## Sample Output

```
[1, 4, 6, 8]

```

## Key Points

- Sorts the original list.
- Default order is ascending.
- Can sort strings alphabetically.
- Use reverse=True for descending order.

## AI Connection

AI sorts prediction scores, confidence values, and datasets before analysis.

# reverse()

- reverse() reverses the current order of elements in a list.

## Syntax

```python

list_name.reverse()

```

## Sample Code

```python

numbers = [10,20,30,40]

numbers.reverse()

print(numbers)

```

## Sample Output

```
[40, 30, 20, 10]

```

## Key Points

- Reverses the existing order.
- Does not sort the list.
- Changes the original list.
- Useful for displaying data in reverse order.

## AI Connection

AI may reverse sequences while processing time-series data or ordered outputs.

# copy()

- copy() creates a new list with the same elements.

## Syntax

```python

new_list = old_list.copy()

```

## Sample Code

```python

list1 = [10,20,30]

list2 = list1.copy()

print(list2)

```

## Sample Output

```
[10, 20, 30]

```

## Key Points

- Creates a separate copy of a list.
- Changes in the copied list do not affect the original list.
- Prevents accidental modification of original data.
- Useful for creating backups.

## AI Connection

AI creates copies of datasets before preprocessing or data augmentation to preserve the original data.

# Membership Operators (in, not in)

- Membership operators check whether an element exists in a list.

## Syntax

```python

value in list_name

value not in list_name

```

## Sample Code

```python

fruits = ["Apple","Banana","Orange"]

print("Apple" in fruits)
print("Mango" not in fruits)

```

## Sample Output

```
True
True

```

## Key Points

- in checks whether an element exists.
- not in checks whether an element does not exist.
- Returns True or False.
- Useful for making decisions.

## AI Connection

AI checks whether a label, word, class, or feature exists before processing data.
