favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'andrew':'c#',
    'akhil':'javascript',
}

# A list who should take my poll
candidates = ["jen","edward","john","andrew","tyson"]
print("\n")
for candidate in candidates:
    if candidate in favourite_languages:
        print(f"Thank you, {candidate.title()} for responding!")
    else:
        print(f"Please, {candidate.title()} take the poll!")
