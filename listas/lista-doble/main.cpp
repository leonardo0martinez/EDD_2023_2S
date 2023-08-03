#include <iostream>
#include <string>

using namespace std;
using std::string;

// CLASE NODO

class Nodo{
    private:
        int id;
        std::string nombre;
    public:
        // APUNTADOR AL SIGUIENTE Y ANTERIOR
        Nodo * siguiente;
        Nodo * anterior;

        //CONSTRUCTOR DE LA CLASE NODO
        Nodo(int id, std::string nombre){
            this->id = id;
            this->nombre = nombre;
            this->siguiente = NULL;
            this->anterior = NULL;
        }
        
        // GETTESR Y SETTERS
        int getId() { return this->id; }
        std::string getNombre() { return this->nombre; }

        void setId(int id) { this->id = id; }
        void setNombre(std::string nombre) { this->nombre = nombre; }
};

// CLASE LISTA DOBLE
class ListaDoble{
    private:
        Nodo * inicio;
        Nodo * ultimo;
    public:
        ListaDoble(){
            this->inicio = NULL;
            this->ultimo = NULL;
        }

        void insertarAlFinal(int id, std::string nombre){
            // CREACION DEL NODO
            Nodo* nuevoNodo = new Nodo(id, nombre);            
            // VERIFICAR QUE SU LISTA ESTE VACIA
            if(inicio == NULL){
                // AGREGAR NODO AL INICIO
                inicio = nuevoNodo; 
                ultimo = nuevoNodo;
            }else{
                // AGREGAR AL FINAL
                ultimo->siguiente = nuevoNodo;
                nuevoNodo->anterior = ultimo;
                ultimo = nuevoNodo;
            }
        }

        void insertarAlInicio(int id, std::string nombre){
            // CREACION DEL NODO
            Nodo* nuevoNodo = new Nodo(id, nombre);            
            // VERIFICAR QUE SU LISTA ESTE VACIA
            if(inicio == NULL){
                // AGREGAR NODO AL INICIO
                inicio = nuevoNodo; 
                ultimo = nuevoNodo;
            }else{
                // AGREGAR AL PRINCIPIO
                inicio->anterior = nuevoNodo;
                nuevoNodo->siguiente = inicio;
                inicio = nuevoNodo;
            }
        }


        void imprimir(){
            // CREAR EL NODO TEMPORAL
            Nodo * temporal = this->inicio;

            // IMPRESION AL DERECHO
            while(temporal != NULL){
                std::cout << temporal->getNombre() << " -> ";
                temporal = temporal->siguiente;
            }
            std::cout << " NULL" << std::endl;

            // IMPREDCION AL REVES
            temporal = this->ultimo;
            while(temporal != NULL){
                std::cout << temporal->getNombre() << " <- ";
                temporal = temporal->anterior;
            }
            std::cout << " NULL" << std::endl;
        }
};


int main (){

    // DECLARAR LA LISTA ENLAZADA
    ListaDoble * lista = new ListaDoble();
    lista->insertarAlFinal(1, "Nombre 1");
    lista->insertarAlFinal(2, "Nombre 2");
    lista->insertarAlFinal(3, "Nombre 3");
    lista->insertarAlFinal(4, "Nombre 4");
    lista->insertarAlInicio(5, "Nombre 5");
    lista->insertarAlInicio(6, "Nombre 6");

    lista->imprimir();
    return 0;
}