import math

class Empleado:
    # CONSTRUCTOR DEL NODO
    def __init__(self, codigo, nombre, contrasenia):
        self.codigo = codigo
        self.nombre = nombre
        self.contrasenia = contrasenia
    # IMPRIMR NODO
    def __str__(self):
        return f"ID: {self.codigo} - Nombre: {self.nombre} - Password: {self.contrasenia}"

class TablaHash:
    # CONSTRUCTOR DE CLASE
    def __init__(self):
        self.tabla = [None] * 5    # ASIGNAR 5 ESPACIOS
        self.capacidad_actual = 5  # -> 8 -> 13 -> 21 
        self.espacios_usados = 0
    # IMPRIMIR TABLA HASH
    def __str__(self):
        str = ""
        for i in range(self.capacidad_actual):
            if self.tabla[i] != None:
                str += f"{i}:\t{self.tabla[i]}\n"
            else:
                str += f"{i}:\tEmpty :p\n"
        return str
    # INSERTAR NUEVO NODO
    def insertar(self, codigo:str, nodo:Empleado):
        indice = self.calcular_indice(codigo)       # GENERAR INDICE
        if indice < self.capacidad_actual:
            try:
                if self.tabla[indice] is None:      # INSERCION NORMAL
                    self.tabla[indice] = nodo
                    self.espacios_usados += 1
                else:
                    indice = self.recalcular(codigo) # RECALCULAR INDICE 
                    self.tabla[indice] = nodo
                    self.espacios_usados += 1
                self.agrandar_tabla() # AGRADAR TABLA, SI FERA NECESARIO
            except Exception as e:
                print("Descripcion: ", e)
                print("Error en insercion", codigo, indice)
    # CALCULAR INDICE
    def calcular_indice(self, codigo:str):
        suma_acii = 0
        # SUMA DE ASCII
        for char in codigo:
            suma_acii += ord(char)
        # MÓDULO POR CAPACIDAD 
        posicion = suma_acii % self.capacidad_actual
        return posicion
    # RECALCULAR INDICE
    def recalcular(self, codigo:str):
        contador = 1
        # OBTENER NUEVO INCIDE
        nuevo_indice = self.calcular_indice(codigo) + int(math.pow(contador, 2))
        # VERIFICAR QUE NO ESTÉ OCUPADO
        while self.tabla[nuevo_indice] is not None:
            contador += 1
            nuevo_indice = nuevo_indice + int(math.pow(contador, 2))
            nuevo_indice = self.verificar_indice(nuevo_indice) # EVITAR QUE SE ENCICLE :P
        return nuevo_indice
    # VERIFICAR QUE EL INDICE SEA MENOR A LA CAPACIDAD
    def verificar_indice(self, indice:int):
        posicion = indice
        if indice < self.capacidad_actual:
            posicion = indice
        else:
            posicion = indice - self.capacidad_actual
            posicion = self.verificar_indice(posicion)
        return posicion
    # REORGANIZAR TABLA HASH POR UTILIZACION
    def agrandar_tabla(self):
        utilizacion = int(self.capacidad_actual * 0.7) # PORCENTAJE DE UTILIZACION
        if self.espacios_usados > utilizacion:
            self.capacidad_actual = self.siguiente_fibonacci(self.capacidad_actual) # SIGUIENTE EN LA SUCESIÓN DE FIBONACCI
            #print("Nueva Capacidad", self.capacidad_actual, "Ocupados", self.espacios_usados, "Max Permitido:", utilizacion)
            self.espacios_usados = 0
            tabla_vieja = self.tabla # ARRAY ANTERIOR
            self.tabla = [None] * self.capacidad_actual # CREAR NUEVO ARRAY CON LA NUEVO TAMAÑO
            for empleado in tabla_vieja: # REINCERTAR EMPLEADOS
                if(empleado is not None):
                    self.insertar(empleado.codigo, empleado)
    # OBTENER SIGUIENTE FIBONACCI
    def siguiente_fibonacci(self, n:int):
        a, b = 0, 1
        while True:
            a, b = b, b + a
            if b > n:
                return b 
    # METODO BUSCAR TABLA HASH
    def buscar(self, codigo:str):
        indice =  self.calcular_indice(codigo)
        if indice < self.capacidad_actual:
            if(self.tabla[indice] is not None and self.tabla[indice].codigo == codigo):
                return self.tabla[indice]
            else:
                contador = 1
                nuevo_indice = indice + int(math.pow(contador, 2))
                # NUEVO INDICE NO PUEDE ITERAR MÁS QUE LA CAPACIDAD ACTUAL 
                try:
                    while self.tabla[nuevo_indice].codigo != codigo or contador > self.capacidad_actual:
                        contador += 1
                        nuevo_indice = nuevo_indice + int(math.pow(contador, 2))
                        nuevo_indice = self.verificar_indice(nuevo_indice) # EVITAR QUE SE ENCICLE :P
                    if(self.tabla[nuevo_indice] is not None and self.tabla[nuevo_indice].codigo == codigo):
                        return self.tabla[nuevo_indice]
                except:
                    print("Error en busqueda!")
        return None # por si no lo encuentra
            

tabla = TablaHash()
tabla.insertar("ADMIN-1", Empleado("ADMIN-1", "admin1", "admin1"))
tabla.insertar("ADMIN-2", Empleado("ADMIN-2", "admin2", "admin2"))
tabla.insertar("ADMIN-3", Empleado("ADMIN-3", "admin3", "admin3"))
tabla.insertar("ADMIN-4", Empleado("ADMIN-4", "admin4", "admin4"))
tabla.insertar("FDEV-1", Empleado("FDEV-1", "Front 1", "Front1"))
tabla.insertar("FDEV-2", Empleado("FDEV-2", "Front 2", "Front2"))
tabla.insertar("FDEV-3", Empleado("FDEV-3", "Front 3", "Front3"))
tabla.insertar("FDEV-4", Empleado("FDEV-4", "Front 4", "Front4"))
tabla.insertar("FDEV-5", Empleado("FDEV-5", "Front 5", "Front5"))
tabla.insertar("FDEV-6", Empleado("FDEV-6", "Front 6", "Front6"))
tabla.insertar("FDEV-7", Empleado("FDEV-7", "Front 7", "Front7"))
tabla.insertar("FDEV-8", Empleado("FDEV-8", "Front 8", "Front8"))
tabla.insertar("FDEV-9", Empleado("FDEV-9", "Front 9", "Front9"))
tabla.insertar("BDEV-1", Empleado("BDEV-1", "Back 1", "Back 1"))
tabla.insertar("BDEV-2", Empleado("BDEV-2", "Back 2", "Back 2"))
tabla.insertar("BDEV-3", Empleado("BDEV-3", "Back 3", "Back 3"))
tabla.insertar("BDEV-4", Empleado("BDEV-4", "Back 4", "Back 4"))
tabla.insertar("BDEV-5", Empleado("BDEV-5", "Back 5", "Back 5"))
tabla.insertar("BDEV-6", Empleado("BDEV-6", "Back 6", "Back 6"))
tabla.insertar("BDEV-7", Empleado("BDEV-7", "Back 7", "Back 7"))
tabla.insertar("BDEV-8", Empleado("BDEV-8", "Back 8", "Back 8"))
tabla.insertar("BDEV-9", Empleado("BDEV-9", "Back 9", "Back 9"))
tabla.insertar("BDEV-10", Empleado("BDEV-10", "Back 10", "Back 10"))
tabla.insertar("QA-1", Empleado("QA-1", "QA1", "QA1"))
tabla.insertar("QA-2", Empleado("QA-2", "QA2", "QA2"))
tabla.insertar("QA-3", Empleado("QA-3", "QA3", "QA3"))
tabla.insertar("QA-4", Empleado("QA-4", "QA4", "QA4"))
tabla.insertar("QA-5", Empleado("QA-5", "QA5", "QA5"))
tabla.insertar("QA-6", Empleado("QA-6", "QA6", "QA6"))

print(tabla.buscar("ADMIN-5"))
# print(tabla)
# print("TAMANIO:", tabla.espacios_usados)