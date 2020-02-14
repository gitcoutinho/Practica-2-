class Car():
    def __init__(self, make, model, year, color='gris', pantalla='si'):
        self.make = make
        self.model = model
        self.year = year
        self.color=color
        self.pantalla=pantalla
        self.odometer_reading=0
    def get_descriptive_name(self):
            long_name = str(self.year)+' '+self.make +' '+self.model
            return long_name.title()
    def read_odometer(self):
            print("This car has " + str(self.odometer_reading)+ " miles on it")

my_new_car=Car('audi','a4','2020')
print(my_new_car.get_descriptive_name())
my_new_car.color= 'amarillo'
my_new_car.pantalla='no'
my_new_car.odometer_reading= 15
my_new_car.get_descriptive_name()
my_new_car.read_odometer()
