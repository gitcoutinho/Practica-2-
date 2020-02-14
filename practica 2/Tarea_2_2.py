#Usuarios
class User():
    def __init__(self,first_name, last_name, mobile, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.mobile=mobile
        self.age=age
        self.country=country
    def describe_user(self):
        print("Usuario: "+self.first_name.title()+" "+self.last_name.title()+ " Celular: "+self.mobile+" Edad: "+self.age+" Pais: "+self.country.title())
    def greet_user(self):
        print("Hola "+self.first_name.title()+" "+self.last_name.title()+" bienvenido!")
    def increment_login_attempts(self):
    
    def reset_loging_attempts(self):
        
    def secure_account(self):
        
us1=User('carlos','coutinho','5565342354','20','mexico')
us1.describe_user()
us1.greet_user()

us2=User('carmen','gonzales','5582390565','23','peru')
us2.describe_user()
us2.greet_user()

us3=User('litzy','otanez','5581204820','19','mexico')
us3.describe_user()
us3.greet_user()

us4=User('hernesto','rojas','5500223388','18','mexico')
us4.describe_user()
us4.greet_user()

us5=User('lalo','nuno','6878458988','19','mexico')
us5.describe_user()
us5.greet_user()

us6=User('laura','mancera','5592304866','19','mexico')
us6.describe_user()
us6.greet_user()

us7=User('ximena','quintanar','5582934056','18','mexico')
us7.describe_user()
us7.greet_user()

us8=User('lizbeth','hernandez','7782034056','20','mexico')
us8.describe_user()
us8.greet_user()

us9=User('miguel','arizmendi','8822308450','20','mexico')
us9.describe_user()
us9.greet_user()

us10=User('karen','servin','6678239455','18','mexico')
us10.describe_user()
us10.greet_user()
