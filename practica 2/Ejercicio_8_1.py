class Car():
	"" "Un intento de representar un auto" "" 
	def  __init__ ( self , marca , modelo , año ):
		self.make  =  make 
		self.modelo  =  modelo 
		self.año  =  año 
		self.odometer_reading  =  0
	def  get_descriptive_name ( self ):
		long_name  =  str ( self . year ) +  ''  +  self . hacer  +  ''  +  auto . modelo 
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
	 carga de def ( auto ):
		print ( "El auto se está cargando ..." )

clase  ElectricCar ( Car ):
	"" "Un intento de representar un auto eléctrico" "" 
	def  __init__ ( self , marca , modelo , año ):
		"" "Inicializa los atributos de la clase padre" ""
		Coche . __init__ ( auto , marca , modelo , año )
		auto . tamaño de la batería  =  70
	def  describe_battery ( self ):
		"" "Imprime la tamanio de la batería" ""
		print ( "Este auto tiene un"  +  str ( self . battery_size ) +  "-kWh battery" ))
	 carga de def ( auto ):
		imprimir ( "La batería está casi descargada, el automóvil se está cargando" )


my_tesla  =  ElectricCar ( 'tesla' , 'model s' , 2020 )
print ( my_tesla . get_descriptive_name ())
my_tesla . describe_battery ()
my_tesla . carga ()
