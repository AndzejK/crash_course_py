favourite_languages = {
    "Andrew":["JavaScript","Python","PHP","RegEx"],
    "Michael":["Bash","C++","C#"],
    "Oleg":["SQL","GO","Swift"],
}
# get the values from the dir, two loops, one loop inside another loop
for name,languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")