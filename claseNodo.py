class Nodo(object):
    __elemento = None
    __siguiente = None
    
    def __init__(self, elemento):
        assert isinstance(elemento, int)
        self.__elemento = elemento
        self.__siguiente = None
    
    def getSiguiente(self):
        return self.__siguiente    
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getDato(self):
        return self.__elemento