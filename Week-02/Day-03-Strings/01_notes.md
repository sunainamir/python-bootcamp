# Strings (Advanced)

Strings are one of the most important data types in Python. They are used to store and manipulate text. In Artificial Intelligence, Natural Language Processing (NLP), chatbots, and translation systems, almost everything is processed as strings.

---

## len()

- Returns the total number of characters in a string.

### Sample Code

```python
text = "Python"

print(len(text))
```

### Sample Output

```
6
```

---

## upper()

- Converts all characters to uppercase.

### Sample Code

```python
text = "hello"

print(text.upper())
```

### Sample Output

```
HELLO
```

---

## lower()

- Converts all characters to lowercase.

### Sample Code

```python
text = "HELLO"

print(text.lower())
```

### Sample Output

```
hello
```

---

## title()

- Capitalizes the first letter of every word.

### Sample Code

```python
text = "bridge talk ai"

print(text.title())
```

### Sample Output

```
Bridge Talk Ai
```

---

## capitalize()

- Capitalizes only the first letter of the sentence.

### Sample Code

```python
text = "hello world"

print(text.capitalize())
```

### Sample Output

```
Hello world
```

---

## strip()

- Removes extra spaces from the beginning and end of a string.

### Sample Code

```python
text = "   Python   "

print(text.strip())
```

### Sample Output

```
Python
```

---

## replace()

- Replaces one word or character with another.

### Sample Code

```python
text = "I love Python"

print(text.replace("Python","AI"))
```

### Sample Output

```
I love AI
```

---

## find()

- Returns the index of the first occurrence of a substring.
- Returns `-1` if the substring is not found.

### Sample Code

```python
text = "BridgeTalk"

print(text.find("Talk"))
```

### Sample Output

```
6
```

---

## count()

- Counts how many times a substring appears.

### Sample Code

```python
text = "AI AI Python AI"

print(text.count("AI"))
```

### Sample Output

```
3
```

---

## startswith()

- Checks whether a string starts with a given value.
- Returns `True` or `False`.

### Sample Code

```python
text = "BridgeTalk"

print(text.startswith("Bridge"))
```

### Sample Output

```
True
```

---

## endswith()

- Checks whether a string ends with a given value.
- Returns `True` or `False`.

### Sample Code

```python
text = "voice.mp3"

print(text.endswith(".mp3"))
```

### Sample Output

```
True
```

---

## split()

- Splits a string into a list using spaces (default separator).

### Sample Code

```python
text = "Hello how are you"

print(text.split())
```

### Sample Output

```
['Hello', 'how', 'are', 'you']
```

---

## join()

- Joins elements of a list into a single string.

### Sample Code

```python
words = ["Hello","World"]

print(" ".join(words))
```

### Sample Output

```
Hello World
```

---

# AI Connection 🤖

String methods are essential in AI because almost all user communication is text. Before translating or analyzing text, AI systems clean and process it.

Examples:

- `strip()` removes unwanted spaces from user input.
- `capitalize()` improves sentence formatting.
- `replace()` corrects common spelling or speech-recognition mistakes.
- `split()` breaks sentences into individual words for processing.
- `join()` combines processed words back into complete sentences.
- `find()` and `count()` help detect keywords and repeated words.
- `startswith()` and `endswith()` validate filenames, commands, or user input.

These methods form the foundation of chatbots, translators, search engines, voice assistants, and Natural Language Processing (NLP) systems.