#Sawyer Wood, Pig Latin Converter Skill Practice

word = input("What word do you want to translate?: ")

def translate(word):
    firstletter = word[0]
    translated = word[1:] + firstletter + "ay"
    return translated

print(translate(word))