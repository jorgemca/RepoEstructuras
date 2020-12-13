//Jorge Castrillo Rojas - B41570
//Reposición - Herencias

#include <iostream>
using namespace std;
 
class InformacionVideo
{
public:
    InformacionVideo(int duracion, string audio, string subtitulos, float size) //constructor
    {
        cout << "\nEspecificaciones de video: " << endl;
        cout << "Duración: " << duracion << "minutos" << endl;
        cout << "Audio: " << audio << endl;
        cout << "Subtítulos: " << subtitulos << endl;
        cout << "Tamaño: " << size << "GB" << endl;
    }
};
 
class InformacionPelicula
{
public:
    InformacionPelicula(string nombre, string director, string genero, int year, string pais) //constructor
    {   
        cout << "Película: " << nombre << endl;
        cout << "\nEspecificaciones de la película: " << endl;
        cout << "Director: " << director << endl;
        cout << "Género: " << genero << endl;
        cout << "Año: " << year << endl;
        cout << "País: " << pais << endl;    
    }
};

class Comentarios
{
public:
    Comentarios(string comentario) //constructor
    {
        cout << "Comentarios: " << comentario << endl;
    }
};
 

class Pelicula: public InformacionPelicula, public InformacionVideo, public Comentarios	//hereda de InformacionPelicula, InformacionVideo y Comentarios
{
public:
    Pelicula(string nombre, string director, string genero, int year, string pais, int duracion, string audio, string subtitulos, float size, string comentario)
    : InformacionPelicula(nombre, director, genero, year, pais), InformacionVideo(duracion, audio, subtitulos, size), Comentarios(comentario) //constructor
    {
    }
};

//Este main es para mí. Es la primera vez que trabajo con herencias, entonces es para ver si es correcto 
int main()
{
    Pelicula SwordOfDoom("The Sword of Doom", "Kihachi Okamoto", "Jidai", 1966, "Japón", 120, "JP", "EN, ES", 2.9, "Es el mismo actor de Harakiri. También aparece Mifune. No lineal, basada en una novela publicada por partes en un periódico");
}
