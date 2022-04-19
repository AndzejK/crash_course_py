from multiprocessing.dummy import current_process


year_born =1990
current_year=2022
age=current_year - year_born
name='andzej'
name_book="The Memory Book by"
book_author_1="harry"
book_author_2="jerry"
msg= "My name is:",name.title(), "I am",age,"years old"

#Interesting topic adding, using a txt and varible at the same time
    #we can even modify a variable inside f-string (format string)
    #in my casw I use the method "title()"
complex_text=f"{name_book} by {book_author_1.title()} and {book_author_2.title()}"
print(msg)

check_type_msg=type(msg)
print(check_type_msg)
print("\n------")
print(complex_text)
print("------\n")

#\t >> TAB;
#\n >> ENTER, newline;
print(f"Names:\n\t{book_author_1}\n\t{book_author_2}\n\tAndrey")
print("------\n")
arr_names=["andzej","Andrey","Andrius","Andrew"]
print(f"{arr_names[1].title()}")
var_whitespace_both_side="  Whitespace "
print(f"whitespace:{var_whitespace_both_side} both sides")
no_white_left=var_whitespace_both_side.lstrip()
print(f"whitespace:{no_white_left} rigt side left")
no_white_right=var_whitespace_both_side.rstrip()
print(f"whitespace:{no_white_right} left side left")
no_whitespace=var_whitespace_both_side.strip()
print(f"whitespace:{no_whitespace} no spcae")