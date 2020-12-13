**1. Defina las clases que modelan su caso, implementando únicamente el constructor, en Python y en C++. No necesita implementar un método main ni correr ningún código, mientras muestre claramente la relación entre las diferentes clases.**

El código está en este directorio

**2. Resuma en un párrafo corto el modelo que decidió resolver.**

Es una herencia con varias ramas, con información de un asegurado. Los posibles caminos de se muestran a continuación:
Persona>Accidente
Persona>Vehiculo>Carro
Persona>Vehiculo>Moto

Los atributos de cada clase se muestran a continuación

* Persona(string nombre, int identificacion) (padre 1 de todas las clases)
* Accidente(int monto, string frecuencia) (hija de Persona. Contiene el monto y la frecuencia de pago)
* Vehiculo(int placa) (hija de Persona. Contiene el número de placa del vehículo)
* Carro(int monto, string frecuencia) (hija de Vehiculo. Contiene el monto y la frecuencia de pago)
* Moto(int monto, string frecuencia) (hija de Vehiculo. Contiene el monto y la frecuencia de pago)

**3. Explique por qué se puede aplicar herencia en este caso.**

Se puede aplicar herencia porque al haber diferentes tipos de seguro, pero que todos requieren la misma información personal del asegurado, se puede heredar de un padre que contiene esta. Lo mismo con el segundo nivel de vehiculos, se puede tener distinto tipos de vehículos y coberturas, pero todos requieren la placa y marchamo al día para poder ser asegurados. En este caso la herencia ayuda.
