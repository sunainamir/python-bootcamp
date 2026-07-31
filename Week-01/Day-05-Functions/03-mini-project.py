print("\n")
print("="*40)
print("      Student Report Card Generator")   
print("="*40)

name = input("Enter Student Name : ") 

phy = int(input("Enter Physics Marks : "))
if phy < 0 or phy > 100:
    print("Invalid Physics Marks")
    exit()
    
chem = int(input("Enter Chemistry Marks : "))
if chem < 0 or chem > 100:
    print("Invalid Chemistry Marks")
    exit()
    
comp = int(input("Enter Computer Marks : "))
if comp < 0 or comp > 100:
    print("Invalid Computer Marks")
    exit()
    
print("\n")
print("-"*10 ," RESULT " , "-"*10)
print("\n")

print(f"Student name : {name}")
print(f"Physics  : {phy}")
print(f"Chemistry  : {chem}")
print(f"Computer  : {comp}")

def total(phy,chem,comp):
    return phy + chem + comp
total_marks = total(phy,chem,comp)
print(f"Total Marks : {total_marks} / 300")

def avg(phy,chem,comp):
    return (phy+chem+comp)/3
student_average = round(avg(phy,chem,comp))
print(f"Average     : {student_average} %")

def grade(student_average):
    if student_average >=90:
        return  "A++"
    elif student_average >=80:
        return "A"
    elif student_average >=70:
        return "B"
    elif student_average >=60:
        return "C"
    elif student_average >=50:
        return "D"
    elif student_average >=40 :
        return "E"
    else:
        return "F"

student_grade = grade(student_average)
print(f"Grade       : {student_grade}")

def result(student_average):
    if student_average >= 50:
        return "Pass"
    else :
        return "Fail"
student_result = result(student_average)
print(f"Result      : {student_result}")


print("\nThank you!\n")


print("=" * 40)
print("     Report Generated Successfully!")
print("=" * 40)