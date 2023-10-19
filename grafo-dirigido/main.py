from edd.grafo import Grafo

grafoAntecesores = Grafo()
grafoSucesores = Grafo()


vertices = ["T1-PY-100","T2-PY-100","T3-PY-100","T4-PY-100","T5-PY-100"]
for valor in vertices:
    grafoAntecesores.insertarFila(valor)
grafoAntecesores.agregarNodo("T3-PY-100","T1-PY-100")
grafoAntecesores.agregarNodo("T3-PY-100","T2-PY-100")
grafoAntecesores.agregarNodo("T5-PY-100","T3-PY-100")
grafoAntecesores.agregarNodo("T5-PY-100","T4-PY-100")
print("Tareas con sus antecesores")
grafoAntecesores.verMatriz()
grafoAntecesores.Grafico("antecesores")


print('\n')
for valor in vertices:
    grafoSucesores.insertarFila(valor)
grafoSucesores.agregarNodo("T1-PY-100","T3-PY-100")
grafoSucesores.agregarNodo("T2-PY-100","T3-PY-100")
grafoSucesores.agregarNodo("T3-PY-100","T5-PY-100")
grafoSucesores.agregarNodo("T4-PY-100","T5-PY-100")
print("Tareas con sus sucesores")
grafoSucesores.verMatriz()
grafoSucesores.Grafico("sucesores")