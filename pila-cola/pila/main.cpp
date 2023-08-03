#include <iostream>
#include <string>

using namespace std;
using std::string;

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
        // GETTESR Y SETTERS
        int getId() { return this->id; }
        std::string getNombre() { return this->nombre; }

        void setId(int id) { this->id = id; }
        void setNombre(std::string nombre) { this->nombre = nombre; }
};


class Pila{
    private:
        Nodo * inicio;
    public:
        Pila(){
            this->inicio = NULL;
        }

        // INSERTARLO AL PRINCIPIO
        void push(int id, std::string nombre){
            Nodo * nuevoNodo = new Nodo(id, nombre);
            if(this->inicio == NULL){
                this->inicio = nuevoNodo;
            }else{
                Nodo * temp = this->inicio;
                this->inicio =  nuevoNodo;
                nuevoNodo->siguiente =  temp;
            }
        }

        // ELIMINAR EL ULTIMO
        Nodo * pop(){
            if(this->inicio == NULL){
                return NULL;
            }else{
                Nodo * temp =  this->inicio;
                this->inicio = this->inicio->siguiente;
                // std::cout << this->inicio->getNombre() << std::endl;
                return temp;
            }
        }

        // IMPRIMIR EN CONSOLA
        void imprimir(){
            if(this->inicio != NULL){
                Nodo * temp = this-> inicio;
                while(temp != NULL){
                    std::cout << temp->getNombre() << "-> ";
                    temp = temp->siguiente;
                }
                std::cout << "NULL" << std::endl;
            }else{
                std::cout << "VACIO" << std::endl;
            }
        }
};


int main(){

    Pila * pila =  new Pila();

    pila->push(1, "Nombre 1");
    pila->push(2, "Nombre 2");
    pila->push(3, "Nombre 3");
    pila->push(4, "Nombre 4");
    pila->push(5, "Nombre 5");

    pila->imprimir();
    
    // std::cout << "Antes del pop" << std::endl;

    Nodo* temp = pila->pop();

    std::cout << "Resultado del pop:" << temp->getNombre() << std::endl;

    pila->imprimir();

    Nodo* temp2 = pila->pop();

    std::cout << "Resultado del pop2:" << temp2->getNombre() << std::endl;

    pila->imprimir();
};
