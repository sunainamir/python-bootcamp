"""
==========================================
Mini Project: Number Analyzer

Description:
This project demonstrates the use of Python loops,
conditions, number processing, data summation,
and pattern printing.

Concepts Used:
- for loop
- range()
- if statements
- arithmetic operators
- data summation
- pattern printing
==========================================
"""

## Code 

print("="*30)
print("      ", "NUMBER ANALYZER")
print("="*30)

number = int(input("\nEnter a positive number : "))

if number < 0:
    print("you entered negative number")
    print("Please enter positive number . THANKYOU! ")
    exit()
    
print("\nWelcome to Number Analyzer!")

print("\n")
print("="*10," Menu ","="*10)

print("1. Counting Numbers ")
print("2. Even Numbers")
print("3. Odd Numbers")
print("4. Sum of Numbers")
print("5. Star Pattern")
print("6. Reverse Counting")
print("7. Multiplication Table")
print("8. Square Pattern")
print("9. Exit")

choice = int(input("\nEnter your choice :"))

if choice == 1 :
    print("\nCounting Numbers are : ")
    for i in range(1,number+1):
        print(i)
       
elif choice <1 or choice > 9:
    print("Invalid choice !")   
    print("Please select a number between 1 and 9.")
    exit()
    
elif choice == 2 :
    print("\nEven Numbers are : ")
    for i in range(2,number+1,2):
        print(i)
        
elif choice == 3 :
    print("\nOdd Numbers are :")
    for i in range(1,number+1,2):
            print(i)

elif choice == 4 :
    total = 0
    for i in range(1,number+1) :
        total = total + i
        
    print("\nSum of Numbers are :", total)
    
            
elif choice == 5 :
    print("\nStar Pattern is :")
    for i in range(1,number+1):
            print("*"*i)
            
elif choice == 6 :
    print("\nReverse Counting :")
    for i in range(number,0,-1):
            print(i)
            
elif choice == 7 :
    print(f"\nMultiplication Table of {number} :")
    for n in range(1,11):
        print(number , "x" , n , "=" ,number*n)
        
elif choice == 8 :
    print("\nSquare Pattrern :")
    for i in range(number):
            print("*"*number)
            
elif choice == 9 :
    print("\n")
    print("="*42)
    print("  ", "Thankyou for using Number Analyzer !")
    print("="*42)
    exit()


