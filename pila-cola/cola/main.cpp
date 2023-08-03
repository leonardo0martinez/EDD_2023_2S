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


class Cola{
    private:
        Nodo* inicio;
        int size;
    public:
        Cola(){
            this->inicio = NULL;
            this->size = 0;
        }

        void encolar(int id, std::string nombre){
            
            Nodo * nuevoNodo =  new Nodo(id, nombre);
            
            if(this->inicio == NULL){
                this->inicio = nuevoNodo;
            }else{
                Nodo * temp = this->inicio;

                // ULTIMO NODO
                while(temp->siguiente != NULL){
                    temp = temp->siguiente;
                }

                temp->siguiente = nuevoNodo;
                // AGREGAN EL TAMAÑO
                this->size ++;
            }

        }
        
        Nodo* desencolar(){
            if(this->inicio == NULL){
                return NULL;
            }else{
                Nodo * temp = this->inicio;
                this->inicio = this->inicio->siguiente;
                this->size --;
                return temp;
            }
        }

        void imprimir(){
            if(this->inicio != NULL){
                Nodo * temp = this->inicio;
                while(temp != NULL){
                    std::cout << temp->getNombre() << " -> ";
                    temp = temp->siguiente;
                }
                std::cout << " NULL " << std::endl;
            }else{
                std::cout << " VACIO " << std::endl;
            }
        }

        int length(){
            return this->size;
        }
};


int main(){

    Cola * cola = new Cola();

    cola->encolar(1, "Nombre 1");
    cola->encolar(2, "Nombre 2");
    cola->encolar(3, "Nombre 3");
    cola->encolar(4, "Nombre 4");
    cola->encolar(5, "Nombre 5");

    cola->imprimir();

    Nodo * res1 = cola->desencolar();
    std::cout << "Resultado de Desencolar: \t" << res1->getNombre() << std::endl;

    cola->imprimir();

    cola->encolar(5, "Nombre 6");

    cola->imprimir();

    Nodo * res2 = cola->desencolar();
    std::cout << "Resultado de Desencolar: \t" << res2->getNombre() << std::endl;

    cola->imprimir();
};
