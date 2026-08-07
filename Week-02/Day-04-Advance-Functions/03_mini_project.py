print("="*40)
print("BRIDGETALK AI SETTING".center(40))
print("="*40)
print()

name = input("Enter your Name : ")
pre_language = input("Enter Preferred Language : ")
voice = input("Enable Voice (True/False) :")                 
speed = input("Enter Voice Speed : ")
theme = input("Enter Theme : ")
mic = input("Enable Microphone (True/False) : ")
speaker = input("Enable Speaker (True/False) : ")
auto_save = input("Enable Auto Save (True/False) : ")   
add_languages = int(input("How many favorite languages do you want to add? "))

def get_languages():
    for i in range(add_languages):
        input(f"Enter language {i} : " )
        return get_languages
    
get_languages()