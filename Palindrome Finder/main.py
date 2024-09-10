#Sawyer Wood, SkillPractice: Palindrome.

word = input("What is the word you want to put in it?: " )
word = str.lower(word)
if word == word [::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")