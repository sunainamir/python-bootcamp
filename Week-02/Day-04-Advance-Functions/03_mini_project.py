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
print()
add_languages = int(input("How many favorite languages do you want to add? "))
print()

def languages():
    for i in range(add_languages):
        input(f"Enter Language {i+1} : ")
        
languages()

print() 
print("="*40)
print("AI SETTINGS".center(40))
print("="*40)
print()

def welcome():
    print(f"Welcome {name}")
welcome()
print()
print("Application name : BridgeTalk AI")
print()

def settings(**details):
    
    for key , value in details.items():
        print(key ," : ",value)
        
settings(Language = pre_language ,
         Voice = voice ,
         Speed=  speed ,
         Theme = theme ,
         Microphone = mic ,
         Speaker = speaker ,
         Auto_Save = auto_save )

print()
print("="*40)
print("FAVOURITE LANGAUGES".center(40))
print("="*40)
print() 

print(languages)

print()
print("="*40)
print("LOCAL VARIABLE DEMO".center(40))
print("="*40)
print()      
print("Current Mode : Translation")

print()
print("="*40)
print("GLOBAL VARIABLE DEMO".center(40))
print("="*40)
print() 
print("Application Name : BridgeTalk AI")

print()
print("="*40)
print("SETTINGS SAVED SUCCESSFULLY".center(40))
print("="*40)
print() 

print("Thank You For Using BridgeTalk AI Setting Manager !")
print()