print("="*40)
print("        SHOPPING LIST MANAGER ")
print("="*40)
print("\n")

shopping_list = []
item1 = input("Enter Item 1 : ")
shopping_list.append(item1)
item2 = input("Enter Item 2 : ")
shopping_list.append(item2)
item3 = input("Enter Item 3 : ")
shopping_list.append(item3)
item4 = input("Enter Item 4 : ")
shopping_list.append(item4)
item5 = input("Enter Item 5 : ")
shopping_list.append(item5)

print("\n")
print("-"*10 , " SHOPPING LIST " ,"-"*10)
print("\n")

print(shopping_list)

remove_item = input("\nEnter Item to remove : ")
shopping_list.remove(remove_item)


print("\n")
print("-"*10 , " UPDATED LIST " ,"-"*12)
print("\n")
print(shopping_list)
print("\n")
print("Total Items : ", len(shopping_list))

print("\n")
print("="*40)
print("     THANK YOU FOR USING THE PROGRAM ")
print("="*40)
print("\n")