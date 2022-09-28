# We create a class
class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
   
    def get_brand_year(self):
        print(f"You entered: {self.brand} and its year is {self.year}")

# We create here an object / an instance from the class?
audi=Car("a3",2020)
audi.get_brand_year()
# We access the values of the created object, audi
print(f"The brand of Audi is {audi.brand} and {audi.year} year")