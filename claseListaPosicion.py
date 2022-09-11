import numpy as np
from claseNodo import Nodo

class ListaSecuecial:
    __maximo = None
    __ult = None
    __lista = None
    
    def __init__(self, maximo = 3):
        self.__lista = np.empty(maximo,dtype=int)
        self.__maximo = maximo
        self.__ult = 0
    
    def lleno(self):
        return (self.__ult > self.__maximo-1)
    
    def vacio(self):
        return (self.__ult == 0)
            
    def shift(self,i):
        j = self.__ult
        while j > i:
            self.__lista[j] = self.__lista[j-1]

            j-=1
            
    def suprimir(self,posicion):
        if not self.vacio():
            if (posicion) >= 1 and (posicion) <= self.__ult:
                for i in range(self.__ult):
                    if i == posicion-1:
                        self.rshift(i)
                        self.__ult-=1
                    
    def rshift(self,i):
        while i <= self.__ult:
            self.__lista[i] = self.__lista[i+1]
            i+=1

    def insertar(self,elemento,p):
        assert isinstance(elemento, int)
        if not self.lleno():
            if (p) >= 1 and (p) <= self.__ult+1:
                i = 0
                encontro = False
                while not encontro:
                    if i == p-1:
                        self.shift(i)
                        self.__lista[i] = elemento
                        self.__ult+=1
                        encontro = True
                    else:
                        i+=1
                    
            
            else:
                print('ERROR: posicion no valida')
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
            if p-1 >= 0 and p-1 <= self.__ult-1:
                    val = self.__lista[p-1]
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
            val = self.__lista[self.__ult-1]
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
    

    def anterior(self, p):
        if not self.vacio():
            val = None
            if p-1 > 0 and p-1 <= self.__ult-1:
                val = p-1
            else:
                print('ERROR: No hay una posicion anterior a la ingresada!')
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

    def insertar(self, elemento, p):
        if p>= 1 and p<= self.__cant+1:
            i = 0
            aux = self.__cab
            ant = self.__cab
            encontro = False
            if p-1 == 0:#CASO 1: insertar al comienzo de la lista
                nodo = Nodo(elemento)
                nodo.setSiguiente(self.__cab)
                self.__cab = nodo
                self.__cant+=1
            else: #CASO 2: insertar al medio o al final de la lista
                while not encontro and   aux != None:
                    if i == p-1:
                        encontro = True
                    else:
                        ant = aux
                        aux = aux.getSiguiente()
                        i+=1
                        
                nodo = Nodo(elemento)
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__cant+=1
        else:
                print('ERROR: Posicion no valida')
    
    def suprimir(self, p):
        if p>= 0 and p<=self.__cant:
            enconto = False
          
            i = 0
            if p-1 == 0:#CASO 1: Se quiere eliminar el primer nodo de la lista
                self.__cab = self.__cab.getSiguiente()
            else:
                aux = self.__cab
                ant = aux
                while aux != None and not enconto: #CASO 2: Se quiere eliminar un nodo intermedio o el ultimo nodo de la lista
                    if i == p-1:
                        enconto = True
                    else:
                        i+=1
                        ant = aux
                        aux = aux.getSiguiente()
                ant.setSiguiente(aux.getSiguiente())
                self.__cant-=1
        else:
            print('ERROR: Posicion no valida!')
            
    
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
            if p -1 >= 0 and p -1 <= self.__cant-1:
                encontro = False
                aux = self.__cab
                while not encontro and aux != None:
                    if i == p-1:
                        encontro = True
                    else:
                        aux= self.siguiente(i)
                        i+=1
                val = aux.getDato()
        return val

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
            if p > 1 and p <= self.__cant:
                aux = self.__cab
                ant = aux
                i = 0
                encontro = False
                while not encontro and aux != None:
                    if i == p-1:
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
    objLista = ListaEncadenada()
    print('-------')
    objLista.insertar(1,1)
    objLista.insertar(2,2)
    objLista.insertar(3, 3)
    objLista.recorrer()
    print('-----------')
    objLista.suprimir(2)
    objLista.recorrer()
    print('--------')
 
