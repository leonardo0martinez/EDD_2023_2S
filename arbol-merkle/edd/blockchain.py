from datetime import datetime
from edd.merkle import Transaccion
import hashlib # generamos el hash
# CADA UNO DE LOS BLOQUES
class Block:
    def __init__(self, index:int, data:Transaccion, hash_anteriror="", hash=""):
        self.index = index # buscar, puede ser un id
        self.timestamp = datetime.now() # marca de tiempo
        self.hash_anterior = hash_anteriror
        self.data = data.hash # HASH DE SU RAIZ
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
                cadena += f'I:{temp.index} T:{temp.timestamp.strftime("%d/%m/%Y %H:%M:%S")} D:{temp.data[:10]} H:{temp.hash} HA:{temp.hash_anterior}\n'
                temp = temp.siguiente
        return cadena
    
    def insertar(self, transaccion: Transaccion):
        nuevo_nodo = Block(self.size, transaccion)
        
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
        cadena  = f'{nodo.index}{nodo.timestamp}{nodo.data}'
        encriptar.update(cadena.encode('utf-8'))
        return encriptar.hexdigest()

    def graficar(self):
        pass