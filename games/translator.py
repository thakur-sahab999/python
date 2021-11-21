#Retard language name

def translate(phrase):
    translations = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
               translations = translations + "L"

            else:
                translations = translations + "l"
        else:translations = translations + letter

    return translations

print(translate(input("Enter a phrase: ")))