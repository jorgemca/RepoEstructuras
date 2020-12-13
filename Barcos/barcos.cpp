//Jorge Castrillo Rojas - B41570
//Reposición - Herencias

#include <iostream>
using namespace std;
 
class Nacion
{
public:
    Nacion(string pais) //constructor
    {
        cout << "País: " << pais << endl;
    }
};
 
class Tipo: public Nacion //hereda de Nacion
{
public:
    Tipo(string pais, string tipo)
    : Nacion(pais) //constructor
    {
        cout << "Tipo: " << tipo << endl;
    }
};
 
class Clase: public Tipo	//hereda de Tipo
{
public:
    Clase(string pais, string tipo, string clase)
    : Tipo(pais, tipo) //constructor
    {
        cout << "Clase: " << clase << endl;
    }
};

class Barco: public Clase	//hereda de Clase
{
public:
    Barco(string pais, string tipo, string clase, string barco, int year, string destino)
    : Clase(pais, tipo, clase) //constructor
    {
        cout << "Barco: " << barco << endl;
        cout << "Asignado: " << year << endl;
        cout << "Destino: " << destino << endl;
    }
};

//Este main es para mí. Es la primera vez que trabajo con herencias, entonces es para ver si es correcto 
int main()
{
    Barco Formidable("Reino Unido", "Portaaviones", "Illustrious", "Formidable", 1940, "Desguazado, 1953");
}
