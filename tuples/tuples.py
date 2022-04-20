#72 characters per comment
#Tuple is the same as a List but we can't change the items inside the tuple, 
#they are immutable; otherwise it will raise an error
#instead of [] we use () for tuples, the techniques we can apply for tuples 
# as for lists
mathematical_constants=(3.141,2.509,2.718,1.731)
for constant in mathematical_constants:
    print(constant)
#We can't change items in a Tuple but we can redefine the whole tuple
print("\n")
mathematical_constants=(0.26,0.31,2.71,3.73)
for constant in mathematical_constants:
    print(constant)
print("\n")
#Buffet
basic_foods=("curry","borshch","stir-fry","dahl","pancakes")
print("Basic menu:")
for food in basic_foods:
    print(f"\t{food}")
#revised menu
print("\nRevised menu:")
basic_foods=("Meatloaf","burger","stir-fry","dahl","pancakes")
for food in basic_foods:
    print(f"\t{food}")
