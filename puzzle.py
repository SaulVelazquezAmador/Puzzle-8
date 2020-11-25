import copy
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.padre = None
        self.hijos = []

    def buscar_guion(self):
        fila=0
        for i in self.dato:
            columna=0
            for j in i:
                if j == "-":
                    return columna,fila
                columna+=1
            fila+=1

    def generar_hijos(self):
        columna, fila = self.buscar_guion()

        if fila > 0:
            arriba = copy.deepcopy(self.dato)
            aux = arriba[fila][columna]
            arriba[fila][columna] = arriba[fila-1][columna]
            arriba[fila-1][columna] = aux
            nuevo = Nodo(arriba)
            self.hijos.append(nuevo)

        if fila < 2:
            abajo = copy.deepcopy(self.dato)
            aux = abajo[fila][columna]
            abajo[fila][columna] = abajo[fila+1][columna]
            abajo[fila+1][columna] = aux
            nuevo = Nodo(abajo)
            self.hijos.append(nuevo)

        if columna > 0:
            izquierda = copy.deepcopy(self.dato)
            aux = izquierda[fila][columna]
            izquierda[fila][columna] = izquierda[fila][columna-1]
            izquierda[fila][columna-1] = aux
            nuevo = Nodo(izquierda)
            self.hijos.append(nuevo)

        if columna < 2:
            derecha = copy.deepcopy(self.dato)
            aux = derecha[fila][columna]
            derecha[fila][columna] = derecha[fila][columna+1]
            derecha[fila][columna+1] = aux
            nuevo = Nodo(derecha)
            self.hijos.append(nuevo)

    def expandir(self):
        if len(self.hijos) == 0:
            self.generar_hijos()
            return
        for hijo in self.hijos:
            hijo.expandir()

    def buscar(self, meta):
        if self.dato == meta:
            for i in range(0,3):
                for j in range(0,3):
                    print(self.dato[i][j]+"\t",end="")
                print("\n")
            print("\n")
            return True
        for hijo in self.hijos:
            respuesta = hijo.buscar(meta)
            if respuesta == True:
                for i in range(0,3):
                    for j in range(0,3):
                        print(self.dato[i][j]+"\t",end="")
                    print("\n")
                print("\n")
                return True
        return False

    def comenzar(self):
        while True:
            encontrado = self.buscar(meta)
            if encontrado == True:
                break
            self.expandir()

inicial = [[0,0,0],[0,0,0],[0,0,0]]
meta = [[0,0,0],[0,0,0],[0,0,0]]
while True:
    opcion = 0
    print("1. Ingresar estados")
    print("2. Buscar resultado")
    print("3. Salir")
    opcion = int(input("-->"))

    if opcion == 1:
        print("Ingrese el estado inicial: ")

        for i in range(0,3):
            for j in range(0,3):
                inicial[i][j] = input("--> ")

        print("Ingrese el estado meta: ")

        for i in range(0,3):
            for j in range(0,3):
                meta[i][j] = input("--> ")
        
        arbol = Nodo(inicial)

    if opcion == 2:
        arbol.comenzar()
    if opcion == 3:
        break