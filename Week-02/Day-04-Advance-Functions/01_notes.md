# Advanced Functions

Functions help us write reusable, organized, and maintainable code. Advanced functions make programs more flexible by allowing optional values, variable numbers of arguments, and better control over variables.

---

# Default Parameters

* Default parameters provide a value automatically if the user does not pass one.
* They make functions easier to use.
* Default parameters must always come after required parameters.

### Sample Code

```python
def greet(name="Guest"):
    print("Welcome", name)

greet()
greet("Sunaina")
```

### Sample Output

```
Welcome Guest
Welcome Sunaina
```

---

# Positional Arguments

* Values are assigned according to their position.
* The order of arguments is important.

### Sample Code

```python
def student(name, age):
    print(name)
    print(age)

student("Ali", 18)
```

### Sample Output

```
Ali
18
```

---

# Keyword Arguments

* Arguments are passed using parameter names.
* The order of arguments does not matter.
* Improves code readability and maintainability.

### Sample Code

```python
def student(name, age, city):
    print(name)
    print(age)
    print(city)

student(city="Gilgit", age=18, name="Ali")
```

### Sample Output

```
Ali
18
Gilgit
```

---

# *args (Variable-Length Positional Arguments)

* `*args` allows a function to accept any number of positional arguments.
* Python automatically stores them in a tuple.
* Useful when the number of inputs is unknown.

### Sample Code

```python
def add(*numbers):

    total = 0

    for number in numbers:
        total += number

    print(total)

add(10, 20, 30, 40)
```

### Sample Output

```
100
```

---

# **kwargs (Variable-Length Keyword Arguments)

* `**kwargs` allows a function to accept any number of keyword arguments.
* Python automatically stores them in a dictionary.
* Makes functions flexible and highly readable.

### Sample Code

```python
def profile(**student):

    for key, value in student.items():
        print(key, ":", value)

profile(
    name="Sunaina",
    age=17,
    city="Gilgit"
)
```

### Sample Output

```
name : Sunaina
age : 17
city : Gilgit
```

---

# Local Variables

* Local variables are created inside a function.
* They can only be accessed within that function.
* They are destroyed after the function finishes execution.

### Sample Code

```python
def show():

    message = "Hello"

    print(message)

show()
```

### Sample Output

```
Hello
```

---

# Global Variables

* Global variables are created outside a function.
* They can be accessed throughout the program.
* They remain available until the program ends.

### Sample Code

```python
language = "Turkish"

def show():

    print(language)

show()
```

### Sample Output

```
Turkish
```

---

# Using the `global` Keyword

* The `global` keyword allows a function to modify a global variable.
* Without `global`, Python creates a new local variable with the same name.

### Sample Code

```python
marks = 90

def update():

    global marks

    marks = 100

update()

print(marks)
```

### Sample Output

```
100
```

---

# AI Connection 🤖

Advanced functions are used extensively in Artificial Intelligence, machine learning, APIs, and software development.

Examples:

* Default parameters provide optional settings such as default language or voice.
* Keyword arguments make AI functions easier to read and configure.
* `*args` allows AI systems to process inputs of different lengths, such as sentences with varying numbers of words.
* `**kwargs` is commonly used for configurable options like language, speed, theme, voice, and translation settings.
* Local variables temporarily store information during processing and are removed after execution.
* Global variables store application-wide settings, although professional developers often prefer passing values as parameters to make programs easier to maintain and test.

These concepts will be essential while developing **BridgeTalk AI**, where functions will manage translation, speech synthesis, user preferences, and application settings efficiently.
