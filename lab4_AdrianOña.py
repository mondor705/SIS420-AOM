# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13hU_YmXlgonvnLaMOFvauoVndNZYksYR
"""

#Laboratorio 04
#Integrante: Adrian Oña Medrano
#descripcion:
#A partir del codigo fuente del aachivo bpa (Busqueda promero en anchura), modificar el mismo para encontrar la sulucion, pero utilizando una lista_frontera ordenada de mayor
# a menor valor que cada nodo pueda tener en su campo costo, ese valor debe llenarselo de manera aleatoria en el momento de creacion del nodo. Una vez implementado se debe describir 
#que sucede y que capacidad de resolver rompecabezas lineales de 4, 6, 7, 8, 9, 10, .... se puede resolver con el mismo. Alguna menora o criterio que usted considere es importante realizar
# para mejorar la capacidad de resolucion. toda la explicación se debe incluir en el codigo fuente.
#Primero me base en el laboratorio anterior, añadiendole un valor random al costo y despues poniendoselo a los nodos que se iban creando en la lista de nodos frontera y visitados
#luego tambien cree una funcion comparar y use un sorted para que vaya ordenandolo el nodo frontera en base a los parametros de comparacion
#por ultimo se uso unos time para sacar el tiempo de jecucion y cuanto era el coste.

#
import random
import time

class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)
        
    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self
                
    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    
    def __str__(self):
        return str(self.get_datos())

def bpa(estado_inicio, estado_solucion,tamaño):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    
    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
           hijo1_datos = nodo_actual.get_datos().copy()
           hijo=hijo1_datos
           for i in range (1,tamaño):   
            for j in range(0,tamaño-1):

              if hijo1_datos[j]>hijo1_datos[j+1]:

                temp = hijo1_datos[j]
                n=j+1
                hijo[j] = hijo[n]
                hijo[n] = temp
                nRandom=random.randrange(0,1)
                hijo1 = Nodo(hijo)
                hijo1.set_costo(nRandom)
                print(hijo1_datos)
                
              if not hijo1.en_lista(nodos_visitados) and not hijo1.en_lista(nodos_frontera):
                nodo_actual.set_hijo(hijo1)
                nodos_frontera.append(hijo1)
            nodos_frontera = sorted(nodos_frontera, key=Comparar, reverse= True)
def Comparar(nodo):
    return nodo.get_costo()

if __name__ == "__main__":
    estado_inicial = [10,9,8,7,6,5,4, 3, 2, 1]
    solucion = [1, 2, 3, 4,5,6,7,8,9,10]
    start= time.time()
    tam= len(solucion)
    nodo_solucion = bpa(estado_inicial, solucion,tam)
    end=time.time()
    print("El tiempo de ejecucion es: " ,end-start, "seg.")

    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo: %s" % str(nodo_solucion.get_costo()))