# Functions

- A function is a reusable block of code that performs a specific task .

## Syntax

```python

def function_name():
    #code

```

## Sample Code

```python

def greet():
   print("Hello, Future AI Engineer!")

greet()

```

## Sample Output

```
Hello, Future AI Engineer!

```

## Key Points

- Functions make code reusable.
- A function performs a specific task.
- Functions reduce code repetition.
- Functions make programs easier to read and maintain.

## AI Connection

- AI uses functions to train models , evaluate models , data loading and make predictions .

# Calling Functions

- Calling Function is used to call function when we need it .

## Syntax

```python

def function_name():
    #code

function_name()

```
## Sample Code

```python

def greet():
    print("Welcome!")

greet()
greet()
greet()

```
## Sample Output

```
Welcome!
Welcome!
Welcome!

```

## Key Points

- A function runs only when it is called.
- A function can be called multiple times.
- Calling functions makes code reusable.
- It improves program organization.

## AI Connection

Functions are called in AI programs to perform specific tasks such as loading data,
preprocessing information, training models, and making predictions.

# Parameters

- A parameter is a variable inside the function that recieves a value when the function is called .

## Syntax

```python

def function_name(parameter):
    #code

function_name(value)

```
## Sample Code

```python

def greet(name):
    print("Hello",name)

greet("Ali")
greet("sara")
greet("Ahmad")

```
## Sample Output

```
Hello Ali
Hello Sara
Hello Ahmad

```

## Key Points

- Parameters are variables defined inside a function.
- They allow a function to receive input values.
- Parameters make functions reusable.
- A function can have one or more parameters.

## AI Connection

Functions in AI use parameters to receive inputs such as datasets, images, text, or model settings before performing a task.

# Arguments

- Arguments are the actual value passed to the function .

## Syntax

```python

def function_name(parameter):
    #code

function_name(argument/ value)

```
## Sample Code

```python

def square(number):
    print(number * number)

square(5)

```
## Sample Output

```
25

```
## Key Points

- Arguments are the actual values passed to a function.
- They are assigned to the function's parameters.
- The number of arguments should match the required parameters.
- Arguments can be numbers, strings, or variables.

## AI Connection

AI programs pass arguments to functions, such as an image for classification or a sentence for language translation.

# Multiple Parameters

- Multiple parameters allow a function to receive more than one value.

## Syntax

```python

def function_name(parameter , parameter):
    #code

function_name( value,value)

```
## Sample Code
```python

def add(a, b):
    print(a + b)

add(10, 20)
add(5, 8)

```
## Sample Output

```
30
13

```
## Key Points

- A function can accept multiple parameters.
- Parameters are separated by commas.
- Multiple parameters allow a function to work with several values at once.
- They improve flexibility and code reuse.

## AI Connection

AI functions often use multiple parameters, such as training data, learning rate, and number of epochs.

# Return Statement

- return sends the value back to the caller so it can be stored, reused, or passed to other functions .

## Syntax
```python

def function_name(parameter):
    # code
    return value

function_name()

```
## Sample Code

```python

def add(a, b):
    return a + b

result = add(10, 20)

print(result * 2)

```

## Sample Output

```
60

```

## Key Points

- return sends a value back to the caller.
- It ends the function immediately.
- Returned values can be stored in variables.
- A function can return different types of data.

## AI Connection

AI functions return prediction results, calculated values, probabilities, or trained models for further processing.

# print() vs return

-  print() and return both are different values . 

## Comparison

- print() displays the result on the screen.
- return sends the result back to the caller.
- A returned value can be stored and reused.
- print() and return have different purposes.

## Sample Code

### By Using print()

```python

def add(a, b):
    print(a + b)

add(10, 20)

```
### By using retrun 

```python

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

```

## Sample Output

### By Using print()

```
30

```
### By using retrun 

```
30

```
## Key Points

- print() displays output on the screen.
- return sends a value back to the caller.
- Returned values can be reused later in the program.
- return is preferred when the result will be used in further calculations.

## AI Connection

AI programs use return to pass prediction results between functions instead of only displaying them on the screen.

# Local Variables

- Local Variables are the variables created inside the functon and can be used only inside the function.

## Syntax

```python

def function_name(parameter ):
    Local_Variables
    #code

function_name( value )

```
## Sample Code

```python

def student():
    name = "Sunaina"
    print(name)

student()

```

## Sample Output

```
Sunaina

```

## Key Points

- Local variables are created inside a function.
- They can only be used within that function.
- They are destroyed when the function finishes.
- Different functions can have local variables with the same name.

## AI Connection

AI functions use local variables to temporarily store intermediate calculations without affecting other parts of the program.

# Global Variables

- Global variables are created outside a function and can be accessed throughout the program.

## Syntax

```python

Global_Variable
def function_name(parameter ):
    
    #code

function_name( value )

```
## Sample Code

```python

name = "Sunaina"

def student():
    print(name)

student()
print(name)

```

## Sample Output

```
Sunaina
Sunaina

```

## Key Points

- Global variables are created outside all functions.
- They can be accessed by multiple functions.
- They remain available throughout the program.
- Excessive use of global variables can make programs harder to maintain.

## AI Connection

AI applications may use global variables to store settings such as model names, configuration values, or dataset paths that are shared across functions.

# Default Parameters

- Default Parameters are predefined values used when no arguments are given .

## Syntax

``` python 

def function_name(default_Parameters):
        #code

function_name()

```

## Sample Code

```python

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sunaina")

```
## Sample Output

```
Hello Guest
Hello Sunaina

```

## Key Points

- Default parameters have predefined values.
- They are used when no argument is provided.
- They make functions more flexible.
- Default values can be changed by passing a different argument.

## AI Connection

AI functions often use default parameters for settings such as learning rate,
batch size, or the number of training epochs.