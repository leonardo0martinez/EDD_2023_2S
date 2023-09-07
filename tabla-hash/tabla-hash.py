
class Nodo:
    def __init__(self, codigo:str, nombre:str, password:str):
        self.codigo = codigo
        self.nombre = nombre
        self.password = password
    

class TablaHash:
    # CONSTRUCTOR
    def __init__(self):
        self.tabla = [None] * 5
        self.capacidad = 5 # -> 8 -> 13 -> 21 
        self.espacios_usados = 0
    
    def calcular_indice(self, codigo=str):
        suma = 0
        # SUMA DE ASCII
        for char in codigo:
            suma += ascii(char)
        ## CALCULAR POSICION POR DIVISION  ** VERIFICAR **
        posicion = suma % self.capacidad
        return posicion
    
    # FORZAR QUE EL INDICE SEA MENOR A LA CAPACIDAD DEL ARRAY
    def nuevo_indice(self, indice_viejo:int):
        pos = 0
        if indice_viejo < self.capacidad:
            pos = indice_viejo
        else:
            ## POR SE TIENE UN INDEX MAYOR A LA CAPACIDAD DEL ARRAY
            pos = indice_viejo - self.capacidad
            pos = self.nuevo_indice(pos)
        return pos
    
    def recalcular_indice(self, indice_viejo:int, salto:int):
        nuevo_indice = self.nuevo_indice(indice_viejo + (salto^2))
        return nuevo_indice

    def insertar(self, codigo:str, nombre:str, password:str):
        # OBTENER EL INDICE DE LA FORMULA
        # FORMULA (SUMA DE ACII)
        indice = self.calcular_indice()
        nuevo_nodo = Nodo(codigo, nombre, password)

        if indice < self.capacidad:
            ## INSERCION CUANDO ESTA NULO EL ESPACIO
            if self.tabla[indice] is None:
                # SE AGREGA EN LA POSICION VACIA
                self.tabla[indice] = nuevo_nodo
                self.espacios_usados = self.espacios_usados + 1
            else:
                # CONTAR LA CANTIDAD DE SALTOS
                contador = 1 # LA CANTIDAD DE COLISIONES

                indice =  self.recalcular_indice(indice, contador)

                while(self.tabla[indice] is not None):
                    contador += 1  
                    indice = self.recalcular_indice(indice, contador)
                
                self.tabla[indice] = nuevo_nodo
                self.espacios_usados += 1
