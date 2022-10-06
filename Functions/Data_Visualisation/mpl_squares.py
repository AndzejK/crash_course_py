import matplotlib.pyplot as plt
# more about - matplotlib.pyplot - https://matplotlib.org/stable/api/pyplot_summary.html?highlight=pyplot#module-matplotlib.pyplot
squares = [1, 4, 9, 16, 25]
fig, ax=plt.subplots()
ax.plot(squares)
plt.show()