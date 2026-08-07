# Week 2 – Day 4 Exercises

# Exercise 01 : Student Marks Calculator

Create a function using `*args` that accepts any number of marks.

Print:

* Total Marks
* Average Marks

## Code

```python
def calculate_marks(*marks):

    total = sum(marks)
    average = total / len(marks)

    print("Total Marks : ", total)
    print("Average Marks : ", average)


calculate_marks(85, 90, 78, 88, 95)
```

## Output

```text
Total Marks :  436
Average Marks :  87.2
```

---

# Exercise 02 : Smart User Profile

Create a function using `**kwargs`.

Pass at least six student details and print every key and value using a loop.

## Code

```python
def student(**details):

    for key, value in details.items():
        print(key, ":", value)


student(
    name="Sunaina",
    age=17,
    city="Gilgit",
    country="Pakistan",
    goal="Study AI",
    scholarship="Turkey Burslari"
)
```

## Output

```text
name : Sunaina
age : 17
city : Gilgit
country : Pakistan
goal : Study AI
scholarship : Turkey Burslari
```

---

# Exercise 03 : Welcome Generator

Create a function with a default parameter.

If no name is provided, it should display `Welcome Guest`.

If a name is provided, it should display the person's name.

## Code

```python
def welcome(name="Guest"):

    print("Welcome", name)


welcome()
welcome("Sunaina")
```

## Output

```text
Welcome Guest
Welcome Sunaina
```

---

# Exercise 04 : Global vs Local Variables

Create:

* One global variable named `academy`.
* One local variable named `course`.
* Print both inside the function.
* Print the global variable outside the function.
* Try to access the local variable outside the function.

## Code

```python
academy = "BridgeTalk Academy"


def show():

    course = "Python"

    print("Academy : ", academy)
    print("Course : ", course)


show()

print("Academy outside function : ", academy)

try:

    print(course)

except NameError:

    print("Course cannot be accessed outside the function.")
```

## Output

```text
Academy :  BridgeTalk Academy
Course :  Python
Academy outside function :  BridgeTalk Academy
Course cannot be accessed outside the function.
```

## Explanation

`academy` is a global variable, so it can be accessed throughout the program.

`course` is a local variable, so it can only be accessed inside the `show()` function.

---

# Exercise 05 : AI Translator Function

Create a function:

```python
translate(text, source="English", target="Turkish")
```

Call the function in three different ways:

1. Only text
2. Text with source language
3. Using keyword arguments in a different order

## Code

```python
def translate(text, source="English", target="Turkish"):

    print("Text : ", text)
    print("Source Language : ", source)
    print("Target Language : ", target)
    print()


# 1. Only text
translate("Hello")


# 2. Text + source language
translate("Hello", "Urdu")


# 3. Keyword arguments in different order
translate(
    target="English",
    text="Merhaba",
    source="Turkish"
)
```

## Output

```text
Text :  Hello
Source Language :  English
Target Language :  Turkish

Text :  Hello
Source Language :  Urdu
Target Language :  Turkish

Text :  Merhaba
Source Language :  Turkish
Target Language :  English
```

---

# Concepts Practiced

Through these five exercises, the following Python concepts were practiced:

* Default Parameters
* Positional Arguments
* Keyword Arguments
* `*args`
* `**kwargs`
* Dictionaries
* `.items()`
* Local Variables
* Global Variables
* Function Parameters
* Exception Handling with `try-except`
* AI-related function design
