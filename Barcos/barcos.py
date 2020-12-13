##Jorge Castrillo Rojas - B41570
#3Reposición - Herencias

class Nacion():       
    #Constructor 
    def __init__(self, pais): 
        self.pais = pais 
    #
    def getNacion(self):
        print("País:", self.pais)
      
class Tipo(Nacion): 
    #Constructor 
    def __init__(self, pais, tipo):
        Nacion.__init__(self, pais)
        self.tipo = tipo

    def getTipo(self): 
        print("Tipo:", self.tipo)

class Clase(Tipo): 
    #Constructor 
    def __init__(self, pais, tipo, clase):
        Tipo.__init__(self, pais, tipo)
        self.clase = clase

    def getClase(self): 
        print("Clase:", self.clase)

class Barco(Clase): 
    #Constructor 
    def __init__(self, pais, tipo, clase, barco, year, destino):
        Clase.__init__(self, pais, tipo, clase)
        self.barco = barco
        self.year = year
        self.destino = destino

    def getBarco(self): 
        print("Barco:", self.barco)

    def getYear(self): 
        print("Asignado:", self.year)

    def getDestino(self): 
        print("Destino:", self.destino)

   
# Ejemplo para ver el funcionamiento del código 
formidable = Barco("Reino Unido", "Portaaviones", "Illustrious", "Formidable", 1940, "Desguazado, 1953")
formidable.getNacion()
formidable.getTipo()
formidable.getClase()
formidable.getBarco()
formidable.getYear()
formidable.getDestino()
