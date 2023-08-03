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
        // APUNTADOR AL SIGUIENTE
        Nodo * siguiente;

        //CONSTRUCTOR DE LA CLASE NODO
        Nodo(int id, std::string nombre){
            this->id = id;
            this->nombre = nombre;
            this->siguiente = NULL;
        }
        
        Nodo(int id, std::string nombre, Nodo* siguiente){
            this->id = id;
            this->nombre = nombre;
            this->siguiente = siguiente;
        }

        // GETTESR Y SETTERS
        int getId() { return this->id; }
        std::string getNombre() { return this->nombre; }

        void setId(int id) { this->id = id; }
        void setNombre(std::string nombre) { this->nombre = nombre; }
};

// CLASE LISTA
class Lista{
    private:
        Nodo * inicio;
    public:
        Lista(){
            this->inicio = NULL;
        }

        void insertar(int id, std::string nombre){
            // CREACION DEL NODO
            Nodo* nuevoNodo = new Nodo(id, nombre);            
            // Nodo* nuevo2Nodo = new Nodo(id, nombre, nuevoNodo);
            
            // VERIFICAR QUE SU LISTA ESTE VACIA
            if(inicio == NULL){
                // AGREGAR NODO AL INICIO
                inicio = nuevoNodo; 
            }else{
                // CREAR EL NODO TEMPORAL
                Nodo * temporal = inicio;
                // ENCONTRAR ULTIMO NODO
                while(temporal->siguiente != NULL){
                    temporal = temporal->siguiente;
                }
                // AGREGAR NODO
                temporal->siguiente = nuevoNodo;
            }
        }

        void imprimir(){
            // CREAR EL NODO TEMPORAL
            Nodo * temporal = this->inicio;
            // ENCONTRAR ULTIMO NODO
            while(temporal != NULL){
                std::cout << temporal->getNombre() << " -> ";
                temporal = temporal->siguiente;
            }
            // AGREGAR NODO
            std::cout << " NULL" << std::endl;
        }

        Nodo* buscar(int id){
            // CREAR EL NODO TEMPORAL
            Nodo * temporal = this->inicio;
            // ENCONTRAR ULTIMO NODO
            while(temporal != NULL){
                if(id == temporal->getId()){
                    return temporal;
                }
                temporal = temporal->siguiente;
            }
            return NULL;
        }
};


int main (){

    // DECLARAR LA LISTA ENLAZADA
    Lista * lista = new Lista();
    lista->insertar(1, "Nombre 1");
    lista->insertar(2, "Nombre 2");
    lista->insertar(3, "Nombre 3");
    lista->insertar(4, "Nombre 4");

    lista->imprimir();
    Nodo * temp = lista->buscar(3);
    std::cout << "Resultado de Busqueda: " << temp->getNombre() << std::endl;
    // std::cout << "Hola mundo" << std::endl;
    return 0;
}