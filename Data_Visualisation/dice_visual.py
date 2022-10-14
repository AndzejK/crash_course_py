from unittest import result
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create D6 x2 - 6-sided die
die_1=Die()
die_2=Die()

# Make some rolls and store them in the list
results=[]
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# Analyse the results, how many times appeared each number 
frequencies=[]
# Determine the maximum result -> 6+6 = 12
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1): # from 2 to 12+1=13 at the last number is not included  
    frequency=results.count(value)
    frequencies.append(frequency)

# Visualise the results
x_values=list(range(2,max_result+1))
data=[Bar(x=x_values, y=frequencies)]

x_axis_config= {"title":"Result", "dtick":1}
y_axis_config= {"title":"Frequency of Result"}
my_layout=Layout(title="Results of rolling two D6 1000 times",xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout},filename="d6_d6.html")
