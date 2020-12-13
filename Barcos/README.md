**1. Defina las clases que modelan su caso, implementando únicamente el constructor, en Python y en C++. No necesita implementar un método main ni correr ningún código, mientras muestre claramente la relación entre las diferentes clases.**

El código está en este directorio

**2. Resuma en un párrafo corto el modelo que decidió resolver.**

Es una herencia multinivel, es decir una clase hereda de otra que hereda de otra, en una línea, en la forma Nación>Tipo>Clase>Barco. (Es sobre barcos de guerra, la historia naval de WW2 es uno de mis intereses). Los atributos de cada clase se muestran a continuación

* Nacion(string pais)
* Tipo (string tipo) eg. Portaaviones, destructor
* Clase (string clase) (muchos eran contruidos en grupo, con características similares)
* Barco (string nombre, int year, string destino) (el nombre del barco, el año en el que fue asignado y lo que le pasó)

**3. Explique por qué se puede aplicar herencia en este caso.**

La mayor parte de los barcos de la segunda guerra mundial cumplen con este esquema que va de mayor a menor, en el que la herencia puede ayudar a reducir la cantidad de código y tiempo, si por ejemplo quiero agregar otro argumento en la clase "Barco" estoy cambiando una línea en lugar de cientas.
