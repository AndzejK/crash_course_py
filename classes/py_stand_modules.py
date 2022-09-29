# RANDOM is a built-in module that has a set of modules
from random import randint,choice
random_number_between_0_10=randint(0,10)
methods_in_RANDOM_module=["uniform()","triangular()","betavariate()","gauss()"]
# Print random method from a given list
random_method=choice(methods_in_RANDOM_module)
print(random_number_between_0_10)
print(random_method)