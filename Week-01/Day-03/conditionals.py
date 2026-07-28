# conditional_statements 

- python uses these statement if any condition is to be executed .

## IF_STATEMENT  
  
  - used when there is only one condition to be executed .

###sample code 1

```python 

number = 10
if number == 10:
    print("Correct")

```

###sample output 1

```
  correct

```
###sample code 2

```python 

number = 8
if number != 10:
    print("different")

```

###sample output 2

```
  different

```

## IF_ELSE STATEMENT  
  
  - used when there is two conditions is to be executed .
  - if first condition evaluates to False then python automatically executes the second one.

###sample code 1

```python 

number = 10
if number == 10:
    print("Correct")
else:
  print("different")

```

###sample output 1

```
  correct

```
###sample code 2

```python 

number = 8
if number == 10:
    print("correct")
else:
    print("different")

```

###sample output 2

```
  different

```

## IF_ELIF STATEMENT  
  
  - used when there more than two conditions are to be executed.
  - if one condition evaluates to False then it goes on next one and similarly checks all condition .

###sample code 

```python 

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

```
###sample input 1
```
  Enter your marks : 90

```
###sample output 1

```
  Excellent

```

###sample input 2
```
  Enter your marks : 77

```
###sample output 2

```
  Good

```

###sample input 3
```
  Enter your marks : 45

```
###sample output 3

```
  Pass

```
###sample input 4
```
  Enter your marks : 35

```
###sample output 4

```
  Fail

```
