# What is a Dictionary?

- A dictionary is a mutable data structure that stores data in **key-value pairs**.
- Each key is unique and is used to access its corresponding value.
- Dictionaries are written using curly braces `{}`.

## Syntax

```python
dictionary = {
    "key": value
}
```

## Sample Code

```python
student = {
    "name": "Ali",
    "age": 18,
    "city": "Gilgit"
}

print(student)
```

## Sample Output

```
{'name': 'Ali', 'age': 18, 'city': 'Gilgit'}
```

## Key Points

- Stores data as key-value pairs.
- Uses curly braces `{}`.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.

## AI Connection

AI models, APIs, databases, and JSON data all use dictionaries because they organize information using meaningful keys instead of indexes.

---

# Accessing Values

- Values are accessed using their keys.

## Syntax

```python
dictionary["key"]
```

## Sample Code

```python
student = {
    "name": "Ali",
    "age": 18
}

print(student["name"])
```

## Sample Output

```
Ali
```

## Key Points

- Access values using keys.
- Using a missing key raises a `KeyError`.

## AI Connection

AI applications retrieve information such as model names, prediction results, and settings using dictionary keys.

---

# Adding Items

- A new key-value pair can be added by assigning a value to a new key.

## Syntax

```python
dictionary["new_key"] = value
```

## Sample Code

```python
student = {
    "name": "Ali"
}

student["city"] = "Gilgit"

print(student)
```

## Sample Output

```
{'name': 'Ali', 'city': 'Gilgit'}
```

## Key Points

- A new key creates a new item.
- No special method like `append()` is required.

## AI Connection

AI applications often add new information such as confidence scores, labels, or metadata to dictionaries.

---

# Updating Items

- Assigning a value to an existing key updates that value.

## Syntax

```python
dictionary["key"] = new_value
```

## Sample Code

```python
student = {
    "age": 18
}

student["age"] = 19

print(student)
```

## Sample Output

```
{'age': 19}
```

## Key Points

- Existing keys are updated.
- Duplicate keys are not created.

## AI Connection

AI systems continuously update predictions, statistics, and user information stored in dictionaries.

---

# Removing Items

## pop()

Removes a key and returns its value.

```python
student.pop("city")
```

## del

Deletes a key completely.

```python
del student["city"]
```

## clear()

Removes all items.

```python
student.clear()
```

## Key Points

- `pop()` returns the removed value.
- `del` only removes the key.
- `clear()` empties the dictionary.

## AI Connection

Applications remove outdated information while keeping current records accurate.

---

# keys()

Returns all dictionary keys.

## Syntax

```python
dictionary.keys()
```

## Sample Output

```
dict_keys(['name', 'age'])
```

---

# values()

Returns all dictionary values.

## Syntax

```python
dictionary.values()
```

## Sample Output

```
dict_values(['Ali', 18])
```

---

# items()

Returns key-value pairs.

## Syntax

```python
dictionary.items()
```

## Sample Output

```
dict_items([('name', 'Ali'), ('age', 18)])
```

---

# get()

Safely retrieves a value without raising a `KeyError`.

## Syntax

```python
dictionary.get("key")
```

## Sample Code

```python
student = {
    "name": "Ali"
}

print(student.get("grade"))
```

## Sample Output

```
None
```

## Key Points

- Returns `None` if the key does not exist.
- Prevents program crashes.

## AI Connection

Professional applications use `get()` when optional information may not exist.