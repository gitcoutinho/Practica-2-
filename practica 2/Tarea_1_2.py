class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_reserved):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_reserved=0
        #self.number_reserved=number_reserved
    def describe_restaurant(self):
        print("El restaurante "+self.restaurant_name.title()+" es de cocina "+self.cuisine_type)
    def open_restaurant(self):
        #self.number_reserved=90
        print("El restaurante "+self.restaurant_name.title()+" esta abierto"+" y se ha atendido a "+str(self.number_reserved)+' '+"clientes")
    def set_number_reserved(self):
        if self.number_reserved >= 1:
            print("el nuevo numero de cliente es: "+self.number_reserved)
        else:
            print("Echenle ganas, no hay clientes atendidos xd")
        
#Restaurant
"""restaurante=Restaurant('busines', 'fria')
restaurante.describe_restaurant()#El restaurante Busines es de cocina fria
restaurante.open_restaurant()#El restaurante Busines esta abierto
#Tres Resrtaurantes
restaurante1=Restaurant('kalifa', 'china')
restaurante1.describe_restaurant()#El restaurante Kalifa es de cocina china
restaurante1.open_restaurant()#El restaurante Kalifa esta abierto

restaurante2=Restaurant('maravilla','japonesa')
restaurante2.describe_restaurant()
restaurante2.open_restaurant()

restaurante3=Restaurant('slip','italiana')
restaurante3.describe_restaurant()
restaurante3.open_restaurant()"""

#Practica 2
rest4=Restaurant('cror','suisa',90)
rest4.describe_restaurant()
rest4.open_restaurant()
rest4.set_number_reserved()