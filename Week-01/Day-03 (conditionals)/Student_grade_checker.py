# Student_grade_checker 

##Features 
- predicts the grade of student and gives remarks
- easy to use and trustworthy .
- gives valid results .

###code

```python 

name = input("enter your name : ")
marks = int(input("enter your marks :"))

print("="*5, "student report", "="*5)
print(f"name: {name}")
print(f"marks :{marks}")

if marks < 0 or marks > 100 :
    print("invalid marks ")
    print("please enter marks between 0-100")
    
elif marks >=90:
    print("grade : A+")
    print("remarks:excellent work ")
elif marks >=80:
    print("grade : A")
    print("remarks: very good ")
elif marks >=70:
    print("grade : B")
    print("remarks :good job ")
elif marks >=60:
    print("grade : C")
    print("remarks: keep improving")
elif marks >=50:
    print("grade : D")
    print("remarks: work hard")
elif marks < 50:
    print("grade : fail")
    print("remarks: better luck next time .")  

print("="*26)

```
###sample input 1

```
enter your name : sunaina
enter your marks :-77

```

###sample output 1 

```
===== student report =====
name: sunaina
marks :-77
invalid marks
please enter marks between 1-100 
==========================

###sample input 2

```
enter your name : sunaina
enter your marks :150

```

###sample output 2

```
===== student report =====
name: sunaina
marks :150
invalid marks
please enter marks between 1-100 
==========================


###sample input 3

```
enter your name : sunaina
enter your marks :99

```

###sample output 3

```
===== student report =====
name: sunaina
marks :99
grade : A+
remarks : excellent work 
==========================

```

###sample input 4

```
enter your name : sunaina
enter your marks :85

```

###sample output 4

```
===== student report =====
name: sunaina
marks :85
grade : A
remarks : very good
==========================

```

###sample input 5

```
enter your name : sunaina
enter your marks :77

```

###sample output 5

```
===== student report =====
name: sunaina
marks :77
grade : B
remarks : good job 
==========================

```

###sample input 6

```
enter your name : sunaina
enter your marks :63

```

###sample output 6

```
===== student report =====
name: sunaina
marks :63
grade : C
remarks : keep improving 
==========================

```

###sample input 7

```
enter your name : sunaina
enter your marks :56

```

###sample output 7

```
===== student report =====
name: sunaina
marks :56
grade : D
remarks :  work hard
==========================

```
###sample input 8

```
enter your name : sunaina
enter your marks :45

```

###sample output 8

```
===== student report =====
name: sunaina
marks :45
grade : Fail
remarks : better luck next time
==========================

```


