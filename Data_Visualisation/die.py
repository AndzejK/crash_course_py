from random import randint

class Die:
    """A class representing a single class"""

    def __init__(self,num_sides=6):
        """Assume a six-side die"""
        self.num_sides=num_sides
    
    def roll(self):
        """Return a radnom value between 1 and a number if sides"""
        return randint(1,self.num_sides)
        