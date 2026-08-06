#  Exercise 1 :  Remove Duplicate Data

Given:

languages = [
    "English",
    "Urdu",
    "English",
    "Turkish",
    "Urdu",
    "Arabic"
]

Tasks:

Convert this list into a set.
Print the unique languages.

## Code 

```python

languages = [
    "English",
    "Urdu",
    "English",
    "Turkish",
    "Urdu",
    "Arabic"
]

set_languages = set(languages)
print(set_languages)

```

## Output 

```
{'Arabic', 'English', 'Urdu', 'Turkish'}

```

#  Exercise 2 : Language Support Checker

Given:

supported_languages = {
    "English",
    "Urdu",
    "Turkish"
}

user_language = "Arabic"

Task:

Check whether the user's language is supported and print an appropriate message.

## Code 

```python

supported_languages = {
    "English",
    "Urdu",
    "Turkish"
}

user_language = "Arabic"

if user_language in supported_languages :
    print("Language Supported !")
else :
    print("language not supported !")

```
## Output 

```
language not supported !

```

#  Exercise 3 : AI User Group Analysis

Given:

english_users = {
    "Ali",
    "Ahmed",
    "Fatima",
    "Sara"
}

turkish_users = {
    "Ahmed",
    "Fatima",
    "John"
}

Find:

Users who know both languages.
All users who know at least one language.
Users who only know English.
Users who only know Turkish.

## Code 

```python 

#(Users who know both languages.
#All users who know at least one language.
#Users who only know English.
#Users who only know Turkish.)

english_users = {
    "Ali",
    "Ahmed",
    "Fatima",
    "Sara"
}

turkish_users = {
    "Ahmed",
    "Fatima",
    "John"
}

both_languages = english_users & turkish_users
print("Users who know both languages : ",both_languages) 

one_language = english_users ^ turkish_users
print("All users who know exactly one language : ",one_language)

only_english = english_users - turkish_users
print("Users who only know English : ",only_english)

only_turkish =  turkish_users - english_users
print("Users who only know Turkish : ",only_turkish)

```

## Code 

```
Users who know both languages :  {'Fatima', 'Ahmed'}
All users who know exactly one language :  {'Ali', 'John', 'Sara'}
Users who only know English :  {'Ali', 'Sara'}
Users who only know Turkish :  {'John'}

```

# Exercise 4 : Updating AI Data

Given:

languages = {
    "English",
    "Urdu"
}

New languages:

{
    "Turkish",
    "Hindi",
    "Arabic"
}

Tasks:

Add all new languages.
Remove "Arabic".
Add "Chinese".
Print the final set.

## Code

```python 

languages = {
    "English",
    "Urdu"
}

new_languages={
    
    "Turkish",
    "Hindi",
    "Arabic"
}

languages.update(new_languages)

languages .remove("Arabic")
languages.add("Chinese")
print("Final List : ",languages)

```

## Output 

```
Final List :  {'Turkish', 'Chinese', 'Hindi', 'Urdu', 'English'}

```

#  Exercise 5 : User Account Management

Given:

active_users = {
    "Ali",
    "Ahmed",
    "Fatima"
}

Tasks:

Remove "Ahmed" from active users.
Safely remove "John" if he exists.
Create a backup copy of the user data.

## Code 

```python 

active_users = {
    "Ali",
    "Ahmed",
    "Fatima"
}

backup_user = active_users.copy()
print("Backup user record : ",backup_user)
remove_users = input("Enter User to Remove : ")
if remove_users in active_users:
    active_users .remove(remove_users)
else:
    print("User Not Found !")

print("Active Users : ",active_users)

```
## Output 

```
Backup user record :  {'Ali', 'Ahmed', 'Fatima'}
Enter User to Remove : Ali
Active Users :  {'Ahmed', 'Fatima'}

```

#  Exercise 6 : AI Dataset Comparison

Given:

dataset_A = {
    "Python",
    "AI",
    "Machine Learning",
    "Data Science"
}

dataset_B = {
    "AI",
    "Deep Learning",
    "Python",
    "Robotics"
}

Find:

Common topics in both datasets.
All available topics.
Topics only in dataset_A.
Topics that are different in both datasets.

## Code 

```python


dataset_A = {
    "Python",
    "AI",
    "Machine Learning",
    "Data Science"
}

dataset_B = {
    "AI",
    "Deep Learning",
    "Python",
    "Robotics"
}

all_topics = dataset_A | dataset_B
print("All available topics : ",all_topics)

common_topics = dataset_A & dataset_B
print("Common topics in both datasets : ",common_topics)

only_A = dataset_A - dataset_B
print("Topics only in dataset_A : ",only_A)

diff_topics = dataset_B ^ dataset_A
print("Topics that are different in both datasets : ",diff_topics)

```
## Output 

```
All available topics :  {'Data Science', 'Python', 'AI', 'Machine Learning', 'Robotics', 'Deep Learning'}
Common topics in both datasets :  {'Python', 'AI'}
Topics only in dataset_A :  {'Data Science', 'Machine Learning'}
Topics that are different in both datasets :  {'Data Science', 'Machine Learning', 'Robotics', 'Deep Learning'}

```
