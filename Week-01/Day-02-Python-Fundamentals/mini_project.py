### PROJECT

## about:
- it is a mini program that takes student data and returns result report.
- it uses if-statement , int() , print() , input() , mathematical operations.

##statement 
Student Marks Calculator

Ask the user for:

Name
Physics Marks
Mathematics Marks
Computer Science Marks

print data , total and averge marks . also print excellent if the average is 80 or above .


##code :

```python

name = input("enter your name : ")
maths=int(input("enter your maths marks :"))
phy=int(input("enter your physics marks :"))
cs=int(input("enter your computer science marks :"))
total= maths+phy+cs 
avg= (maths+phy+cs)/3

print("="*5 , "student report" , "="*5)
print(f"name :{name}")
print(f"maths :{maths}")
print(f"physics :{phy}")
print(f"computer science :{cs}")
print(f"total marks :{total}")
print(f"average marks :{avg}")

if avg >= 80:
    print("Excellent ! you did well")

```
#input :

```
enter your name : naina
enter your maths marks :99
enter your physics marks :90
enter your computer science marks :98

```

##output:

```
===== student report =====
name :naina
maths :99
physics :90
computer science :98
total marks :287
average marks :95.67
Excellent ! you did well

```









