# ============================================
# Project: BridgeTalk AI Language Analyzer
# Week 02 - Day 02: Python Sets
#
# Features:
# - Manage supported languages
# - Check language support
# - Add and remove languages
# - Compare language groups using set operations
# ============================================

print("="*40)
print("    BRIDGETALK AI LANGUAGE ANALYZER")
print("="*40,"\n")

supported_languages = {
    "English" , "Urdu" , "Turkish"
}
print("Supported Languages : \n" )
for language in supported_languages:
    print (f"- {language}")
print("-"*40)

supported_languages.update({"Arabic","Spanish"})
print("Adding New Languages ...")
print("added : Arabic , Spanish","\n")

print("Updated Languages : \n")
for language in supported_languages:
    print(f"- {language}")
print("-"*40)

print("Checking Language Support ...\n")
language_support = input("Enter Language to Check : ").title()

if language_support in supported_languages :
    print(f"\n✅ {language_support} is Supported .\n")
else :
    print(f"\n❌ {language_support} is not supported .\n")
print("-"*40,"\n")   

print("Removing a Language ...")
remove_language = input("\nEnter Language to Remove : ").title()

if remove_language in supported_languages :
    supported_languages.remove(remove_language)
    print(f"\n✅ {remove_language} has been removed successfully .\n")
else :
    print(f"\n❌ {remove_language} doesn't exist .\n")
print("-"*40,"\n")  

print("Current Languages : \n")
for language in supported_languages:
    print (f"- {language}")
print("-"*40,"\n")



english_group = {
    "Ahmed",
    "Fatima",
    "Ali",
    "Faiz"
}

turkish_group = {
    "Fatima",
    "John",
    "Den",
    "Ali"
}

print("New User ...\n")
language = input("Enter Known Language :").title().strip()

if language in supported_languages :
    name = input("Enter Your Name : ").title().strip()
    if language == "Turkish" :
        turkish_group.add(name)
    elif language == "English" :
        english_group.add(name)

else:
    print("Language not supported .")


print("-"*40,"\n")

print("Comparing Language Groups ...")
print("\nEnglish Group :   " )
for user in english_group:
    print(f"- {user}")
print("\nTurkish Group :   ")
for user in turkish_group:
    print(f"- {user}")

both_languages = english_group & turkish_group
print("\nUsers who know both languages :  ")
for user in both_languages:
    print(f"- {user}")

one_languages = english_group ^ turkish_group
print("\nUsers who know exactly one languages :  ")
for user in one_languages:
    print(f"- {user}")

only_English = english_group - turkish_group
print("\nUsers who know only English :  ")
for user in only_English:
    print(f"- {user}")

only_Turkish = turkish_group - english_group
print("\nUsers who know only Turkish :  ")
for user in only_Turkish:
    print(f"- {user}")
    
all_users = english_group | turkish_group
print("\nAll Users:")
for user in all_users:
    print(f"- {user}")
print("-"*40,"\n")

print("Total Supported Languages : ",len(supported_languages),"\n")

print("="*40)
print("   THANK YOU FOR USING BRIDGETALK AI ")
print("="*40,"\n")


