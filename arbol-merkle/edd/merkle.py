from datetime import datetime
import hashlib

# INFORMACION QUE DEBE DE TENER EL NODO
# ● Fecha y hora de Pago
# ● ID de la billetera del empleado a cargo
# ● Monto Pagado
# ● Proyecto Asociado
class Transaccion:
    def __init__(self, id_cartera: str, monto_pagado: str, id_proyecto: str):
        self.fecha_hora = datetime.now()  # marca de tiempo
        self.id_cartera = id_cartera
        self.monto_pagado = monto_pagado
        self.id_proyecto = id_proyecto
        self.hash = self.crear_hash()
        self.izquierda = None
        self.derecha = None

    def crear_hash(self):
        # SHA3(“15-10-23::14:02:23” + “DC56RT89” + “152.50” + “PY-100”)
        cadena =""
        cadena += self.fecha_hora.strftime("%d/%m/%Y::%H:%M:%S")
        cadena += self.id_cartera
        cadena += self.monto_pagado
        cadena += self.id_proyecto
        return hashlib.sha3_256(cadena.encode()).hexdigest()

# CLASE DE ARBOL
class Merkle:
    # CONSTRUCTOR
    def __init__(self):
        self.raiz = None
    # METODO INSERTAR

    def insertar(self, id_cartera: str, monto_pagado: str, id_proyecto: str):
        nuevo_nodo = Transaccion(id_cartera, monto_pagado, id_proyecto)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            # COLA PARA LA INSERCION
            cola = [self.raiz]
            while cola:
                actual = cola.pop(0)

                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                    break
                elif actual.derecha is None:
                    actual.derecha = nuevo_nodo
                    break
                else:
                    cola.append(actual.izquierda)
                    cola.append(actual.derecha)
        self.actualizar_hashes()

    def actualizar_hashes(self):
        nodo = [self.raiz]
        while nodo:
            actual = nodo.pop(0)
            if actual.izquierda:
                nodo.append(actual.izquierda)
            if actual.derecha:
                nodo.append(actual.derecha)
            # ASIGNACIONES
            hash_izquierda = actual.izquierda.hash if actual.izquierda else ""
            hash_derecha = actual.derecha.hash if actual.derecha else ""
            # JUNTAR HASHES
            # concat_hash = ""
            # if hash_izquierda:
            #     concat_hash += hash_izquierda
            # if hash_derecha:
            #     concat_hash += hash_derecha
            actual.hash = hashlib.sha3_256(((hash_izquierda + hash_derecha)).encode('UTF-8')).hexdigest()
    
    def imprimir(self):
        self._imprimit_rec(self.raiz, 0)
    
    def _imprimit_rec(self, nodo:Transaccion, nivel:int):
        if nodo is not None:
            self._imprimit_rec(nodo.derecha, nivel + 1)
            print(" " * nivel + f"{nodo.id_cartera} ({nodo.hash})")
            self._imprimit_rec(nodo.izquierda, nivel + 1)
