# Exercise 1 : Create a list of 5 favorite fruits and print:
- First fruit
- Last fruit

## Sample Code 

```python

fruits = ["Apple","Banana","Orange","Grapes","Cherry"]
print(fruits[0])
print(fruits[4])

```

## Sample Output

```
Apple
Cherry

```

# Exercise 2 :  Create a list of 5 numbers and print:
- Second number
- Fourth number


## Sample Code 

```python

numbers = [1,2,3,4,5]
print(numbers[1])
print(numbers[3])

```

## Sample Output

```
2
4

```

# Exercise 3 :  Use negative indexing to print:
- Last element
- Second last element


## Sample Code 

```python

number = [1,2,3,4,5]
print(number[-1])
print(number[-2])

```

## Sample Output

```
5
4

```

# Exercise 4 :  Create a list of cities and print the first three cities using slicing.


## Sample Code 

```python

cities = ["Gilgit","Lahore","islamabad","Karachi","Sindh"]
print(cities[:3])

```

## Sample Output

```
['Gilgit', 'Lahore', 'islamabad']

```

# Exercise 5 :  Print every second element of this list.

numbers = [10,20,30,40,50,60,70,80]


## Sample Code 

```python

numbers = [10,20,30,40,50,60,70,80]
print(numbers[1:9:2])

```

## Sample Output

```
[20, 40, 60, 80]

```

# Exercise 6 : Create an empty list . Append these values one by one:
10
20
30
40

Print the final list.


## Sample Code 

```python

numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)

print(numbers)

```

## Sample Output

```
[10, 20, 30, 40]

```

# Exercise 7 :  Using extend(), combine these lists.

list1 = [1,2,3]
list2 = [4,5,6]


## Sample Code 

```python

list =[]
list1 = [1,2,3]
list2 = [4,5,6]
list = list1 + list2
print(list)

```

## Sample Output

```
[1, 2, 3, 4, 5, 6]

```

# Exercise 8 :  Insert "Python" at index 2.

languages = ["C","C++","Java"]


## Sample Code 

```python

languages = ["C","C++","Java"]
languages.insert(2,"Python")
print(languages)

```

## Sample Output

```
['C', 'C++', 'Python', 'Java']

```

# Exercise 9 :  Remove "Banana" from the list.

fruits = ["Apple","Banana","Orange","Mango"]

## Sample Code 

```python

fruits = ["Apple","Banana","Orange","Mango"]
fruits.remove("Banana")
print(fruits)

```

## Sample Output

```
['Apple', 'Orange', 'Mango']

```

# Exercise 10 :  Remove the last element using pop().

Print:

Removed value
Updated list

## Sample Code 

```python

numbers = [1,2,3,4,5,]
print(numbers.pop())
print(numbers)

```

## Sample Output

```
5
[1, 2, 3, 4]

```

# Exercise 11 :  Predict the output.

```python
numbers = [1,2]

numbers.append([3,4])

print(numbers)

```

## Sample Output

```
[1,2,[3,4]]

```
# Exercise 12 :  Predict the output .

```python

numbers = [1,2]

numbers.extend([3,4])

print(numbers)

```

## Sample Output

```
[1,2,3,4]

```
# Exercise 13 :  Predict the output .

```python

numbers = [10,20,30]

numbers.insert(-1,99)

print(numbers)

```

## Sample Output

```
[10,20,99,30]

```
# Exercise 14 :  Predict the output .


```python

numbers = [10,20,30]

numbers.remove(20)

print(numbers)

```

## Sample Output

```
[10,30]

```
# Exercise 15 :  Predict the output .

```python

numbers = [10,20,30]

x = numbers.pop()

print(x)
print(numbers)

```

## Sample Output

```
30
[10,20]

```
# Exercise 16 :  Create a list of marks.

Calculate:

Total marks
Average

## Sample Code 

```python

marks = [89,90,99,80,97,87]
print("Total marks : ", sum(marks))
avg = round(sum(marks)/len(marks))
print(f"Average :{avg} %")

```

## Sample Output

```
Total marks : 542
Average :90 %

```
# Exercise 17 :  Take five numbers from the user using input().

Store them in a list using append().

Print the final list.

## Sample Code 

```python

list = []

num1 = int(input("Enter 1st  number : "))
list.append(num1)
num2 = int(input("Enter 2nd  number : "))
list.append(num2)
num3 = int(input("Enter 3rd  number : "))
list.append(num3)
num4 = int(input("Enter 4th  number : "))
list.append(num4)
num5 = int(input("Enter 5th  number : "))
list.append(num5)

print("\nYour final list is :",list)


```

## Sample Output

```
Enter 1st  number : 1
Enter 2nd  number : 2
Enter 3rd  number : 3
Enter 4th  number : 4
Enter 5th  number : 5

Your final list is : [1, 2, 3, 4, 5]

```
# Exercise 18 :  Create a list.

Remove the second element using del.

Print the updated list.

## Sample Code 

```python

numbers = [1,2,3,4,5,6]
del numbers[1]
print(numbers)

```

## Sample Output

```
[1, 3, 4, 5, 6]

```
# Exercise 19 :  Create a list.

Clear the list using clear().

Print it.

## Sample Code 

```python

numbers = [1,2,3,4,5,6]
numbers.clear()
print(numbers)

```

## Sample Output

```
[]

```
# Exercise 20 :  Predict the output


```python

numbers = [10,20]

numbers.append(30)
numbers.insert(1,15)
numbers.extend([40,50])
numbers.remove(20)

print(numbers)

```

## Sample Output

```
[10,15,30,40,50]

```

# Exercise 21 : Use len() to print the number of elements in a list.

## Sample Code

```python

fruits = ["Apple","Banana","Orange","Mango"]

print(len(fruits))

```

## Sample Output

```
4

```

# Exercise 22 : Count how many times 5 appears in the list.

## Sample Code

```python

numbers = [5,2,5,8,5,10]

print(numbers.count(5))

```

## Sample Output

```
3

```

# Exercise 23 : Find the index of "Python".

## Sample Code

```python

languages = ["C","C++","Python","Java"]

print(languages.index("Python"))

```

## Sample Output

```
2

```

# Exercise 24 : Sort a list in ascending order.

## Sample Code

```python

numbers = [8,2,6,1,4]

numbers.sort()

print(numbers)

```

## Sample Output

```
[1, 2, 4, 6, 8]

```

# Exercise 25 : Sort a list in descending order.

## Sample Code

```python

numbers = [8,2,6,1,4]

numbers.sort(reverse=True)

print(numbers)

```

## Sample Output

```
[8, 6, 4, 2, 1]

```

# Exercise 26 : Reverse a list.

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

# Exercise 27 : Create a copy of a list and add a new element to the copied list.

## Sample Code

```python

list1 = [10,20,30]

list2 = list1.copy()

list2.append(40)

print("Original List :",list1)
print("Copied List :",list2)

```

## Sample Output

```
Original List : [10, 20, 30]
Copied List : [10, 20, 30, 40]

```

# Exercise 28 : Check whether "Apple" is in the list and "Mango" is not in the list.

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