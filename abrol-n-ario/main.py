
class Nodo:
    # constructor de la clase
    def __init__(self, nombre_carpeta:str):
        self.nombre_carpeta = nombre_carpeta
        self.hijos = [] # array de hijos
        self.id_carpeta = None
    
    def __str__(self):
        string = ""
        for hijo in self.hijos:
            string += "\t-"+ hijo.nombre_carpeta + "\n"
        return string



class Arbol:
    def __init__(self):
        self.raiz = Nodo('EDD/')
        self.raiz.id_carpeta = 0
        self.size = 0

    def insertar(self, nombre_carpeta:str, ruta_padre:str):
        nuevo_nodo = Nodo(nombre_carpeta)
        padre = self.buscar_carpeta(ruta_padre)
        if(padre):
            self.size += 1
            nuevo_nodo.id_carpeta = self.size
            padre.hijos.append(nuevo_nodo)
            # nuevo_nodo.hijos.append(nuevo_nodo)
        else:
            print("Error al ingresar nodo")

    def buscar_carpeta(self, ruta:str):
        # ruta sea igual a la raiz
        if ruta == self.raiz.nombre_carpeta:
            return self.raiz
        else:
            temp = self.raiz
            carpetas_ruta = ruta.split('/')
            while(len(carpetas_ruta) > 0):
                carpeta_temp  = carpetas_ruta.pop(0)
                # busqueda dentro los hijos
                for hijo in temp.hijos:
                    if(hijo.nombre_carpeta == carpeta_temp):
                        temp = hijo
                # pasar al siguiente nodo
            return temp # encontro la carpeta
        
    def __str__(self): 
        cola = []
        cola.append(self.raiz)
        cadena = ""
        while len(cola) != 0:
            for i in range(0, len(cola)):
                temp = cola.pop(0)
                cadena += str(temp.nombre_carpeta) + "\n"
                cadena += str(temp) + "\n"
                for hijo in temp.hijos: # agregar hijos a la cola
                    cola.append(hijo)
        return cadena

    def graficar(self):
        cola = []
        cola.append(self.raiz)
        nodos = "" # declarar nodos en graphviz
        conexiones = "" # conexiones entre los nodos
        while len(cola) != 0:
            for i in range(0, len(cola)):
                temp = cola.pop(0)
                nodos += f"S_{temp.id_carpeta}[label=\"{temp.nombre_carpeta}\"];\n" # nodo padre
                for hijo in temp.hijos: # agregar hijos a la cola
                    nodos += f"S_{hijo.id_carpeta}[label=\"{hijo.nombre_carpeta}\"];\n" # nodos hijos
                    conexiones += f"S_{temp.id_carpeta} -> S_{hijo.id_carpeta};\n"
                    cola.append(hijo)
        return nodos + conexiones


arbol = Arbol()
arbol.insertar("Documentos", "EDD/")
arbol.insertar("Imagenes", "EDD/")
arbol.insertar("Documentos2", "EDD/")
arbol.insertar("Documentos3", "EDD/")
arbol.insertar("Documentos4", "EDD/")
arbol.insertar("Documentos5", "EDD/")
arbol.insertar("Documentos6", "EDD/")
arbol.insertar("Repos", "EDD/Documentos/")
arbol.insertar("Word", "EDD/Documentos/")
arbol.insertar("Excel", "EDD/Documentos/")
arbol.insertar("Power Point", "EDD/Documentos/")
arbol.insertar("Publisher", "EDD/Documentos/")
arbol.insertar("Visio", "EDD/Documentos/")
arbol.insertar("FotosCasamiento", "EDD/Imagenes/")
arbol.insertar("FotosXXX", "EDD/Imagenes/")
arbol.insertar("Raros", "EDD/Imagenes/FotosXXX")

# print(arbol)

print(arbol.graficar())
