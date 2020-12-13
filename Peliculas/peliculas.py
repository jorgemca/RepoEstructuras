##Jorge Castrillo Rojas - B41570
#3Reposición - Herencias

class InformacionPelicula():       
    #Constructor 
    def __init__(self, nombre, director, year, genero, pais): 
        self.nombre = nombre 
        self.director = director
        self.year = year
        self.genero = genero
        self.pais = pais
    #
    def getInfoPelicula(self):
        print("Película:", self.nombre)
        print("\nEspecificaciones de la película: ")
        print("Director:", self.director)
        print("Año:", self.year)
        print("Genero:", self.genero)
        print("País:", self.pais)

class InformacionVideo(): 
    #Constructor 
    def __init__(self, duracion, audio, subtitulos, size):
        self.duracion = duracion
        self.audio = audio
        self.subtitulos = subtitulos
        self.size = size

    def getInfoVideo(self): 
        print("\nEspecificaciones de video: ")
        print("Duración:", self.duracion, "minutos")
        print("Audio:", self.audio)
        print("Subtitulos:", self.subtitulos)
        print("Tamaño:", self.size, "GB")

class Comentarios(): 
    #Constructor 
    def __init__(self, comentario):
        #Tipo.__init__(self, pais, tipo)
        self.comentario = comentario

    def getComentario(self): 
        print("\nComentario:", self.comentario)

class Pelicula(InformacionPelicula, InformacionVideo, Comentarios): 
    #Constructor 
    def __init__(self, nombre, director, year, genero, pais, duracion, audio, subtitulos, size, comentario):
        InformacionPelicula.__init__(self, nombre, director, year, genero, pais)
        InformacionVideo.__init__(self, duracion, audio, subtitulos, size)
        Comentarios.__init__(self, comentario)


# Ejemplo para ver el funcionamiento del código 
SwordOfDoom = Pelicula("The Sword of Doom", "Kihachi Okamoto", "Jidai", 1966, "Japón", 120, "JP", "EN, ES", 2.9, "Es el mismo actor de Harakiri. También aparece Mifune. No lineal, basada en una novela publicada por partes en un periódico")
SwordOfDoom.getInfoPelicula()
SwordOfDoom.getInfoVideo()
SwordOfDoom.getComentario()