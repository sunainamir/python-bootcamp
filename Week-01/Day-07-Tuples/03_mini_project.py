print("="*40)
print("       STUDENT INFORMATION VIEWER")
print("="*40)

name = input("Enter Student Name : ")
age = int(input("Enter Age : "))
city = input("Enter City : ")
grade = input("Enter Grade : ")

print("\n")

print("-"*10," STUDENT RECORD ","-"*10)
print("\n")

student_tuple = (name,age,city,grade)
print("Student Tuple :")
print(student_tuple)

print("\nUsing Indexing :")

print("\n")
print("Name : ",student_tuple[0])
print("Age : ",student_tuple[1])
print("City : ",student_tuple[2])
print("Grade : ",student_tuple[3])
print("\n")

print("Using Tuple Unpacking :")
print("\n")

name,age,city,grade = student_tuple
print("Name : ",name)
print("Age : ",age)
print("City : ",city)
print("Grade : ",grade)
print("\n")

print("="*40)
print("      THANK FOR USING THE PROGRAM")
print("="*40)