import numpy as np
from claseNodo import Nodo

class ListaSecuecial:
    __maximo = None
    __ult = None
    __lista = None
    
    def __init__(self, maximo = 10):
        self.__lista = np.empty(maximo,dtype=int)
        self.__maximo = maximo
        self.__ult = 0
    
    def lleno(self):
        return (self.__ult == self.__maximo-1)
    
    def vacio(self):
        return (self.__ult == 0)
            
    def shift(self,i):
        j = self.__ult
        while j > i:
            self.__lista[j] = self.__lista[j-1]
            j-=1
            
    def suprimir(self,elemento):
        assert isinstance(elemento, int)
        if not self.vacio():
            i = 0
            encontro = False
            while not encontro and i <= self.__ult-1:
                if self.recuperar(i) == elemento:
                    self.rshift(i)
                    self.__ult-=1
                    encontro = True
                else:
                    i += 1
            if not encontro:
                print('ERROR: Elemento no encontrado')
               
                    
    def rshift(self,i):
        while i <= self.__ult:
            self.__lista[i] = self.__lista[i+1]
            i+=1

    def insertar(self,elemento):
        assert isinstance(elemento, int)
        if not self.lleno():
            i = 0
            if self.vacio():
                self.__lista[i] = elemento
                self.__ult+=1
            else:
                encontro = False
                while not encontro and i<=self.__ult-1:
                    if self.recuperar(i) < elemento:
                        self.shift(i)
                        self.__lista[i] = elemento
                        self.__ult+=1
                        encontro = True
                    else:
                        i+=1
                
                if not encontro:#Si el elemento debe ir al final..
                    self.__lista[i] = elemento
                    self.__ult+=1           
        else:
            print('ERROR: no hay espacio')
    
    def recorrer(self):
        if not self.vacio():
            for i in range(self.__ult):
                print(self.__lista[i])
        else:
            print('ERROR: Lista vacia!')
    
    def recuperar(self, p):
        val = None
        if not self.vacio():
            if p >= 0 and p <= self.__ult-1:
                    val = self.__lista[p]
        return val

    def buscar(self, elemento):
        encontro = False
        i = 0
        val = None
        while not encontro and i<=self.__ult-1:
            if self.__lista[i] == elemento:
                encontro = True
                val = i
            else:
                i+=1
        if not encontro:
            print('ERROR: elemento no encontrado!')
        return val
        
    def primer_elemento(self):
        val = None
        if not self.vacio():
            val = self.__lista[0]
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def ultimo_elemento(self):
        val = None
        if not self.vacio():
            val = self.__lista[ult-1]
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def siguiente(self, p):
        if not self.vacio():
            val = None
            if p-1 >= 0 and p-1 < self.__ult-1:

                val = p+1
            else:
                print('ERROR: No hay mas elementos despues de la posicion ingresada!')
        else:
            print('ERROR: Lista vacia!')
    
class ListaEncadenada:
    __cab = None
    __cant = None
    
    def __init__(self):
        self.__cab = None
        self.__cant = 0
    
    def vacia(self):
        return (self.__cab == None)

    def insertar(self, elemento):
        i = 0
        aux = self.__cab
        ant = self.__cab
        encontro = False
        if self.vacia():
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__cab)
            self.__cab = nodo
            self.__cant+=1
        else:
            while not encontro and aux != None:
                if self.recuperar(i) < elemento:
                    encontro = True
                else:
                    i+=1
                    ant = aux
                    aux = aux.getSiguiente()
            if i == 0:
                nodo = Nodo(elemento)
                nodo.setSiguiente(self.__cab)
                self.__cab = nodo
                self.__cant+=1
            else:
                nodo = Nodo(elemento)
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__cant+=1
            
        
    
    def suprimir(self, elemento):
        enconto = False  
        i = 0
        ant = self.__cab
        aux = self.__cab
        while not enconto and aux != None:
            if self.recuperar(i) == elemento:
                enconto = True
            else:
                i+=1
                ant = aux
                aux = aux.getSiguiente()
        if i == 0:
            self.__cab = self.__cab.getSiguiente()
        else:
            ant.setSiguiente(aux.getSiguiente())
        if not enconto:
            print('ERROR: elemento no encontrado')
        
            
    def buscar(self, elemento):
        val = None
        if not self.vacia():
            encontro = False
            aux = self.__cab
            i = 0
            while not encontro and aux != None:
                if self.recuperar(i) == elemento:
                    encontro = True
                    val = i
                else:
                    i+=1
                    aux = self.siguiente(i)
            if not encontro:
                print('ERROR: elemento no encontrado!')
        else:
            print('ERROR: Lista vacia!')
        return val

    
    def recorrer(self):
        if not self.vacia():
            aux = self.__cab
            while aux != None:
                print('{}'.format(aux.getDato()))
                aux = aux.getSiguiente()
        else:
            print('ERROR: Lista vacia!')
    
    def recuperar(self, p):
        val = None
        if not self.vacia():
            i = 0
            if p >= 0 and p <= self.__cant-1:
                encontro = False
                aux = self.__cab
                while not encontro and aux != None:
                    if i == p:
                        encontro = True
                    else:
                        i+=1
                        aux= aux.getSiguiente()
                val = aux.getDato()
        return val
    
    def siguiente(self, p):
        val = None
        if not self.vacia():
            if p >= 0 and p < self.__cant-1:
                aux = self.__cab
                i = 0
                encontro = False
                while not encontro and aux != None:
                    if i == p:
                        encontro = True
                    else:
                        i+=1
                        aux = aux.getSiguiente()
                val = aux.getSiguiente()
        return val
    
    def anterior(self,p):
        val = None
        if not self.vacia():
            if p > 0 and p <= self.__cant-1:
                aux = self.__cab
                ant = aux
                i = 0
                encontro = False
                while not encontro and aux != None:
                    if i == p:
                        encontro = True
                    else:
                        ant = aux
                        aux = self.siguiente(i)
                        i+=1
                val = ant
              
        return val
    
    def primer_elemento(self):
        val = None
        if not self.vacia():
            val = self.recuperar(1)
        else:
            print('ERROR: lista vacia!')
        return val
    
    def ultimo_elemento(self):
        val = None
        if not self.vacia():
            val = self.recuperar(self.__cant)
        else:
            print('ERROR: lista vacia!')
        return val


if __name__ == '__main__':
    objLista = ListaSecuecial()
    print('-------')
    objLista.insertar(1)
    objLista.insertar(-1)
    objLista.recorrer()
    objLista.suprimir(1)
    objLista.recorrer()
    print('-------------')
   

