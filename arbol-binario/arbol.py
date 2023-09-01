
# CLASE NODO
class Nodo:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, id:int, nombre:str):
        self.id = id
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None

# ESTRUCTURA DEL ARBOL
class Arbol:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self):
        self.raiz = None
    
    def insertar(self, id:int, nombre:str):
        #CREAR EL NUEVO NODO
        nuevo_nodo = Nodo(id, nombre)
        if(self.raiz == None):
            self.raiz = nuevo_nodo
        else:
            # METODO RECURSIVO
            self._recursivo(self.raiz, nuevo_nodo)

    def _recursivo(self, actual:Nodo, nuevo:Nodo):
        # VERIFICAMOS SI ES HIJO IZQUIERDO
        if(nuevo.id < actual.id):
            if(actual.izquierda is not None):
                self._recursivo(actual.izquierda, nuevo)
            else:
                actual.izquierda = nuevo
        elif(nuevo.id > actual.id):
            if(actual.derecha is not None):
                self._recursivo(actual.derecha, nuevo)
            else:
                actual.derecha = nuevo
        else:
            print("No se aceptan repetidos")

    _conexiones = ""
    _nodos = ""
    def grafica(self):
        self._conexiones =""
        self._nodos=""
        self._grafica_rec(self.raiz)
        return self._nodos + self._conexiones

    def _grafica_rec(self, actual:Nodo):
        # IZQUIERDA 
        if(actual.izquierda is not None):
            self._grafica_rec(actual.izquierda)
            self._conexiones += "S"+str(actual.id)+" -> "+"S"+str(actual.izquierda.id)+";\n"
        # RAIZ 
        self._nodos += "S"+str(actual.id)+"[label=\"id:"+str(actual.id)+"\\n nombre:"+actual.nombre+"\"];\n"
        # DERECHA 
        if(actual.derecha is not None):
            self._grafica_rec(actual.derecha)
            self._conexiones += "S"+str(actual.id)+" -> "+"S"+str(actual.derecha.id)+";\n"

    ## -------------------------------------------------
    ## RECORRIDO IN ORDER ------------------------------
    ## -------------------------------------------------
    def in_order(self):
        self._conexiones =""
        self._nodos=""
        self._in_order_rec(self.raiz)
        return self._nodos + self._conexiones 

    def _in_order_rec(self, actual:Nodo):
        # IZQUIERDA 
        if(actual.izquierda != None):
            self._in_order_rec(actual.izquierda)
            self._conexiones += " -> "
        # RAIZ 
        self._nodos += "S"+str(actual.id)+"[label=\"id:"+str(actual.id)+"\\n nombre:"+actual.nombre+"\"];\n"
        self._conexiones += "S"+str(actual.id)
        # DERECHA 
        if(actual.derecha != None):
            self._conexiones += " -> "
            self._in_order_rec(actual.derecha)
    
    ## -------------------------------------------------
    ## RECORRIDO PRE ORDER -----------------------------
    ## -------------------------------------------------
    def pre_order(self):
        self._conexiones =""
        self._nodos=""
        self._pre_order_rec(self.raiz)
        return self._nodos + self._conexiones 

    def _pre_order_rec(self, actual:Nodo):
        # RAIZ 
        self._nodos += "S"+str(actual.id)+"[label=\"id:"+str(actual.id)+"\\n nombre:"+actual.nombre+"\"];\n"
        self._conexiones += "S"+str(actual.id)
        # IZQUIERDA 
        if(actual.izquierda != None):
            self._conexiones += " -> "
            self._pre_order_rec(actual.izquierda)
        # DERECHA 
        if(actual.derecha != None):
            self._conexiones += " -> "
            self._pre_order_rec(actual.derecha)

    ## -------------------------------------------------
    ## RECORRIDO POST ORDER ----------------------------
    ## -------------------------------------------------
    def post_order(self):
        self._conexiones =""
        self._nodos=""
        self._post_order_rec(self.raiz)
        return self._nodos + self._conexiones 

    def _post_order_rec(self, actual:Nodo):
        # IZQUIERDA 
        if(actual.izquierda != None):
            self._post_order_rec(actual.izquierda)
            self._conexiones += " -> "
         # DERECHA 
        if(actual.derecha != None):
            self._post_order_rec(actual.derecha)
            self._conexiones += " -> "
        # RAIZ 
        self._nodos += "S"+str(actual.id)+"[label=\"id:"+str(actual.id)+"\\n nombre:"+actual.nombre+"\"];\n"
        self._conexiones += "S"+str(actual.id)
 
            
    


arbolito = Arbol()
arbolito.insertar(6, "prueba 6")
arbolito.insertar(2, "prueba 2")
arbolito.insertar(5, "prueba 5")
arbolito.insertar(9, "prueba 9")
arbolito.insertar(7, "prueba 7")
arbolito.insertar(1, "prueba 1")
arbolito.insertar(10, "prueba 10")

print(arbolito.post_order())