# Exercise 01 :  Predict the output :

```python

student = {
    "name": "Ali",
    "age": 18
}

student["city"] = "Gilgit"
student["age"] = 19

print(student)

```

## Output 

```
{'name': 'Ali', 'age': 19, 'city': 'Gilgit'}

```
# Exercise 02 :  Predict the output :

```python

student = {
    "name": "Ali",
    "age": 18
}

student["name"] = "Ahmed"

print(student)

```

## Output 

```
{'name': 'Ahmed', 'age': 18}

```

# Exercise 03 :  Predict the output :

```python

student = {
    "name": "Ali",
    "age": 18
}

print(student.get("grade"))
print(student["grade"])

```

## Output 

```
None
KeyError: 'grade'

```
## Explaination 

student.get("grade") does not raise a KeyError. Instead, it safely returns None if the key does not exist. However, student["grade"] raises a KeyError because "grade" is not present in the dictionary.

# Exercise 04 :  Predict the output :

```python

book = {
    "title": "Python",
    "pages": 500
}

x = book.pop("pages")

print(x)
print(book)

```

## Output 

```
500
{'title': 'Python'}

```
# Exercise 05 : Can two keys have the same name?  Why?

## Explaination 

No. Dictionary keys must be unique. If the same key is written again, Python replaces the previous value with the new one.

# Exercise 06 :  Predict the output :

```python

student = {
    "name": "Ali",
    "city": "Gilgit",
    "birth_city": "Gilgit"
}

print(student)

```

## Output 

```
{'name': 'Ali', 'city': 'Gilgit', 'birth_city': 'Gilgit'}

```
## Explanation

it is valid because here key is not repeated , value is repeated . what matters is key .. values can be repeat .

# Exercise 07 :  Predict the output :

```python

student = {
    "name": "Ali",
    "age": 18,
    "city": "Gilgit"
}

del student["age"]

print(student.keys())
print(student.values())

```

## Output 

```
dict_keys(['name', 'city'])
dict_values(['Ali', 'Gilgit'])

```
# Exercise 08 :  Predict the output :

```python

student = {
    "name": "Ali"
}

student.clear()

print(student)

```

## Output 

```
{}

```

# Exercise 09 : Design a dictionary for your dream AI university profile.It should contain at least 8 meaningful keys (for example: name, country, university, program, scholarship, GPA target, language, etc.).

## Code 

```python

university = {
    "Name" : "Sunaina Mir" ,
    "Country" : "Turkey" ,
    "University" : "Istanbol University" ,
    "Program" : "BS AI" ,
    "Scholarship" : "Türkiye Scholarships (Türkiye Bursları)" ,
    "GPA target" : 4 ,
    "language" : "English"
}
print("=" * 40)
print("      DREAM AI UNIVERSITY PROFILE")
print("=" * 40)
print(university)

```

## Output 

```
========================================
      DREAM AI UNIVERSITY PROFILE
========================================
{'Name': 'Sunaina Mir', 'Country': 'Turkey', 'University': 'Istanbol University', 'Program': 'BS AI', 'Scholarship': 'Türkiye Scholarships (Türkiye Bursları)', 'GPA target': 4, 'language': 'English'}

```
