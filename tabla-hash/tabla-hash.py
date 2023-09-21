import math
# CLASE NODO DE EMPLEADO ----------------------------------------------------------------------------
class Empleado:
    def __init__(self, codigo:str, nombre:str, password:str):
        self.codigo = codigo
        self.nombre = nombre
        self.password = password
    def __str__(self):
        return  f"ID: {self.codigo}\t\tNombre:{self.nombre}\t\tPassword: {self.password}"

## TABLA HASH ----------------------------------------------------------------------------
class TablaHash:
    # CONSTRUCTOR -------------------------------------------------------------------------------------
    def __init__(self):
        self.tabla = [None] * 5 # ASIGNAR 5 ESPACIOS CON NONE
        self.capacidad = 5 # -> 8 -> 13 -> 21 
        self.espacios_usados = 0
    # IMPRIMIR TABLA HASH-----------------------------------------------------------------------------
    def __str__(self):
        str = ""
        for i in range(self.capacidad):
            if self.tabla[i] != None:
                str += f"{i}:\t{self.tabla[i]}\n"
            else:
                str += f"{i}:\tEmpty :p\n"
        return str
    # INSERTAR NUEVO NODO ------------------------------------------------------------------------------
    def insertar(self, codigo:str, nuevo_nodo:Empleado):
        # OBTENER INDICE DE FORMULA
        indice = self.calcular_indice(codigo)
        if indice < self.capacidad:
            if self.tabla[indice] is None: # INSERCIÓN SI EL ESPACIO ESTÁ VACÍO
                print("INSERCION", indice, nuevo_nodo.nombre)
                self.tabla[indice] = nuevo_nodo
                self.espacios_usados = self.espacios_usados + 1
            else: # INSERCIÓN SI HAY UNA COLISÓN (POSICIÓN LLENA)
                contador = 1 # CONTAR LA CANTIDAD DE COLISIONES
                indice =  self.recalcular_indice(codigo, contador)
                while(self.tabla[indice] is not None):
                    contador += 1  
                    indice = self.recalcular_indice(codigo, contador)
                print("INSERCION", indice, nuevo_nodo.nombre)
                self.tabla[indice] = nuevo_nodo
                self.espacios_usados += 1
            # VERIFICAR UTILIZACION
                self.agrandar_tabla() 
    # CALCULAR EL INDICE DE INSERCION -----------------------------------------------------------------
    def calcular_indice(self, codigo=str):
        suma = 0
        # SUMA DE ASCII
        for char in codigo:
            suma += ord(char)
        # MÓDULO POR CAPACIDAD 
        posicion = suma % self.capacidad
        return posicion    
    # RECALCULAR INDICE --------------------------------------------------------------------------------
    def recalcular_indice(self, codigo:str, saltos:int):
        nuevo_indice =  self.calcular_indice(codigo) + pow(saltos, 2)
        while(nuevo_indice > self.capacidad - 1): # NO QUITAR EL MENOS 1 0_0
            nuevo_indice -= self.capacidad
        return nuevo_indice
    # AGRANDAR TABLA ------------------------------------------------------------------------------------
    def agrandar_tabla(self):
        # PORCENTAJE DE UTILIZACION
        utilizacion = math.floor(self.capacidad * 0.7)
        if self.espacios_usados > utilizacion:
            # SIGUIENTE EN LA SUCESIÓN DE FIBONACCI
            self.capacidad = self.siguiente_fibonacci(self.capacidad)
            print("NUEVA CAPACIDAD", self.capacidad, "ESPACIOS USADOS", self.espacios_usados, "% ", utilizacion)
            self.espacios_usados = 0
            # ARRAY ANTERIOR
            tabla_vieja = self.tabla
            # CREAR NUEVO ARRAY CON LA NUEVO TAMAÑO
            self.tabla = [None] * self.capacidad
            # REINCERTAR EMPLEADOS
            for empleado in tabla_vieja:
                if(empleado is not None):
                    self.insertar(empleado.codigo, empleado)                    
    # SIGUIENTE EN LA SUCESION DE FIBONACCI --------------------------------------------------------------
    def siguiente_fibonacci(self, n:int):
        a, b = 0, 1
        while True:
            a, b = b, b + a
            if b > n:
                return b
    # BUSCAR EN TABLA HASH -------------------------------------------------------------------------------
    def buscar(self, codigo:str):
        indice =  self.calcular_indice(codigo)
        try:
            if(self.tabla[indice] is not None and self.tabla[indice].codigo == codigo):
                return self.tabla[indice]
        except:
            contador = 1
            contador = 1 # CONTAR LA CANTIDAD DE COLISIONES
            indice =  self.recalcular_indice(codigo, contador)
            while(self.tabla[indice] is not None):
                contador += 1  
                indice = self.recalcular_indice(codigo, contador)
                if(self.tabla[indice] is not None and self.tabla[indice].codigo == codigo):
                    return self.tabla[indice]
            
            
       
# if self.espacios_usados > math.floor(self.capacidad * 0.7):
tablahash = TablaHash()
# for i in range(0,10):
#     tablahash.insertar("admin-1-"+str(i), Empleado("admin-1-"+str(i), "Admin"+str(i), "12345"))
#     tablahash.insertar("front-2-"+str(i), Empleado("front-2-"+str(i), "Frontend"+str(i), "12345"))
#     tablahash.insertar("back-3-"+str(i), Empleado("back-3-"+str(i), "Backend"+str(i), "12345"))
#     tablahash.insertar("qa-4-"+str(i), Empleado("qa-4-"+str(i), "QualityAssurance"+str(i), "12345"))
# print(tablahash.buscar('admin-1-1'))
tablahash.insertar("ADMINISTRADOR", Empleado("ADMINISTRADOR", "ADMIN", "12345"))
tablahash.insertar("EMPLEADO-FRONT", Empleado("EMPLEADO-FRONT", "FRON", "12345"))
tablahash.insertar("EMPLEADO-BACK", Empleado("EMPLEADO-BACK", "BACK", "12345"))
print(tablahash)
tablahash.insertar("EMPLEADO-QA", Empleado("EMPLEADO-QA", "QA", "12345"))
tablahash.insertar("EMPLEADO-FRON-2", Empleado("EMPLEADO-FRONT-2", "FRONT2", "12345"))
print(tablahash)

