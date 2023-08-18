#include <iostream>
#include <string>

using namespace std;
using std::string;

// CLASE NODO
class Nodo{
    private:
        int id;
        int x;
        int y;
        std::string nombre;
    public:
        // APUNTADOR AL SIGUIENTE
        Nodo * arriba;
        Nodo * abajo;
        Nodo * izquierda;
        Nodo * derecha;

        //CONSTRUCTOR DE LA CLASE NODO DE FILA Y COLUMNA
        Nodo(int id){
            this->id = id;
            this->nombre = "";
            this->arriba = NULL;
            this->abajo = NULL;
            this->izquierda = NULL;
            this->derecha = NULL;
        }

        //Contructor de los nodos de la matriz
        Nodo(std::string nombre, int x, int y){
            this->nombre = nombre;
            this->x = x;
            this->y = y;
            this->arriba = NULL;
            this->abajo = NULL;
            this->izquierda = NULL;
            this->derecha = NULL;
        }
        
        // GETTESR Y SETTERS
        int getId() { return this->id; }
        std::string getNombre() { return this->nombre; }

        void setId(int id) { this->id = id; }
        void setNombre(std::string nombre) { this->nombre = nombre; }

        int getX() { return this->x; }
        int getY() { return this->y; }
};



class MatrizDispersa{

    private:
        // NODO INICIAL
        Nodo* inicio;

    public:
        // CONSTRUCTOR DE LA CLASE
        MatrizDispersa(){
            this->inicio =  new Nodo(0);
        }
        
        // Donde x es el numero de fila
        // Donde y es el numero de columna
        void agregar(int x, int y){
            // AGREGAR FILAS
            agregarFila(x);
            // AGREGAR COLUMNAS
            agregarColumna(y);

            // CONSTRUCTOR DE SOLO STRING
            Nodo * nuevoNodo = new Nodo("( " +std::to_string(x) + ", " + std::to_string(y)+ " )", x, y);

            agregarNodoX(nuevoNodo, x, y);
            agregarNodoY(nuevoNodo, x, y);

        }

        void printX(){
            std::cout << "EJE X-----------------------------------" << std::endl;
            Nodo * temp = NULL;
            try{ temp = this->inicio->abajo; } catch(const std::exception&) { temp = NULL; }
            // Nodo * iterador = NULL;
            while(temp != NULL ){
                std::cout << temp->getId() << ": ";
                if(temp->derecha != NULL){
                    Nodo * iterador = temp->derecha;
                    while(iterador != NULL){
                        std::cout << iterador->getNombre() << ", ";
                        iterador = iterador->derecha;
                    }
                    std::cout << "" << std::endl;
                }
                temp = temp->abajo;
            }
        }

        void printY(){
            std::cout << "EJE Y-----------------------------------" << std::endl;
            Nodo * temp = NULL;
            try{ temp = this->inicio->derecha; } catch(const std::exception&) { temp = NULL; }
            // Nodo * iterador = NULL;
            while(temp != NULL ){
                std::cout << temp->getId() << ": ";
                if(temp->abajo != NULL){
                    Nodo * iterador = temp->abajo;
                    while(iterador != NULL){
                        std::cout << iterador->getNombre() << ", ";
                        iterador = iterador->abajo;
                    }
                    std::cout << "" << std::endl;
                }
                temp = temp->derecha;
            }
        }

        void grafica(){
            std::string codigoDOT = "graph [nodesep=\"0.8\", ranksep=\"0.6\"]; \n";
            codigoDOT += "M0[ label = \"Inicio\" width = 1.5 shape = \"square\" style = \"filled\" fillcolor =\"slateblue\" group=\"0\"]; \n";
            // CODIGO DE LAS CABECERAS
            codigoDOT += graficaCabeceras();
            // CODIGO DE LOS NODOS
            codigoDOT += graficaNodos();
            
            std::cout << codigoDOT << std::endl;
        }


    // METODOS PRIVADOS PARA QUE NO MOLESTEN
    private:
        //Crear los nodos que identifiquen la fila
        void agregarFila(int x){
            Nodo * actual = new Nodo(x);

            if(this->inicio->abajo == NULL){
                this->inicio->abajo = actual;
                actual->arriba = this->inicio;
            }else{
                Nodo * temp = this->inicio;
                
                while(temp->abajo != NULL && temp->abajo->getId() < x){
                    temp = temp->abajo;
                }
                //CASO DE QUE FUERA ULTIMA FILA
                if(temp->abajo == NULL){
                    temp->abajo = actual;
                    actual->arriba = temp;
                }else if(temp->abajo != NULL &&  temp->abajo->getId() != x){
                    // CASO DE QUE FUERA ENTRE DOS NODOS
                    Nodo * r = temp->abajo;
                    temp->abajo = actual;
                    actual->arriba = temp;
                    actual->abajo = r;
                    r->arriba = actual;
                }

            }

        }
        //Crear los nodos que identifiquen la columna
        void agregarColumna(int y){
            Nodo * actual = new Nodo(y);
            if(this->inicio->derecha == NULL){
                this->inicio->derecha = actual;
                actual->izquierda = this->inicio;
            }else{
                Nodo * temp = this->inicio;
                
                while(temp->derecha != NULL && temp->derecha->getId() < y){
                    temp = temp->derecha;
                }
                //CASO DE QUE FUERA ULTIMA FILA
                if(temp->derecha == NULL){
                    temp->derecha = actual;
                    actual->izquierda = temp;
                }else if(temp->derecha != NULL &&  temp->derecha->getId() != y){
                    // CASO DE QUE FUERA ENTRE DOS NODOS
                    Nodo * r = temp->derecha;
                    temp->derecha = actual;
                    actual->izquierda = temp;
                    actual->derecha = r;
                    r->izquierda = actual;
                }

            }
        }
        //Agregar Nodo
        void agregarNodoX(Nodo * nodo, int x, int y){
            Nodo * fila = this->inicio;
            
            // OBETENER EL NODO DE LA FILA
            while(fila->getId() != x){
                fila = fila->abajo;
            }
            // OBTNER 
            if(fila->derecha == NULL){
                fila->derecha = nodo;
                nodo->izquierda = fila;
            }else{
                // INSERCION ORDENADA
                try {
                    while(fila->derecha != NULL && fila->derecha->getY() < y){
                        fila = fila->derecha;
                    }

                    if(fila->derecha == NULL){
                        fila->derecha = nodo;
                        nodo->izquierda = fila;
                    }else if(fila->derecha != NULL &&  fila->derecha->getY() != y){
                        Nodo * r = fila->derecha;
                        fila->derecha = nodo;
                        nodo->izquierda = fila;
                        nodo->derecha = r;
                        r->izquierda = nodo;
                    }

                } catch(const std::exception& e){
                    std::cerr << e.what() << '\n';
                }
            }   
        }
        // AGREGAR NODO
        void agregarNodoY(Nodo * nodo, int x, int y){
            Nodo * colum = this->inicio;
            
            // OBETENER EL NODO DE LA FILA
            while(colum->getId() != y){
                colum = colum->derecha;
            }
            // OBTNER 
            if(colum->abajo == NULL){
                colum->abajo = nodo;
                nodo->arriba = colum;
            }else{
                // INSERCION ORDENADA
                try {
                    while(colum->abajo != NULL && colum->abajo->getX() < x){
                        colum = colum->abajo;
                    }

                    if(colum->abajo == NULL){
                        colum->abajo = nodo;
                        nodo->arriba = colum;
                    }else if(colum->abajo != NULL &&  colum->abajo->getX() != x){
                        Nodo * r = colum->abajo;
                        colum->abajo = nodo;
                        nodo->arriba = colum;
                        nodo->abajo = r;
                        r->arriba = nodo;
                    }

                } catch(const std::exception& e){
                    std::cerr << e.what() << '\n';
                }
            }   
        }

        std::string graficaCabeceras(){
            std::string conexiones = "M0 ->";
            std::string nodos = "";
            std::string rank = "{rank = same; M0; ";

            Nodo * temp = NULL;
            // EJE X-----------------------------------------------------------------------
            try{ temp = this->inicio->abajo; } catch(const std::exception&) { temp = NULL; }
            while(temp != NULL ){            
                nodos += "X" + std::to_string(temp->getId()) + "[label=\"X"+std::to_string(temp->getId())+"\" width = 1.5 shape =\"square\" style=\"filled\" fillcolor=\"skyblue3\" group=0];\n";
                if(temp->abajo != NULL){
                    conexiones += "X" + std::to_string(temp->getId()) + " -> ";
                }else{
                    conexiones += "X" + std::to_string(temp->getId());
                }
                temp = temp->abajo;
            }
            conexiones += ";\n M0 -> ";
            // EJE Y-----------------------------------------------------------------------

            try{ temp = this->inicio->derecha; } catch(const std::exception&) { temp = NULL; }
            // Nodo * iterador = NULL;
            while(temp != NULL ){
                nodos += "Y" + std::to_string(temp->getId()) + "[label=\"Y"+std::to_string(temp->getId())+"\" width = 1.5 shape =\"square\" style=\"filled\" fillcolor=\"skyblue3\" group=\""+std::to_string(temp->getId())+"\"];\n";
                rank += "Y" + std::to_string(temp->getId()) + ";";
                if(temp->derecha != NULL){
                    conexiones += "Y" + std::to_string(temp->getId()) + " -> ";
                }else{
                    conexiones += "Y" + std::to_string(temp->getId());
                }
                temp = temp->derecha;
            }
            rank += "};";
            conexiones += "[dir=both]; \n";

            return nodos +"\n"+ conexiones +"\n"+ rank +"\n";
        }

        std::string graficaNodos(){
            std::string conexiones = "";
            std::string nodos = "";
            std::string rank = "";
            
            Nodo * temp = NULL;
            // EJE X-----------------------------------------------------------------------
            try{ temp = this->inicio->abajo; } catch(const std::exception&) { temp = NULL; }
            // Nodo * iterador = NULL;
            while(temp != NULL ){            
                if(temp->derecha != NULL){
                    // CONEXION CON LA CABECERA
                    conexiones += "X"+std::to_string(temp->getId())+" -> ";
                    rank += "{rank=same; X"+std::to_string(temp->getId())+"; ";

                    Nodo * iterador = temp->derecha;
                    while(iterador != NULL){
                        // NOMBRE DEL NODO
                        nodos += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY());
                        rank += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY())+";";
                        // DATOS DEL NODO
                        nodos += "[label=\""+iterador->getNombre()+"\" width=1.5 shape=\"square\" style=\"filled\" fillcolor=\"slategray1\" group=\""+to_string(iterador->getY())+"\"];\n";
                        // CONEXIONES DE NODO                        
                        if(iterador->derecha != NULL){
                            conexiones += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY()) + " -> ";
                        }else{
                            conexiones += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY());
                        }

                        iterador = iterador->derecha;
                    }
                    rank += "};\n";
                    conexiones += "[dir=both]; \n";
                }
                temp = temp->abajo;
            }


            // EJE Y-----------------------------------------------------------------------
            try{ temp = this->inicio->derecha; } catch(const std::exception&) { temp = NULL; }
            // Nodo * iterador = NULL;
            while(temp != NULL ){
                if(temp->abajo != NULL){
                    conexiones += "Y"+std::to_string(temp->getId())+" -> ";
                    Nodo * iterador = temp->abajo;

                    while(iterador != NULL){
                        nodos += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY());
                        // DATOS DEL NODO
                        nodos += "[label=\""+iterador->getNombre()+"\" width=1.5 shape=\"square\" style=\"filled\" fillcolor=\"slategray1\" group=\""+to_string(iterador->getY())+"\"];\n";
                        // CONEXIONES DE NODO                        
                        if(iterador->abajo != NULL){
                            conexiones += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY()) + " -> ";
                        }else{
                            conexiones += "S"+to_string(iterador->getX())+"_"+to_string(iterador->getY());
                        }
                        iterador = iterador->abajo;
                    }

                    conexiones += "[dir=both];\n";
                }
                temp = temp->derecha;
            }

            return nodos +"\n"+ conexiones +"\n"+ rank +"\n";
        }
};


int main(){
    
    MatrizDispersa * matriz =  new MatrizDispersa();

    matriz->agregar(4,5);
    matriz->agregar(2,1);
    matriz->agregar(1,3);
    matriz->agregar(2,6);
    matriz->agregar(3,5);
    matriz->agregar(4,4);
    matriz->agregar(1,4);
    matriz->agregar(2,3);
    matriz->agregar(2,5);
    matriz->agregar(4,3);

    // matriz->printX();    
    // matriz->printY();
    matriz->grafica();

};


