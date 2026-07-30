# =====================
# Day 04 - Python Loops
# File: 02_exercises.py
# =====================

# Exercise 1: Print numbers from 1 to 5

## Code

```python
  for i in range (1,6):
    print(i)
```

## Output

```
1
2
3
4
5

```

# Exercise 2: Print even numbers from 2 to 10

## Code

```python
  for i in range (2 ,11, 2):
    print(i)
    
```

## Output

```
2
4
6
8
10

```

# Exercise 3: Print odd numbers from 1 to 9

## Code

```python
  for i in range (1 ,10, 2):
    print(i)
    
```

## Output

```
1
3
5
7
9

```

# Exercise 4: Print numbers from 10 to 1

## Code

```python
  for i in range (10 ,0, -1):
       print(i)
    
```

## Output

```
10
9
8
7
6
5
4
3
2
1

```

# Exercise 5: Print numbers except 4 using continue

## Code

```python
  for number in range (1,6):
     if number == 4 :
           continue
     print(number)
    
```

## Output

```
1
2
3
5

```

# Exercise 6: Stop the loop when number becomes 5

## Code

```python
  for number in range (1,10):
     if number == 5 :
            break
     print(number)
    
```

## Output

```
1
2
3
4

```

# Exercise 7: Calculate the sum of numbers from 1 to 10

## Code

```python
totle = 0
for number in range (1,11):
    totle = totle + number
    
print("sum = ",sum)

```

## Output

```
sum = 55

```

# Exercise 8: Print a right triangle pattern

## Code

```python

for i in range (1,6):
    print("*"*i)

```

## Output

```
*
**
***
****
*****

```

# Exercise 9: Print an inverted triangle pattern
  
## Code

```python

for i in range (5,0,-1):
    print("*"*i)

```

## Output

```
*****
****
***
**
*
  
```

# Exercise 10: Print a square pattern
  
## Code

```python

for i in range (5):
    print("*"*5)

```

## Output

```
*****
*****
*****
*****
*****
  
```
