file_name="Pride_and_Prejudice.txt"
'''
Pride_and_Prejudice.txt
pi_digits.txt
test.txt
A_Room_with_a_View.txt
'''

# Adding in a TRY block to make secure and more readable app for an end-user
try:
    with open(file_name,encoding="utf-8") as f:
        content=f.read()
except FileNotFoundError:
    print(f"\nSorry, the file {file_name} does not exist!")
else:
# Counting an approximate number of the words in the file_name
    # the string method that finds an empty space, technically we're couting the empty spaces
    # to find the count of the words
    words=content.split()
    num_words=len(words)
    print(f"\nThe file - {file_name} - has about ~ {num_words} words")
