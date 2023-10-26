from edd.merkle import ArbolMerkle, Transaccion
from edd.blockchain import BlockChain


# CREACION DE ARBOL MERKLE
arbol = ArbolMerkle()
temp = [
    Transaccion("oiasmd1920","120","PY-100"),
    Transaccion("ksadl12o1i","920","PY-100"),
    Transaccion("saklmd9121","320","PY-100"),
    Transaccion("alksdo2212","240","PY-100")
]
arbol.crear_arbol(temp)
# CREACION DEL BLOCKCHAIN
bloques = BlockChain()
for transaccion in temp:
    bloques.insertar(transaccion)
print(bloques)