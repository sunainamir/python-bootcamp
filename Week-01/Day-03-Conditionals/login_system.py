# login_system

##features
- secure because username and password both are required 
- better visual 
- uses logical operators 

### code 

```python
name =  input("Enter username :")
password = input("Enter password :")

if name == "sunaina" and password =='python123' :
    print("="*25)
    print("    AI system login")
    print("="*25)
    print("\nlogin successful ! ")
    print("\nWelcome sunaina ")
    print("\nHave a great day ")
    print("="*25)
    
elif name == "sunaina" and password !='python123' :
    print("Access denied ! ")
    print("wrong password. try again! ")
    
elif name != "sunaina" and password =='python123' :
    print("access denied ! ")
    print("wrong username . try again! ")
    
elif name != "sunaina" and password !='python123' :
    print("invalid username and password  ! ")
    print("please try again !")


```

### sample input 1

```
Enter username :sunaina
Enter password :python123

```

### sample output 1

```
=========================
    AI system login
=========================

login successful ! 

Welcome sunaina 

Have a great day 
=========================
  
```

### sample input 2

```
Enter username :sunaina
Enter password :abc123

```

### sample output 2 

```
Access denied ! 
wrong password. try again! 

```

### sample input 3

```
Enter username :maisam
Enter password :python123

```

### sample output 3

```
Access denied ! 
wrong username . try again! 

```

### sample input 4

```
Enter username :maisam
Enter password :abc123

```

### sample output 4

```

invalid username and password  ! 
please try again !

```

