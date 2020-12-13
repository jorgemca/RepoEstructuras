##Jorge Castrillo Rojas - B41570
#3Reposición - Herencias

class Persona():       
    #Constructor 
    def __init__(self, nombre, identificacion): 
        self.nombre = nombre 
        self.identificacion = identificacion 

    def getDatosPersonales(self):
        print("Nombre:", self.nombre)
        print("Identificacion:", self.identificacion)
      
class Accidente(Persona): #hereda de Persona
    #Constructor 
    def __init__(self, nombre, identificacion, monto, frecuencia):
        Persona.__init__(self, nombre, identificacion)
        self.monto = monto
        self.frecuencia = frecuencia

    def getPoliza(self): 
        print("Persona tiene una póliza de accidentes. Monto ", self.frecuencia,": ₡", self.monto)


class Vehiculo(Persona): #hereda de Persona
    #Constructor 
    def __init__(self, nombre, identificacion, placa):
        Persona.__init__(self, nombre, identificacion)
        self.placa = placa

    def getPlaca(self): 
        print("Placa: ", self.placa)

class Carro(Vehiculo):	#hereda de Vehiculo
    #Constructor 
    def __init__(self, nombre, identificacion, placa, monto, frecuencia):
        Vehiculo.__init__(self, nombre, identificacion, placa)
        self.monto = monto
        self.frecuencia = frecuencia

    def getPoliza(self): 
        print("Persona tiene una póliza de automovil. Monto ", self.frecuencia,": ₡", self.monto)

class Moto(Vehiculo):	#hereda de Vehiculo
    #Constructor 
    def __init__(self, nombre, identificacion, placa, monto, frecuencia):
        Vehiculo.__init__(self, nombre, identificacion, placa)
        self.monto = monto
        self.frecuencia = frecuencia

    def getPoliza(self): 
        print("Persona tiene una póliza de motocicleta. Monto ", self.frecuencia,": ₡", self.monto)

   
# Ejemplo para ver el funcionamiento del código 
accidente = Accidente("Nombre1 Apellido1", 100000000, 100000, "semestral")
accidente.getDatosPersonales()
accidente.getPoliza()

auto = Carro("Nombre2 Apellido2", 200000000, 123456, 200000, "trimestral")
auto.getDatosPersonales()
auto.getPlaca
auto.getPoliza()

moto = Moto("Nombre3 Apellido3", 300000000, 654321, 50000, "cuatrimestral")
moto.getDatosPersonales()
moto.getPlaca
moto.getPoliza()
