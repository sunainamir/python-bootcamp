# Exercise 01 : Clean User Input

A user enters a sentence with extra spaces.

Perform the following operations:

Remove extra spaces.
Capitalize the sentence.
Print the cleaned sentence.


## Code

```python

name = input("Enter your name  in full sentence , keep spaces and and keep letters small  : ").strip().capitalize()
text = " ".join(name.split())

print ("new version of sentence : ",text )

```

## Input

```
Enter your name your name in full sentence  :   hello  my name is    Sunaina      Mir .

```

## Output

```
new version of sentence :  Hello my name is Sunaina Mir 

```

# Exercie 02 : Word Analyzer

Given the string:

text = "Python AI Python Machine Learning Python"

Print:

Total number of characters.
Number of times "Python" appears.
Position of "Machine".
Convert the whole sentence to uppercase.

## Code 

```python 

text = "Python AI Python Machine Learning Python"
print(text)

print("Total number of character : ",len(text))
print("Number of word Python appears : ",text.count("Python"))
print("Position of word Machine : ",text.find("Machine"))
print("Upper case version : ",text.upper())

```

## Output

```
Python AI Python Machine Learning Python
Total number of character :  40
Number of word Python appears :  3
Position of word Machine :  17
Upper case version :  PYTHON AI PYTHON MACHINE LEARNING PYTHON

```

# Exercise 03 : File Validator

Given:

filename = input("Enter File Name : ")

Check whether the file is:

.pdf
.docx
.txt

If none of them, print:

Unsupported File

## Code 

```python 
filename = input("Enter File Name : ")
if filename.endswith(".pdf"):
    print("file supported !")
elif filename.endswith(".dox"):
    print("file supported !")
elif filename.endswith(".txt"):
    print("file supported !")
else:
    print("unspported file !")

```

## Input 

```
Enter File Name : abc.txt

```
## Output

```
file supported !

```

# Exercise 04 : AI Text Formatter

Given:

text = input("Enter Sentence : ")

Perform these tasks:

Remove extra spaces.
Replace "AI" with "Artificial Intelligence".
Capitalize the sentence.
Print the final sentence.

## Code

```python

text = input("Enter Sentence : ")
text = " ".join(text.split())
text = text.replace("AI","Artificial Intelligence")
text = text.capitalize()
print("final sentence : ",text)

```

## Input 

```
Enter Sentence :  i  love  ai

```

## Output

```
final sentence :  I Love artificial intelligence

```

# Exercise 05 : BridgeTalk AI Keyword Detector

Given:

sentence = input("Enter Sentence : ")

Check whether the sentence contains the word:

Turkey

If found:

Keyword Found

Otherwise:

Keyword Not Found

## Code

```python

text = input("Enter Sentence : ")
if "Turkey" in text:
    print("Keyword found ")
else :
    print("keyword not found ")

```

## Input

```
Enter Sentence : my dream is to study in Turkey

```

## Output

```
Keyword found 

```