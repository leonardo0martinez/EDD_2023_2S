from datetime import datetime
import hashlib # generamos el hash
# CADA UNO DE LOS BLOQUES
class Block:
    def __init__(self, index:int, emisor, receptor, mensaje, hash_anteriror="", hash=""):
        self.index = index # buscar, puede ser un id
        self.timestamp = datetime.now() # marca de tiempo
        self.emisor = emisor
        self.receptor = receptor
        self.mensaje = mensaje
        self.hash_anterior = hash_anteriror
        self.hash = hash
        # APUNTADORES DEL NODO
        self.siguiente = None
        self.anterior = None

class BlockChain:
    def __init__(self):
        self.inicio = None
        self.ultimo = None
        self.size = 0
    def __str__(self):
        cadena =""
        if(self.inicio != None):
            temp = self.inicio
            while(temp != None):
                cadena += f'I:{temp.index} T:{temp.timestamp.strftime("%d/%m/%Y %H:%M:%S")} E:{temp.emisor} R:{temp.receptor} M:{temp.mensaje} H:{temp.hash} HA:{temp.hash_anterior}\n'
                temp = temp.siguiente
        return cadena
    
    def insertar(self, emisor, receptor, mensaje):
        nuevo_nodo = Block(self.size, emisor, receptor, mensaje)
        
        if self.inicio == None:
            # LISTA VACIA
            nuevo_nodo.hash_anterior = "000000"
            nuevo_nodo.hash = self.sha256(nuevo_nodo)
            # INSERTAR
            self.inicio = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.size += 1
        else:
            # HASH ANTERIOR
            nuevo_nodo.hash_anterior = self.ultimo.hash
            # CREAR EL HASH
            nuevo_nodo.hash = self.sha256(nuevo_nodo)
            # INSERTAR
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
            self.size += 1

    # GENERAR SHA256
    def sha256(self, nodo:Block):
        encriptar = hashlib.sha256()
        cadena  = f'{nodo.emisor} - {nodo.receptor} - {nodo.mensaje}'
        encriptar.update(cadena.encode('utf-8'))
        return encriptar.hexdigest()



cadena_de_bloques = BlockChain()

cadena_de_bloques.insertar("Leonardo", "Carlos", "Hola1")
cadena_de_bloques.insertar("Carlos", "Julio", "Hola2")
cadena_de_bloques.insertar("Julio", "Leonardo", "Hola3")
cadena_de_bloques.insertar("Leonardo", "Julio", "Hola4")
cadena_de_bloques.insertar("Julio", "Carlos", "Hola5")
cadena_de_bloques.insertar("Carlos", "Leonardo", "Hola6")
cadena_de_bloques.insertar("Leonardo", "Marcos", "Hola7")
cadena_de_bloques.insertar("Marcos", "Julio", "Hola8")

print(cadena_de_bloques)