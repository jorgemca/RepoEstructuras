//Jorge Castrillo Rojas - B41570
//Reposición - Herencias

#include <iostream>
using namespace std;
 
class Persona
{
public:
    Persona(string nombre, int identificacion) //constructor
    {
        cout << "Nombre: " << nombre << endl;
        cout << "Identificación: " << identificacion << endl;

    }
};
 
class Accidente: public Persona	//hereda de Persona
{
public:
    Accidente(string nombre, int identificacion, int monto, string frecuencia)
    : Persona(nombre, identificacion) //constructor
    {
        cout << "Persona tiene una póliza de accidentes. Monto " << frecuencia << ": ₡" << monto << endl;
    }
};
 
class Vehiculo: public Persona	//hereda de Persona
{
public:
    Vehiculo(string nombre, int identificacion, int placa)
    : Persona(nombre, identificacion) //constructor
    {
        cout << "Placa: " << placa << endl;
    }
};


class Carro: public Vehiculo	//hereda de Vehiculo
{
public:
    Carro(string nombre, int identificacion, int placa, int monto, string frecuencia)
    : Vehiculo(nombre, identificacion, placa) //constructor
    {
        cout << "Persona tiene una póliza de automovil. Monto " << frecuencia << ": ₡" << monto << endl;
    }
};

class Moto: public Vehiculo	//hereda de Vehiculo
{
public:
    Moto(string nombre, int identificacion, int placa, int monto, string frecuencia)
    : Vehiculo(nombre, identificacion, placa) //constructor
    {
        cout << "Persona tiene una póliza de motocicleta. Monto " << frecuencia << ": ₡" << monto << endl;
    }
};


//Este main es para mí. Es la primera vez que trabajo con herencias, entonces es para ver si es correcto 
int main()
{
    Accidente unAccidente("Nombre1 Apellido1", 100000000, 100000, "semestral");
    Carro unCarro("Nombre2 Apellido2", 200000000, 123456, 200000, "trimestral");
    Moto unaMoto("Nombre3 Apellido3", 300000000, 654321, 50000, "cuatrimestral");

}
