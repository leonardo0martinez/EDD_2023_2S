from datetime import datetime
import hashlib
import math
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
    
    def label(self):
        return f"{str(self.fecha_hora)} \\n {self.id_cartera} \\n Q. {self.monto_pagado} \\n {self.id_proyecto}"
    # QUE ESTA PASANDO
    def __str__(self):
        return f"{str(self.fecha_hora)} - {self.id_cartera} -  {self.id_proyecto} - {self.hash}"
    

class ArbolMerkle:

    def __init__(self):
        self.raiz =  None
        self.transacciones = []
    
    def crear_arbol(self, transacciones=[]):
        # COPIA DE ARRAY
        self.transacciones = transacciones
        # INSERCION
        while len(transacciones) > 1:
            nuevos_nodos = [] # temporal
            for i in range(0, len(transacciones), 2): # VA IR EN PARES
                nodo_izq = transacciones[i]
                nodo_der = transacciones[i + 1] if i + 1 < len(transacciones) else None
                
                nuevo_nodo = Transaccion("", "", "")
                nuevo_nodo.izquierda = nodo_izq
                nuevo_nodo.derecha = nodo_der
                
                mensaje = f"{nodo_izq.hash}{nodo_der.hash if nodo_der else ''}".encode('utf-8')
                nuevo_nodo.hash = hashlib.sha256(mensaje).hexdigest()
                
                nuevos_nodos.append(nuevo_nodo)
            transacciones = nuevos_nodos
        self.raiz = transacciones[0]
    
    def generar_dot(self, nodo=None, dot_content=None):
        if dot_content is None:
            dot_content = "digraph MerkleTree {\n node[shape=record];"

        if nodo is None:
            nodo = self.raiz

        if nodo.id_cartera == "" :
            len_hash = len(nodo.hash)
            lbl = nodo.hash[:math.floor(len_hash/2)] + "\\n" + nodo.hash[math.floor(len_hash/2):]
            dot_content += f'  "{nodo.hash}" [label="{lbl}"];\n'
        else:
            dot_content += f'  "{nodo.hash}" [label="{nodo.label()}"];\n'

        if nodo.izquierda:
            dot_content += f'  "{nodo.izquierda.hash}" [label="{nodo.izquierda.label()}"];\n'
            dot_content += f'  "{nodo.hash}" -> "{nodo.izquierda.hash}"; \n'
            dot_content = self.generar_dot(nodo.izquierda, dot_content)

        if nodo.derecha:
            dot_content += f'  "{nodo.derecha.hash}" [label="{nodo.derecha.label()}"];\n'
            dot_content += f'  "{nodo.hash}" -> "{nodo.derecha.hash}" ;\n'
            dot_content = self.generar_dot(nodo.derecha, dot_content)
        return dot_content

