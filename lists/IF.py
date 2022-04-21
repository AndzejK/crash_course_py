cars=["audi","bmw","mazda","subaru"]
#Find intials and make them uppercase
cars_edited=[]
for car in cars:
    if car=="bmw":
        cars_edited.append(car.upper())
    else:
        cars_edited.append(car.title())
print(cars)
print(cars_edited)  

#       a bit of theory of IF (condition of interest)      
#inside IF we have test="conditional TEST" either it's TRUE or FALSE
car="Audi" 
#if it's test=TRUE Python begins IF statement, what we want to perform
print(car.lower()=="audi") #yes, it's case sensetive 
#if it's test=FALSE Python skips/ignores IF statement
print(car=="bmw")
#.lower() the method doesnt change the original value unless I set to a diff var

#checking for inequality => !+
#less than OR equal to <= | more/greater than OR equal to >= 
print(f"this is less than: 2<8 - {2<8}")
print(f"this is more than: 7>5 - {7>5}")
        
        ### Multiple conditions of interest 
#When I NEED an overall condition to be True simultaneously,  e.x two conditions, use AND operator
#When I'm satisfied with just ONE condition being True in an overall condition use OR operator

ages=[16,16,17,19,22,15,19,39,32,21,30,31]
guests_above_21=[]
guests_below_21=[]
for age in ages:
    if age>=21:
        guests_above_21.append(age)
    else:
        guests_below_21.append(age)
print(f"\nWe have {len(guests_above_21)} adults.")
print(guests_above_21)
print(f"We have {len(guests_below_21)} kids.")
print(guests_below_21)
        

