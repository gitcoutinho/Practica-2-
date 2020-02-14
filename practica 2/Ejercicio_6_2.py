class Car():
	"" "Un intento de representar un auto" "" 
	def  __init__ (self, make, modelo, año):
		self.make  =  make 
		self.modelo  =  modelo 
		self.año  =  año 
		self.odometer_reading  =  0
	def  get_descriptive_name ( self ):
		long_name  =  str ( self . year ) +  ','  +  self . make  +  ','  +  self . modelo 
		return  long_name . título ()
	def  read_odometer ( self ):
		print ( "Este auto tiene"  +  str ( self . odometer_reading ) +  "miles en él" )
	def  update_odometer ( auto , kilometraje ):
		Si  el kilometraje  > =  auto . odometer_reading :
			auto . odometer_reading  =  kilometraje
		más :
			print ( "¡No puedes hacer retroceder un odómetro!" )
	def  increment_odometer ( self , miles ):
		auto . odometer_reading  + =  millas

clase  ElectricCar ( Car ):
	"" "Un intento de representar un auto eléctrico" "" 
	def  __init__ ( self , marca , modelo , año ):
		"" "Inicializa los atributos de la clase padre" "" 
		Coche . __init__ ( auto , marca , modelo , año )
my_tesla  =  ElectricCar ( 'tesla' , 'model s' , 2020 )
print ( my_tesla . get_descriptive_name ())

clase  HybridCar ( Car ):
	"" "Un intento de representar un auto eléctrico" "" 
	def  __init__ ( self , marca , modelo , año ):
		"" "Inicializa los atributos de la clase padre" "" 
		Coche . __init__ ( auto , marca , modelo , año )
my_Hybridcar  =  HybridCar ( 'BMW' , 'i3' , 2020 )
print ( my_Hybridcar . get_descriptive_name ())
clase  FuelCar ( Car ):
	"" "Un intento de representar un auto eléctrico" "" 
	def  __init__ ( self , marca , modelo , año ):
		"" "Inicializa los atributos de la clase padre" "" 
		Coche . __init__ ( auto , marca , modelo , año )
my_FuelCar =  FuelCar ( 'mustang' , 'shelby' , 2020 )
print ( my_FuelCar . get_descriptive_name ())
