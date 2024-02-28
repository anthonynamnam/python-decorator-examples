class Car:
    '''Object for Car.'''
    def __init__(self, brand: str, weight: float, color:str, make_year: int):
        self.brand = brand
        self.weight = weight # in kilograms
        self.color = color  
        self.make_year = make_year

    def __repr__(self):
        return f"Car(brand={self.brand}, weight={self.weight}, color={self.color}, make_year={self.make_year})"


my_car = Car("Audi",1940.54,"red",2019)
print(my_car)


from dataclasses import dataclass 
@dataclass
class Car_class:
    '''Object for Car.'''
    brand: str
    weight: float
    color: str
    make_year: int

my_car_class = Car_class("Toyota",1501.54,"orange",2008)
print(my_car_class)