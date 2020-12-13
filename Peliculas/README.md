**1. Defina las clases que modelan su caso, implementando únicamente el constructor, en Python y en C++. No necesita implementar un método main ni correr ningún código, mientras muestre claramente la relación entre las diferentes clases.**

El código está en este directorio

**2. Resuma en un párrafo corto el modelo que decidió resolver.**

Es una herencia en la que una hija hereda de varios padres, en una línea, en la forma

(Información de la Película, Información del video, Comentarios) >>> Película

Los atributos de cada clase se muestran a continuación

* InformacionPelicula(string nombre, string director, string genero, int year, string pais) (padre 1, contiene información de la película como tal)
* InformacionVideo(int duracion, string audio, string subtitulos, float size) (padre 2, contiene información del vídeo como el tamaño, duración, etc)
* Comentarios(string comentario) (padre 3, contiene comentarios que uno quiera agregar)
* Pelicula (esta hija hereda de los padres)

**3. Explique por qué se puede aplicar herencia en este caso.**

Se puede aplicar herencia porque hay una clase que quiere usar atributos de varias otras clases, y es útil porque si quisiera agregar otros atributos a los padres se ahorra tiempo modificando pocas líneas de código.
