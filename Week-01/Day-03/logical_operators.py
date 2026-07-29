# Logical_operators :

- python uses logical operators to check more conditions at the same time .

## and operator (and) :

- and operator simply checks whether both conditions are true or not .
- both condition should meet for further execution .

### sample code 

``` python
  
age = 20
citizen = True

if age >= 18 and citizen:
    print("You can vote.")
  
```
       
## processing 

- Python asks:

Is age >= 18? ✅ Yes
Is citizen True? ✅ Yes

Both are True.

### sample ouput 

```
       You can vote .

```

## or operator (or) :
       
- at least one condition should True for further execution .

### sample code 

``` python
       
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
       
```
## processing 

Is it Saturday?

✅ Yes

### sample ouput 

```
      Weekend

```

## not operator (not) :
       
- not operator simply reverses the condition .

### sample code 

``` python
       
logged_in = False

if not logged_in:
    print("Please log in.")
       
```
## processing 

not False

↓

True

### sample ouput 

```
     Please log in. 

```


       
