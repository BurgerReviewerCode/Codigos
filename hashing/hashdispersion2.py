class nodo:
    clave=int
    valor=str
    siguiente=object
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None
    
    def getclave(self):
        return self.clave
    def getvalor(self): 
        return self.valor
    def getsig(self):
        return self.siguiente
    
    def setsig(self, sig):
        self.siguiente = sig
    def setvalor(self, valor):
        self.valor = valor
    def setclave(self, clave):
        self.clave = clave

class dispersor:
    lista=[]
    dimension=int
    componente=object

    def __init__(self,dimension):
        self.dimension = dimension
        self.lista = [None]*dimension
        componente = nodo(None,None)

    def hash_division(self, valor):
        return valor%self.dimension
    
    def hash_extraccion(self, valor):
        valorx=int(valor) / 100
        valorx=int(valorx) % 1000
        valorx=int(valorx)
        return valorx%self.dimension

    def hash_plegado(self, valor):
        valorx=str(valor)
        longitud=len(valorx)
        acum=0
        i=0
        for i in range(0, longitud, 2):
            acum+=int(valorx[i]+valorx[i+1])
        return acum%self.dimension

    def hash_halfcube(self, valor):
        valorx=valor*valor
        valorx=int(valorx)/10000000
        valorx=int(valorx)%100
        return valorx%self.dimension
    
    def hash_alfa(self, valor):
        valorx="".join(str(ord(c)) for c in valor)
        valorfinal=int(valorx)%self.dimension
        return valorfinal

    def insertar(self, dato, tipo):
        if tipo=="plegado":
            indice=self.hash_plegado(dato)
        elif tipo=="division":
            indice=self.hash_division(dato)
        elif tipo=="extraccion":
            indice=self.hash_extraccion(dato)
        elif tipo=="halfcube":
            indice=self.hash_halfcube(dato)
        elif tipo=="alfa":
            indice=self.hash_alfa(dato)
        if self.lista[indice] is None:
            # self.lista[indice]=nodo(indice, dato)
            # actual=self.items[indice]
            actual=nodo(indice,dato)
            actual.setclave(indice)
            actual.setvalor(dato)
            actual.setsig(None)
            self.lista[indice]=actual
            # print("Colisiones detectadas: 0")
        else:
            nuevo=nodo(indice,dato)
            actual=self.lista[indice]
            nuevo.settrue
            actual.setfalse
            nuevo.setvalor(dato)
            nuevo.setclave(indice)
            nuevo.setsig(actual)
            self.lista[indice]=nuevo

    def mostrar(self, valor, tipo):
        if tipo=="halfcube":
            indice=self.hash_halfcube(valor)
        elif tipo=="alfa":
            indice=self.hash_alfa(valor)
        if self.lista[indice].getvalor()==valor:
            print(self.lista[indice].getvalor())
            print("Encontrado!")
        else:
            enc=False
            sig=self.lista[indice].getsig
            while enc==False and sig!=None:
                if self.lista[indice].getvalor==valor:
                    print(self.lista[indice].getvalor)
                    print("Encontrado!")


if __name__=="__main__":
    listado=dispersor(67)
    listado.insertar("E010-267","alfa")
    listado.mostrar("E010-267","alfa")
    listado.insertar(45212557,"halfcube")
    listado.mostrar(45212557,"halfcube")