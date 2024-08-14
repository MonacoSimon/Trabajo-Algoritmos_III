import csv
class Pasajero:
    def __init__(self, PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked):
        self.PassengerId = int(PassengerId)
        self.Survived = int(Survived)
        self.Pclass = int(Pclass)
        self.Name = Name
        self.Sex = Sex
        self.Age = round(float(Age)) if Age else 0
        self.SibSp = int(SibSp)
        self.Parch = int(Parch)
        self.Ticket = Ticket
        self.Fare = float(Fare)
        self.Cabin = Cabin
        self.Embarked = Embarked

    def __str__(self):
        return f'{self.PassengerId}, {self.Name}, {self.Age}, {self.Pclass}'

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def InsertarPrincipio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Long(self):
        a = self.cabeza
        cont = 0
        while a:
            cont +=1
            a = a.siguiente
        print("la cantidad de nodos es de: " + str(cont))
    def Eliminar(self, eliminar):
        if self.cabeza.dato == eliminar:
            self.cabeza = self.cabeza.siguiente
            return
        else:
            a = self.cabeza
            while a.siguiente:
                if a.dato == eliminar:
                    a.siguiente = a.siguiente.siguiente
                a = a.siguiente

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            return
        else:
            a = self.cabeza
            while a.siguiente:
                a = a.siguiente
            a.siguiente = nuevo_nodo

    def Vacia(self):
        if self.cabeza == None:
            return None

    def Mostrar(self):
        a = self.cabeza
        while a:
            print(a.dato, end=(" -> "))
            a = a.siguiente
        print("None")

    def ordenamiento_burbuja(self):
        cambio = True
        while cambio:
            cambio = False
            a = self.cabeza
            while a:
                if a.dato > a.siguiente.dato:
                    aux = a.siguiente.dato
                    a.siguiente.dato = a.dato
                    a.dato = aux
                    cambio = True
                a = a.siguiente

    def obtener_lista_clase(self, Pclass):
        a = self.cabeza 
        sublista = Lista()
        while a:
            if a.dato.Pclass == Pclass:
                sublista.insertar_al_final(a.dato) 
            a = a.siguiente 
        return sublista 
    
    def obtener_lista_mayor_edad(self):
        sublistaMayores = Lista()
        subListaMenores = Lista()
        a = self.cabeza
        while a:
            if a.dato.Age >= 18:
                sublistaMayores.insertar_al_final(a.dato)
            else:
                subListaMenores.insertar_al_final(a.dato)
            a = a.siguiente
        return subListaMenores, sublistaMayores


 
def leer_csv(archivo):
    with open(archivo, mode='r') as Titanic:
        lector = csv.reader(Titanic)
        for linea in lector:
            print(linea) 


def crear_pasajero(ruta_archivo):
    pasajeros = []
    with open(ruta_archivo, mode='r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            pasajero = Pasajero(
                PassengerId=fila['PassengerId'],
                Survived=fila['Survived'],
                Pclass=fila['Pclass'],
                Name=fila['Name'],
                Sex=fila['Sex'],
                Age=fila['Age'],
                SibSp=fila['SibSp'],
                Parch=fila['Parch'],
                Ticket=fila['Ticket'],
                Fare=fila['Fare'],
                Cabin=fila['Cabin'],
                Embarked=fila['Embarked']
            )
            pasajeros.append(pasajero)
    return pasajeros
def Insertar_Pasajero(pasajeros):
    listaPasajero = Lista()
    cont = 0
    for pasajero in pasajeros:
        cont +=1
        listaPasajero.insertar_al_final(pasajero)
    return listaPasajero

pasajeros =crear_pasajero('Titanic.csv')

a = Lista()
lista = Insertar_Pasajero(pasajeros)


sublista_menores, sublista_mayores = lista.obtener_lista_mayor_edad()

# Mostrar pasajeros menores de 18 años
print("Menores de 18:")
sublista_menores.Mostrar()

# Mostrar pasajeros mayores de 18 años
# print("Mayores de 18:")
# sublista_mayores.Mostrar()


