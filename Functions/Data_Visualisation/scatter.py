import matplotlib.pyplot as plt
plt.style.use("seaborn")
fig, ax=plt.subplots()

# Ploting a single point
#ax.scatter(2,4, s=100) # X,Y

# Get a square
y_values=[]

# Set any range you'd like to have in a square, last digit isn't included 
x_values=range(1,1001)
y_values=[x**2 for x in x_values]

# My way of implementing 
""""
# get square from the set range    
for y in x_values:
    y_values.append(y*y)
    """

# Ploting a range of number
ax.scatter(x_values,y_values, s=10, c=(0, 0.8, 0)) # X,Y - c _ colour

# values close to O produce blacker colour and values close to 1 produce lighter colours

# Set chart title and label axes
ax.set_title("Square numbers", fontsize=20)
ax.set_xlabel("Value (x)", fontsize=12)
ax.set_ylabel("Square of Value (y)", fontsize=12)

# Set size of tick labels 
ax.tick_params(axis="both",which="major",labelsize=12)

# Set the range for each axis X (min and max) and Y (min and max)
ax.axis([0, 1100, 0, 1100000])
plt.show()
