  # For Loop 

- Python uses a `for` loop when the number of iterations is known.

## Syntax

```python
for variable in sequence:
    # code
```

## Sample Code 

```python

for i in range (5):
        print (i)
  
```

## Sample Output

```
0
1
2
3
4

```

## Key Points

- Executes a block of code repeatedly.
- Commonly used with `range()`.
- Best when the number of iterations is known.

## AI Connection

Loops are used in AI to process datasets, train models over multiple epochs, and automate repetitive tasks.

# While Loop

-  A ' while ' loop  repeats until its condition becomes 'False'  .

## Syntax

```python
while condition:
    # code
```

## Sample Code

```python
number=1
while number <= 5:
      print(number)
      number=number+1
  
```
## Sample Output

```
1
2
3
4
5

```

## Key Points

- Used when the number of iterations is not known in advance.
- The condition is checked before each iteration.
- Be careful to avoid infinite loops.

## AI Connection

While loops can be used when a process should continue until a stopping condition is met, 
such as repeating training until a target accuracy is reached.

# Range 

- `range()` is used to generate a sequence of numbers. . 
-  used with ' for ' loop 

## Syntax

```python

for variable in range(start , stop , step ):
                  #code
  
```
## Sample Code 

```python

for i in range ( 0 , 10 , 2 ) :
          print(i)

```

## Sample Output

```
0
2
4
6
8

```

## Key Points 

  - used with ' for ' loop .
  - control the sequence of iterations .
  - range() has three paremeters , range ( start , stop , step ) .
  - `start` → Starting value
  - `stop` → Ending value (not included)
  - `step` → Increment or decrement
    
## AI Connection

- `range()` is used to iterate through large datasets and process data 
   one item at a time during AI training and prediction.

# Break Statement

- 'break' is used to immediately stop the loop

## Syntax

```python
for variable in sequence :
      #code
      break
      #code

```
## Sample Code

```python
for number in range (1,10):
      if number == 5:
            break
      print(number)
      
```
## Sample Output

```
1
2
3
4

```
## Key Points

- When python reaches the condition it stops the whole loop .
- Python checks :
    iteration = 5
    number = 5
    condition = True   (loop stops)

## AI Connecion

- Used in searching an image from a huge database

### Example

```python
for image in dataset:
    if image == target_image:
        break
```

- It will stop when image is found .


# Continue

- continue skips only the current iteration and continues the loop .

## Syntax 

```python
for variable in sequence :
      #code
      continue
      #code

```

## Sample Code 

```python
for i in range(1,6):
    if i == 3:
        continue
    print(i)
  
```
## Sample Output

```
1
2
4
5

```
## Key Points

- Skips one iteration and continues the loop .
- Python checks :
    iteration = 3
    number = 3
    condition = True   (iteration skips , loop continues)

## AI Connection

- used when we have to skip unnessesery data from  large data set .
###Example :

    ```python

            data = [10, 20, -5, 30, 40]
            for value in data:
                 if value < 0:
                     continue
                 print(value)
```
      output :

```
              10
              20
              30
              40
```

# Number Processing Logic 

- Number processing is the technique to analyze and manipulate data by using loops and conditions .

## Common Operations 

- Counting numbers
- Finding even and odd numbers
- Finding the largest or smallest number
- Calculating squares or cubes
- Reversing numbers
- Checking prime numbers

## Sample Code 

```python 

for number in range ( 1 , 11 ) :
    if number % 2 == 0 :
          print(number)

```

## Sample Output 

```
2
4
6
8
10

```

## Key Points

- Uses loops to process numbers one by one.
- Often combined with if statements.
- Forms the basis of many programming problems.

## AI Connection

- Number processing is used to analyze numerical datasets, perform calculations,
  and prepare data before training AI models.



# Data Summation Logic

- Data summation is the process of calculating the total of multiple values using a loop.

## Sample Code 

```python
  
  total = 0

  for number in range(1, 6):
    total += number

  print(total)

```

## Sample Output

```
15

```

## Key Points

- Initialize a variable (usually total) with 0.
- Add each value to the total inside the loop.
- Display the final total after the loop ends.
  
## AI Connection

 - Summation is used in AI to calculate totals, averages, losses, 
   probabilities, and many mathematical operations during model training.


# Pattern Printing 
   - Pattern printing is the process of displaying shapes or designs using
     loops and characters such as `*`, numbers, or letters.

## Sample Code 

```python
  
 for i in range(1, 6):
    print("*" * i)
   
```

## Sample Output

```
*
**
***
****
*****

```

## Key Points

 - Uses nested or single loops.
 - Helps improve logical thinking.
 - Strengthens understanding of loop execution.
  
## AI Connection

  - Although pattern printing is not directly used in AI, it develops logical thinking
    and problem-solving skills that are essential for programming and algorithm design.



























