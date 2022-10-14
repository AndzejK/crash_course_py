from unittest import result
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create D6 - 6-sided die
die=Die()

# Make some rolls and store them in the list
results=[]
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyse the results, how many times appeared each number 
frequencies=[]
for value in range(1,die.num_sides+1): # from 1 to 6+1=7 at the last number is not included  
    frequency=results.count(value)
    frequencies.append(frequency)

# Visualise the results
x_values=list(range(1,die.num_sides+1))
data=[Bar(x=x_values, y=frequencies)]

x_axis_config= {"title":"Result"}
y_axis_config= {"title":"Frequency of Result"}
my_layout=Layout(title="Results of rolling one D6 1000 times",xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout},filename="d6.html")
