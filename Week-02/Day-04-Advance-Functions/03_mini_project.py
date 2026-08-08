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

favorite_languages = []

def languages():
    for i in range(add_languages):
        language = input(f"Enter Language {i+1} : ")
        favorite_languages.append(language)

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

def show_languages(*languages):
    for number, language in enumerate(languages, start=1):
        print(number, ".", language)

show_languages(*favorite_languages)

print()
print("="*40)
print("LOCAL VARIABLE DEMO".center(40))
print("="*40)
print()      
def local_var():
    mode = "Translation"
    print("Current Mode : ",mode)
local_var()

print()
print("="*40)
print("GLOBAL VARIABLE DEMO".center(40))
print("="*40)
print() 
app = "BridgeTalk AI"
def global_var():
    print("Application Name : BridgeTalk AI")
global_var()

print()
print("="*40)
print("SETTINGS SAVED SUCCESSFULLY".center(40))
print("="*40)
print() 

print("Thank You For Using BridgeTalk AI Setting Manager !")
print()