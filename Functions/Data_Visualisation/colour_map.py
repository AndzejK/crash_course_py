"""
A colormap is a series of colors in a gradient that moves from 
a starting to an ending color. You use colormaps in visualizations 
to emphasize a pattern in the data. For example, you might make 
low values a light color and high values a darker color.
"""

import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values]

plt.style.use("seaborn")
fig, ax=plt.subplots()


#Here’s how to assign each point a color based on its y-value
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Set chart title and label axes
ax.set_title("Square numbers", fontsize=20)
ax.set_xlabel("Value (x)", fontsize=12)
ax.set_ylabel("Square of Value (y)", fontsize=12)

# Set size of tick labels 
ax.tick_params(axis="both",which="major",labelsize=12)

# Set the range for each axis X (min and max) and Y (min and max)
ax.axis([0, 1100, 0, 1100000])

# just display a figure
#plt.show()

# Save a figure
plt.savefig("squares_plot.png")


