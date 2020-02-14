class Car():
    """Clase tipo coche"""
    def __init__(self, make, model, year, color, odometer_reading):
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
    def read_odometer(self):
        """Imprime los kilometros recorrido por el auto"""
        print("This car has " + str(self.odometer_reading) + " miles on it")
    def atributo_nuevo1 (self):
        self.color='gris'
        print ("El color de su coche es: "+self.color)
    def atributo_nuevo2 (self):
        self.odometer_reading=67
        if self.odometer_reading>=0:
            print("Su kilometraje es de: "+str(self.odometer_reading))
        else:
            print ("Kilometrage incorrecto. Verifica valor.") 
        
#Error
        #Error de tipo: 
        #leer el odómetro toma exactamente 
        #2 argumentos (1 dado)

my_new_car = Car('audi','a4','2020','green','150')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.atributo_nuevo1()
my_new_car.atributo_nuevo2()


