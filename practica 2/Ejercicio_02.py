class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year, color, pantalla):
        """Inicializacion de los atributos"""
        self.make = make
        self.model = model
        self.year = year
        self.color= 'azul'
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """ Imprime las caracteristicas en la pantalla"""
        long_name = str(self.year)+' '+self.make +' '+self.model
        return long_name.title()
    def read_odometer(sefl,odometer_reading):
        '''self.odometer_reading=0'''
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(sefl.odometer_reading) + " miles on it")
#Error
        #Error de tipo: 
        #leer el odómetro toma exactamente 
        #2 argumentos (1 dado)

my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
