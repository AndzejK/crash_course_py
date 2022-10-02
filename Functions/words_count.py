def count_words(filename):
    try:
        with open(filename,encoding="utf-8") as f:
            content=f.read()
    except FileNotFoundError:
        print(f"\nSorry, the file {filename} does not exist!")
    else:
        words=content.split()
        num_words=len(words)
        print(f"The file - {filename} - has about ~ {num_words} words")

file_names=["Pride_and_Prejudice.txt","pi_digits.txt","test.txt","A_Room_with_a_View.txt"]


for file_name in file_names:
    count_words(file_name)