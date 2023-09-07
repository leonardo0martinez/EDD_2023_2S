
# CLASE NODO
class Nodo:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, id:int, nombre:str):
        self.id = id
        self.nombre = nombre
        self.altura = 1
        self.izquierda = None
        self.derecha = None

# ESTRUCTURA DEL ARBOL
class ArbolAVL:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self):
        self.raiz = None
    
    # METODOS PARA ALV
    def altura(self, nodo:Nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    def factor_de_equilibrio(self, nodo:Nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha) # > 2 o < -2
    # -----------------------------------------------------------

    # ROTACIONES DEL AVL
    def rotacion_derecha(self, y:Nodo):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y 
        y.izquierda = T2

        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))

        return x

    def rotacion_izquierda(self, x:Nodo):
        y = x.derecha
        T2 = y.izquierda
        
        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        
        return y
    # -----------------------------------------------------------

    def insertar(self, id:int, nombre:str):
        #CREAR EL NUEVO NODO
        nuevo_nodo = Nodo(id, nombre)
        self.raiz = self._recursivo(self.raiz, nuevo_nodo)

    def _recursivo(self, raiz:Nodo, nuevo_nodo:Nodo):
        if raiz is None:
            return nuevo_nodo
        
        # print(nuevo_nodo.id , raiz.id)
        if nuevo_nodo.id < raiz.id:
            raiz.izquierda = self._recursivo(raiz.izquierda, nuevo_nodo)
        else:
            raiz.derecha = self._recursivo(raiz.derecha, nuevo_nodo)
        
        # CAMBIAR ALTURA Y FACTOR DE EQUILIBRIO
        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.factor_de_equilibrio(raiz)

        # Rotaciones para equilibrar el árbol
        if balance > 1:
            if nuevo_nodo.id < raiz.izquierda.id:
                return self.rotacion_derecha(raiz)
            else:
                raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
                return self.rotacion_derecha(raiz)

        if balance < -1:
            if nuevo_nodo.id > raiz.derecha.id:
                return self.rotacion_izquierda(raiz)
            else:
                raiz.derecha = self.rotacion_derecha(raiz.derecha)
                return self.rotacion_izquierda(raiz)

        return raiz



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
        self._nodos += "S"+str(actual.id)+"[label=\"id:"+str(actual.id)+"\\n nombre:"+actual.nombre+"\\n altura:"+str(actual.altura)+"\"];\n"
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
 
            
    


arbolito = ArbolAVL()
arbolito.insertar(1, "prueba 1")
arbolito.insertar(2, "prueba 2")
arbolito.insertar(3, "prueba 3")
arbolito.insertar(4, "prueba 4")
arbolito.insertar(5, "prueba 5")
# arbolito.insertar(6, "prueba 8")
# arbolito.insertar(7, "prueba 7")

print(arbolito.grafica())