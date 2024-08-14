class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def ListarP(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def ListarF(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            return
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def Mostrar(self):
        a = self.cabeza
        while a:
            print(a.dato, end=("->"))
            a = a.siguiente
        print("None")

    def Long(self):
        a = self.cabeza
        cont = 0
        while a:
            cont +=1
            a = a.siguiente
        print("la cantidad de valores de la lista es de: " + str(cont))

    def Eliminar(self, dato):
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(True)
        else:
            actual = self.cabeza
            bandera = False
            while actual.siguiente:
                if actual.siguiente.dato == dato:
                    actual.siguiente = actual.siguiente.siguiente
                    bandera = True
                    print(True)
                actual = actual.siguiente
            if bandera == False:
                print(False)

    
    def OrdB(self):
        bandera = True
        while bandera:
            bandera = False
            actual = self.cabeza
            while actual and actual.siguiente:
                if actual.dato > actual.siguiente.dato:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                    bandera = True
                actual = actual.siguiente

    def Ordenamiento_por_seleccion(self):
        a = self.cabeza
        while a:
            ord = a
            siguiente = a.siguiente
            while siguiente:
                if siguiente.dato < ord.dato:
                    ord = siguiente
                siguiente = siguiente.siguiente
            temp = a.dato
            a.dato = ord.dato
            ord.dato = temp
            a = a.siguiente
        
                

a = Lista()
a.ListarF(8)
a.ListarF(3)
a.ListarF(4)
a.ListarF(11)
a.ListarP(10)
a.ListarP(45)
a.ListarP(8)
a.ListarP(76)
a.Mostrar()
# a.OrdB()
a.Ordenamiento_por_seleccion()
a.Mostrar()

