favorite_languages={
    "Andrey":"python",
    "Mike":"C++",
    "Catie":"Java",
    "Lea":"JavaScript",
}

language_lea=favorite_languages["Lea"].title()
print(f"\nLea's favorite language is: {language_lea}")

#get key/value pair which doesn't exist in dic
language_ghost=favorite_languages.get("ghost","Looks like that you're looking for a ghost!")
language_andrey=favorite_languages.get("Andrey","Looks like that you're looking for a ghost!")

print(f"{language_ghost} | {language_andrey}")