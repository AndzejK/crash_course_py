# Matlablib
import matplotlib.pyplot as plt
# more about - matplotlib.pyplot - https://matplotlib.org/stable/api/pyplot_summary.html?highlight=pyplot#module-matplotlib.pyplot

input_valus=[1,2,3,4,5,6]  # X values but default :)
squares = [1, 4, 9, 16, 25,36] #Y values are as attemps/times/order
fig, ax=plt.subplots() # subplot is FN that can generate one or more plots in the same Figure
                    # fig - represets the entire figure or collection of plot 
ax.plot(input_valus,squares,linewidth=3)

# Set chart title and lbl axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value (x)", fontsize=14)
ax.set_ylabel("Square of Value (y)", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both",labelsize=12)
plt.show()