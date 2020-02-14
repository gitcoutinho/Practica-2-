class Car():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def get_describe_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car=Car('audi','a4','2020')
print(my_new_car.get_describe_name())

