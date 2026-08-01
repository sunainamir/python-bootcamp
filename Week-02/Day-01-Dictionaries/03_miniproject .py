print("="*40)
print("        STUDENT RECORD MANAGER")
print("="*40,"\n")

name = input("Enter Student Name : ")
age = int(input("Enter Age : "))
roll_number = int(input("Enter Roll Number : "))
grade = input("Enter Grade : ")
city = input("Enter City : ")

student = {
    "name" : name ,
    "age" : age ,
    "roll_number" : roll_number ,
    "grade" : grade ,
    "city" : city
}
print("\nStudent Dictionary:")
print("\n")
print(student)
print("\n")
print("-"*9," STUDENT RECORD ","-"*9,"\n")

print("Name : ",student["name"])
print("Age : ",student["age"])
print("Roll_Number : ",student["roll_number"])
print("Grade : ",student["grade"])
print("City : ",student["city"],"\n")

key_update = input("Enter Key to Update : ")

value_update = input("Enter New Value :")
print("\n")
if key_update in student :
    student[key_update] = value_update
    print(f"{key_update} updated successfully!\n")
    print("Updated Record :")
    print("\n",student,"\n")
else:
    print("Key Not Found \n")
    
item_remove = input("Enter Key to Remove : ")
if item_remove in student :
    remove_key = student.pop(item_remove)
    print(f"\nRemoved {item_remove} : " ,remove_key,"\n")
    print("Final Student Record : " ,"\n\n" ,student,"\n")
else:
    print("\nKey Not Found")

print("\nDictionary Keys : ", "\n")
print(student.keys())

print("\nDictionary Values : ", "\n")
print(student.values())

print("\nDictionary Items : ", "\n")
print(student.items(),"\n")

search_key = input("Enter Key to Search Record : ")
search = student.get(search_key)
if search is None:
    print("Key Not Found\n")
else:
    print("\nSearched Record : ","\n")
    print(search_key," : ",search,"\n")

print("="*50)
print("         THANK YOU FOR USING THE PROGRAM")
print("="*50,"\n")